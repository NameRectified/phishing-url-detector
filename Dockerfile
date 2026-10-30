FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./

RUN pip install --no-cache-dir uv && uv sync --frozen --no-dev

COPY feature_extraction.py predict.py best_model.joblib ./

EXPOSE 9696

CMD ["uv", "run", "--frozen", "--no-sync", "uvicorn", "predict:app", "--host", "0.0.0.0", "--port", "9696"]