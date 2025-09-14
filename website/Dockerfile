# Stage 1: Build the static HTML / CSS / JS bundle
#          This stage is responsible for using Jekyll to build the static
#          files that are ultimately served by nginx. This is not the final
#          image.
FROM ruby:3.2.2 AS build-image
ENV NODE_VERSION=18.17.1
ENV NVM_DIR=/root/.nvm
ENV PATH="/root/.nvm/versions/node/v${NODE_VERSION}/bin/:${PATH}"
ARG http_proxy
ARG https_proxy
ARG no_proxy

ENV http_proxy=$http_proxy \
    https_proxy=$https_proxy \
    no_proxy=$no_proxy \
    HTTP_PROXY=$http_proxy \
    HTTPS_PROXY=$https_proxy \
    NO_PROXY=$no_proxy

WORKDIR /app
COPY ./Gemfile /app/Gemfile
COPY ./package.json /app/package.json
## If you have corporate root CA certificates, place them in website/certs/
## Copy the entire directory so build doesn't fail when there are no *.crt files
COPY certs/ /usr/local/share/ca-certificates/
ENV SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt \
    CURL_CA_BUNDLE=/etc/ssl/certs/ca-certificates.crt \
    BUNDLE_SSL_CA_CERT=/etc/ssl/certs/ca-certificates.crt \
    SSL_CERT_DIR=/etc/ssl/certs
RUN apt-get clean && \
    apt-get update && \
    apt-get install -y curl git ca-certificates nodejs npm && \
    update-ca-certificates && \
    git config --global http.sslCAInfo /etc/ssl/certs/ca-certificates.crt && \
    npm config set cafile /etc/ssl/certs/ca-certificates.crt && \
    npm install --legacy-peer-deps chart.js && \
    bundle config set ssl_ca_cert /etc/ssl/certs/ca-certificates.crt && \
    bundle config set ssl_verify_mode 0 && \
    bundle install

COPY . /app
RUN bundle exec jekyll build && \
    npx gulp updateUswds


# Stage 2: Build the final nginx image
#          This stage is responsible for building the final nginx image that
#          contains the static files generated in Stage 1.
FROM nginxinc/nginx-unprivileged:alpine AS runtime-image
ARG http_proxy
ARG https_proxy
ARG no_proxy

ENV http_proxy=$http_proxy \
    https_proxy=$https_proxy \
    no_proxy=$no_proxy \
    HTTP_PROXY=$http_proxy \
    HTTPS_PROXY=$https_proxy \
    NO_PROXY=$no_proxy

COPY nginx.conf /etc/nginx/nginx.conf
COPY --from=0 /app/_site /usr/share/nginx/html
EXPOSE 8080