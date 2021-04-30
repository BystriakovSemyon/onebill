FROM python:3.9-alpine3.12

WORKDIR /opt/app/

# Логин для git sbtatlas.sigma.sbrf.ru
ARG GIT_USER
# Пароль для git sbtatlas.sigma.sbrf.ru
ARG GIT_PASSWORD

ENV TZ 'UTC'
ENV PYTHONUNBUFFERED 1
ENV PIP_TRUSTED_HOST files.pythonhosted.org pypi.org pypi.python.org
ENV CRYPTOGRAPHY_DONT_BUILD_RUST 1

# Разбито на несколько этапов чтобы в разных сервисах это совпало
RUN apk upgrade \
    && apk add --no-cache libpq tzdata libffi g++ gcc libxslt-dev \
    && python3 -m venv /opt/venv \
    && /opt/venv/bin/pip install --no-cache-dir -U pip setuptools setuptools-scm

COPY requirements requirements

RUN cat /opt/app/requirements/apk.txt | xargs apk add --no-cache \
    && apk add --no-cache --virtual .base-build-deps postgresql-dev musl-dev git libffi-dev \
    && cat /opt/app/requirements/apk_build.txt | xargs apk add --no-cache --virtual .build-deps \
    && git config --global http.sslVerify false \
    && git config --global credential.helper '!f() { echo "username=${GIT_USER}"; echo "password=${GIT_PASSWORD}"; }; f' \
    && /opt/venv/bin/pip install --no-cache-dir -r requirements/python.txt \
    && rm -rf /opt/venv/src/*/.git \
    && rm -rf ~/.gitconfig \
    && apk del --no-cache .base-build-deps \
    && apk del --no-cache .build-deps

COPY . .

ENV APP_NAME 'onebill_menu_integrations'
EXPOSE 7999
ENV PYTHONPATH "${PYTHONPATH}:/opt/app/onebill_menu_integrations"

ENTRYPOINT  []
CMD ["/opt/venv/bin/python", "-m", "onebill_menu_integrations"]
