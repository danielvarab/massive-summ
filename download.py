import argparse
import gzip
import io
import json
import random
from multiprocessing import Pool

import requests
from tqdm import tqdm


def load_samples(filename: str) -> list:
    samples = []
    with gzip.open(filename) as fh_in:
        for row in tqdm(fh_in):
            sample = json.loads(row)
            samples.append(sample)
    return samples


def download_sample(sample: dict) -> dict:
    filename = sample["filename"]
    length = int(sample["length"])
    offset = int(sample["offset"])

    offset_end = offset + length - 1
    # We'll get the file via HTTPS so we don't need to worry about S3 credentials
    # Getting the file on S3 is equivalent however - you can request a Range
    prefix = "https://commoncrawl.s3.amazonaws.com/"
    # We can then use the Range header to ask for just this set of bytes
    try:
        resp = requests.get(
            prefix + filename,
            headers={"Range": "bytes={}-{}".format(offset, offset_end)},
        )

        compressed_file = io.BytesIO(resp.content)
        decompressed_file = gzip.GzipFile(fileobj=compressed_file)
        data = decompressed_file.read().decode()
        warc, header, response = data.strip().split("\r\n\r\n", 2)
        return {"language": sample["annotated_language"], "html": response}
    except:
        print(">> url sample:")
        with open("error.log", "at") as err_log:
            err_log.write(json.dumps(sample) + "\n")
        # pprint.pprint(sample)
        return None


def download_list(samples, n_processes: int):
    with Pool(n_processes) as pool:
        for sample in pool.imap_unordered(download_sample, samples):
            if sample:  # don't yield failing samples
                yield sample


def run(url_file: str, archive_file: str, n_proc: int, limit: int):
    samples = load_samples(url_file)
    if limit > 0:
        samples = random.sample(samples, limit)

    with gzip.open(archive_file, "at") as fh_out:
        for sample in tqdm(
            download_list(samples, n_processes=n_proc), total=len(samples)
        ):
            fh_out.write(json.dumps(sample) + "\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--urls", required=True)
    parser.add_argument("--archive", required=True)
    parser.add_argument("--n_proc", type=int, required=True)
    parser.add_argument("--limit", type=int, default=-1)

    args = parser.parse_args()
    print(args)
    run(args.urls, args.archive, args.n_proc, args.limit)
