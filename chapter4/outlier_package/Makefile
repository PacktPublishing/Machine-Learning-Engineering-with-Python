# INSPIRED BY https://github.com/MartinHeinz/python-project-blueprint/blob/master/Makefile
# The binary to build (just the basename).
MODULE := outliers

# Where to push the docker image.
REGISTRY ?= docker.pkg.github.com/martinheinz/python-project-blueprint

IMAGE := $(REGISTRY)/$(MODULE)

# This version-strategy uses git tags to set the version string
TAG := $(shell git describe --tags --always --dirty)

BLUE='\033[0;34m'
NC='\033[0m' # No Color

run:
	@python -m $(MODULE)

test:
	@pytest

lint:
	@echo "\n${BLUE}Running Pylint against source and test files...${NC}\n"
	@pylint --rcfile=setup.cfg **/*.py
	@echo "\n${BLUE}Running Flake8 against source and test files...${NC}\n"
	@flake8
	@echo "\n${BLUE}Running Bandit against source files...${NC}\n"
	@bandit -r --ini setup.cfg

.PHONY: clean image-clean build-prod push test

clean:
	rm -rf .pytest_cache .coverage .pytest_cache coverage.xml

