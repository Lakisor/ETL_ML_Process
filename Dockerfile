FROM python:3.11-slim

RUN apt-get update && apt-get install -y curl unzip && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh

ENV PATH="/root/.local/bin:${PATH}"

WORKDIR /app

COPY pyproject.toml uv.lock requirements.txt ./

RUN uv sync --frozen

COPY . .

ENV PYTHONPATH=/app

CMD ["uv", "run", "python", "main.py"]
