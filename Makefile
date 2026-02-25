# --- Configuration ---
PYTHON = python
# FastAPI Paths
FASTAPI_DIR = fastapi_codes
FASTAPI_VENV = $(FASTAPI_DIR)/expense_venv
FASTAPI_PY   = $(FASTAPI_VENV)/Scripts/python.exe

# Playwright Paths
PLAY_DIR  = playwright_codes
PLAY_VENV = $(PLAY_DIR)/ui_venv
PLAY_PY   = $(PLAY_VENV)/Scripts/python.exe
FILE ?= test_day1_topic.py
BROWSER ?= chromium
HEADLESS ?= --headed

.PHONY: help install-fastapi install-playwright run-fastapi

help:
	@echo "Available Commands:"
	@echo "  make install-fastapi    - Update FastAPI dependencies using expense_venv"
	@echo "  make install-playwright - Update Playwright dependencies using ui_venv"
	@echo "  make run-fastapi        - Start the FastAPI server"

# --- FastAPI Logic ---
install-fastapi:
	$(FASTAPI_PY) -m pip install --upgrade pip
	$(FASTAPI_PY) -m pip install -r $(FASTAPI_DIR)/requirements.txt

run-fastapi:
	cd $(FASTAPI_DIR) && ../$(FASTAPI_PY) -m uvicorn app.main:app --reload

# --- Playwright Logic ---
install-playwright:
	$(PLAY_PY) -m pip install --upgrade pip
	$(PLAY_PY) -m pip install -r $(PLAY_DIR)/requirements.txt
	$(PLAY_PY) -m playwright install

# Usage: make test-playwright FILE=test_day1_topic.py
test-playwright:
# 	$(PLAY_PY) -m pytest $(PLAY_DIR)/$(FILE) --browser $(BROWSER) $(HEADLESS)
# 	$(PLAY_PY) -m pytest $(PLAY_DIR)/$(FILE) -s -v --browser $(BROWSER) $(HEADLESS) --html=report.html
# 	$(PLAY_PY) -m pytest $(PLAY_DIR)/$(FILE) -s -v --browser $(BROWSER) $(HEADLESS) --html=report.html --self-contained-html
	$(PLAY_PY) -m pytest $(PLAY_DIR)/$(FILE) -s -v --browser $(BROWSER) $(HEADLESS)
