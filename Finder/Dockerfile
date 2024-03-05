FROM python

WORKDIR /Finder

RUN export DOCKER_BUILDKIT=0 \
    export COMPOSE_DOCKER_CLI_BUILD=0 \
    pip install watchdog \
    pip install os \
    pip install shutil \
    pip install pika \
    pip install re \
    pip install logging \


COPY . .

CMD ["python", "main.py"]