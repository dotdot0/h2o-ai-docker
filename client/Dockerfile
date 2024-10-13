FROM alpine:latest

RUN apk add --no-cache \
    python3 py3-pip python3-dev 

RUN pip3 install --break-system-packages virtualenv

RUN python3 -m virtualenv /opt/venv

RUN . /opt/venv/bin/activate && pip install virtualenv h2o-client

ENV VIRTUAL_ENV=/opt/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

COPY scripts/train.py /opt/scripts/train.py

CMD [ "python3", "/opt/scripts/train.py" ]