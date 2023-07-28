FROM golang:alpine@sha256:6f592e0689192b7e477313264bb190024d654ef0a08fb1732af4f4b498a2e8ad
ENV CGO_ENABLED=0
ENV PYTHONUNBUFFERED=1
ENV FLAG="FLAG{TrY_H4rD3R_!!!}"

RUN apk add --update --no-cache build-base gcc python3 socat && ln -sf python3 /usr/bin/python && python3 -m ensurepip 
RUN pip3 install --no-cache --upgrade pip setuptools rich

WORKDIR /app
COPY src .
COPY FlagReader.c /FlagReader.c
RUN gcc /FlagReader.c -o /FlagReader && rm /FlagReader.c
RUN chmod 555 challenge.py && chmod +xs /FlagReader

RUN echo "CATF{FAKE_FLAG_FOR_TESTING}" > /root/flag.txt
RUN adduser -D meow && chown -R meow /app
USER meow

ENTRYPOINT ["python3","challenge.py"]
