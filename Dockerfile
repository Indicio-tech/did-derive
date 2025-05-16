ARG PY_BASE=3.12-slim
FROM python:$PY_BASE AS builder
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Change the working directory to the `app` directory
WORKDIR /app

COPY pyproject.toml uv.lock README.md /app/
# Install dependencies
RUN uv sync --locked --no-install-project --no-editable

# Copy the project into the intermediate image
COPY src /app/

# Sync the project
RUN uv sync --locked --no-editable

FROM python:$PY_BASE

# Copy the environment, but not the source code
COPY --from=builder /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

# Run the application
CMD ["did-derive-default"]
