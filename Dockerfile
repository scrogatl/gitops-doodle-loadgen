FROM python:3.10-slim-bullseye
# Optional: trust an extra CA (for local builds behind TLS inspection). Pass it with
#   docker build --secret id=extra_ca,src=ca.pem ...
# Does nothing when the secret is absent, so CI builds are unaffected.
RUN --mount=type=secret,id=extra_ca \
    if [ -s /run/secrets/extra_ca ]; then \
      cp /run/secrets/extra_ca /usr/local/share/ca-certificates/extra-ca.crt && update-ca-certificates \
      && pip3 config --global set global.cert /etc/ssl/certs/ca-certificates.crt; \
    fi

WORKDIR /
COPY loadgen /loadgen
WORKDIR /loadgen

# setup app requirements
RUN pip3 install -r requirements.txt

CMD python3 app.py
