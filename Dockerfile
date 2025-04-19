FROM python:3.12-slim
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app
COPY . . 

RUN pip install --no-cache-dir poetry==2.0.0

RUN poetry config installer.max-workers 10
RUN poetry install --no-interaction --no-ansi

EXPOSE 8000
CMD ["poetry", "run", "uvicorn", "--host", "0.0.0.0", "fast_api_do_zero.app:app"]
