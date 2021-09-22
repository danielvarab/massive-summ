#!/bin/sh
LANGS=$(csvtomd cc-urls.tsv -d "$(echo '\t')")
export LANGS

cat readme.md.template | envsubst > readme.md
echo readme.md is updated