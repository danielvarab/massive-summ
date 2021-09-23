"""
Copyright 2018 Max Grusky

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

This this file has been altered and adopted. Specifically, it is modified to accomodate
the common crawl archive instead of the waybackmachine.
"""

import gzip
import json
import os
from multiprocessing import Pool, cpu_count

import orjson
from tqdm import tqdm

from article import Article

PROCS = cpu_count()


def extract(archive, dataset, n_proc: int = PROCS, batch_size: int = PROCS * 20):

    previously = set()
    todo = set()

    if os.path.isfile(dataset):

        print("Comparing archive and dataset files: ", end="")

        with gzip.open(dataset) as dataset_file:

            for article in dataset_file:
                article = orjson.loads(article)
                url = article.get("archive", article.get("url"))
                previously.add(url)

        print("found", len(previously), "finished summaries... ", end="")
    else:
        print("Loading downloaded summaries: ", end="")

    with gzip.open(archive) as archive_file:
        for article in archive_file:
            article = orjson.loads(article)
            url = article.get("archive", article.get("url"))
            todo.add(url)

    todo -= previously

    print("found", len(todo), "new summaries.\n")

    with tqdm(total=len(todo), desc="Extracting Summaries") as progress:
        with gzip.open(archive) as archive_file:
            with gzip.open(dataset, "at") as dataset_file:

                chunk = []

                def process_batch():

                    with Pool(n_proc) as ex:
                        results = list(ex.map(Article.process, chunk))
                        results = [r for r in results if r is not None]

                        for result in results:
                            if result["text"] is None or result["summary"] is None:
                                continue
                            else:
                                dataset_file.write(json.dumps(result) + "\n")

                        progress.update(len(results))

                for article in archive_file:
                    article = orjson.loads(article)
                    url = article.get("archive", article.get("url"))
                    if url not in todo:
                        continue

                    chunk.append(article)
                    
                    if len(chunk) >= batch_size:
                        process_batch()
                        chunk = []

                process_batch()

    print("\nExtraction complete.")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument("--archive", required=True)
    parser.add_argument("--dataset", required=True)

    args = parser.parse_args()
    extract(args.archive, args.dataset, n_proc=PROCS)
