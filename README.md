# validator_db_endpoint

## Introduce

This is the endpoint to connect validators and indexing db of scraping subnet.
Validators can access via this endpoint and can add meta info about their uploaded data of wasabi s3.

There's one more function.
That is to generate api_key for accessing to this endpoint.

## Install environments.

```bash
python -m pip install -r requirements.txt
```

And make `.env` file from `.env.example`.

## Running app

Please run this code on terminal.
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

## Generate api key.

Please run this code on terminal.

```bash
python api_key.py
```