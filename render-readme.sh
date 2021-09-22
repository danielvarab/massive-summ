#!/bin/sh
LANGS=$(csvtomd cc-urls.csv -d "$(echo '\t')")
export LANGS

cat readme.md.template | envsubst > readme.md
echo readme.md is updated