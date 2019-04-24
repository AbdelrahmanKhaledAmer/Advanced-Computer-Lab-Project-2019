#################################################################################
# GLOBALS                                                                       #
#################################################################################
MAKEFLAGS = -s
PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))

PYTHON_INTERPRETER = python
ANTLR = antlr4 -Dlanguage=Python3 -lib $(PROJECT_DIR)/milestone1/src

# variables for active milestone
MILESTONE =				# indicates the active network

#################################################################################
# MILESTONE COMMANDS                                                            #
#################################################################################
.PHONY: milestone1 m1
## Sets active milestone to milestone1
milestone1 m1:
	$(eval MILESTONE=1)


.PHONY: milestone2 m2
## Sets active milestone to milestone2
milestone2 m2:
	$(eval MILESTONE=2)


.PHONY: test
## Runs MILESTONE/test.py
test:
	cd "${PROJECT_DIR}" && $(PYTHON_INTERPRETER) -m milestone$(MILESTONE).test


.PHONY: gen
## Generate Antlr files
gen:
	cd "${PROJECT_DIR}/milestone${MILESTONE}/src" && $(ANTLR) "${PROJECT_DIR}/milestone${MILESTONE}/src/milestone_$(MILESTONE).g4"


#################################################################################
# MISC COMMANDS                                                                 #
#################################################################################
.PHONY: clean
## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type f -name "*.tokens" -delete
	find . -type f -name "*Lexer.py" -delete
	find . -type f -name "*Parser.py" -delete
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*Listener.py" -delete
	find . -type d -name ".ipynb_checkpoints" -exec rm -rv {} +
