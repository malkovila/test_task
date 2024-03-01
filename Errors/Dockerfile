FROM python

WORKDIR /Errors

RUN export DOCKER_BUILDKIT=0 \
    export COMPOSE_DOCKER_CLI_BUILD=0 \
    pip install pika \
    pip install smtplib \
    pip install MIMEText    

COPY . .

CMD ["python", "main.py"]