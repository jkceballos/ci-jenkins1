FROM jenkins/jenkins:lts

USER root

# Instala Docker y Git
RUN apt-get update && apt-get install -y docker.io git

# Crea el grupo docker con el mismo GID que el host
RUN groupadd -g 124 docker && usermod -aG docker jenkins

USER jenkins
