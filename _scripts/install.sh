#!/bin/bash

# Copy the .env file
cp .env.example .env

# Create virtual environment and then activate it
python -m venv _
source _/bin/activate


pip install --upgrade pip
# Install poetry, then use it to install dependencies
pip install poetry
poetry install
poetry run pre-commit install
