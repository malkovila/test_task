FROM python

WORKDIR /Analizator


RUN export DOCKER_BUILDKIT=0 \
    export COMPOSE_DOCKER_CLI_BUILD=0 \
    pip install pika\
    pip install pymysql


COPY . .

CMD ["python", "main.py"]