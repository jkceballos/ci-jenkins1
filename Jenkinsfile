pipeline {
    agent any

    environment {
        IMAGE_NAME = "demo-backend"
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/jkceballos/ci-jenkins1.git', branch: 'main'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build("${IMAGE_NAME}:${env.BUILD_NUMBER}", "backend/")
                }
            }
        }

        stage('Test') {
            steps {
                sh "docker run --rm ${IMAGE_NAME}:${env.BUILD_NUMBER} python -c \"import flask\""
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker compose down'
                sh 'docker compose up -d --build'
            }
        }
    }

    post {
        always {
            echo "Pipeline finalizado"
        }
    }
}
