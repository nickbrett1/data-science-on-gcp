# gsutil works only upto python 3.11
ARG VARIANT=
FROM mcr.microsoft.com/devcontainers/python:3.11

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
	&& apt-get -y install --no-install-recommends zsh-syntax-highlighting curl gnupg

ADD .zshrc /home/node
ADD .p10k.zsh /home/node

# Downloading gcloud package
RUN curl https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz > /tmp/google-cloud-sdk.tar.gz

# Installing the package
RUN mkdir -p /usr/local/gcloud \
	&& tar -C /usr/local/gcloud -xvf /tmp/google-cloud-sdk.tar.gz \
	&& /usr/local/gcloud/google-cloud-sdk/install.sh

# Adding the package path to local
ENV PATH $PATH:/usr/local/gcloud/google-cloud-sdk/bin
