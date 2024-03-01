FROM python

WORKDIR /Finder

RUN export DOCKER_BUILDKIT=0 \
    export COMPOSE_DOCKER_CLI_BUILD=0 \
    pip install watchdog

COPY . .

CMD ["python", "main.py"]