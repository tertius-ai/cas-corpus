.PHONY: check check-metadata

check:
	python3 tools/check_cases.py --execute

check-metadata:
	python3 tools/check_cases.py

