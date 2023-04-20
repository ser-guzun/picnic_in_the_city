FROM python:3.10.6-alpine

# set working directory
WORKDIR /app

# install python dependencies
RUN pip install --upgrade pip && pip install poetry

COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml
RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN python -m  pip install -r requirements.txt

# add app
ADD . .

CMD ["sh", "-c", "alembic upgrade head && uvicorn --host 0.0.0.0 --port 8000 src.main:app"]
