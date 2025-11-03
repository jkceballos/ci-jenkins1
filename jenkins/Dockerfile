FROM jenkins/jenkins:lts

USER root

# Instala Docker dentro del contenedor
RUN apt-get update && apt-get install -y docker.io git

# Añade el usuario jenkins al grupo docker
RUN usermod -aG docker jenkins

USER jenkins
