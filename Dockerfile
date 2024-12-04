ARG PY_BASE=3.12-slim
FROM python:$PY_BASE AS builder
RUN pip install -U pdm
ENV PDM_CHECK_UPDATE=false
COPY pyproject.toml pdm.lock README.md /usr/src/app/
COPY src/ /usr/src/app/src
WORKDIR /usr/src/app
RUN pdm install --check --prod --no-editable

FROM python:$PY_BASE
COPY --from=builder /usr/src/app/.venv /usr/src/app/.venv
ENV PATH="/usr/src/app/.venv/bin:$PATH"
ENTRYPOINT []
CMD ["did-derive-default"]
