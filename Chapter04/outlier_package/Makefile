# INSPIRED BY https://github.com/MartinHeinz/python-project-blueprint/blob/master/Makefile
# The binary to build (just the basename).
MODULE := outliers

run:
	@python -m $(MODULE)

test:
	@pytest

#lint:
#	@echo "\n${BLUE}Running Pylint against source and test files...${NC}\n"
#	@pylint --rcfile=setup.cfg **/*.py
#	@echo "\n${BLUE}Running Flake8 against source and test files...${NC}\n"
#	@flake8
#	@echo "\n${BLUE}Running Bandit against source files...${NC}\n"
#	@bandit -r --ini setup.cfg

.PHONY: clean test

clean:
	rm -rf .pytest_cache .coverage .pytest_cache coverage.xml

