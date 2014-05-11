# Make file for building all the docs
# Inspired by Makefile used by Phraseanet-Docs
# https://github.com/alchemy-fr/Phraseanet-Docs
#

PYTHON = python

.PHONY: all clean html

# Languages that can be built.
LANGS = en zh-cn


# Dependencies to perform before running other builds
SPHINX_DEPENDENCIES = $(foreach lang, $(LANGS), $(lang)/Makefile)

# Clone the en/Makefile everywhere
%/Makefile: en/Makefile
	cp $< $@



#
# Loop over the possible languages and call other build targets
#
html: $(foreach lang, $(LANGS), html-$(lang))



# make with correctly nested language folders
html-%: $(SPHINX_DEPENDENCIES)
	cd $* && make html LANG=$*


clean:
	rm -rf _build/*
