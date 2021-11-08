#!/bin/sh
LANGS=$(csvtomd urls.tsv -d "$(echo '\t')")
export LANGS

cat readme.md.template | envsubst > readme.md
echo readme.md is updated