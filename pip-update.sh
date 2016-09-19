#!/bin/bash
workon nyt-prb-scraper

pandoc --from=markdown --to=rst --output=README.rst README.md

python setup.py sdist upload