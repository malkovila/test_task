FROM python

WORKDIR /ReadMaster

RUN export DOCKER_BUILDKIT=0 \
    export COMPOSE_DOCKER_CLI_BUILD=0 \
    pip install pymysql \
    pip install MIMEText \
    pip install Process \
    pip install flask 


COPY . .

CMD ["python", "main.py"]