# Validator Indexing Database Endpoint

## Overview

This endpoint facilitates the connection between validators and the indexing database of the scraping subnet. Validators can interact with this endpoint to add metadata about their uploaded data to the Wasabi S3.

An additional feature of this endpoint is the generation of API keys for access.

## Environment Setup

To install the necessary environment, run the following command:

```bash
python -m pip install -r requirements.txt
```

Next, create a `.env` file using the provided `.env.example` as a template.

## Running the Application

To start the application, execute the following command in your terminal:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## API Key Generation

To generate an API key, run the following command in your terminal:

```bash
python api_key.py
```