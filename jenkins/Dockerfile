FROM jenkins/jenkins:lts

USER root

# Instala Docker y Git
RUN apt-get update && apt-get install -y docker.io git

# Define el GID del host (ajusta 124 por el que obtuviste con getent group docker)
ARG DOCKER_GID=124

# Cambia el GID del grupo docker si ya existe
RUN groupmod -g ${DOCKER_GID} docker && \
    usermod -aG docker jenkins

USER jenkins
