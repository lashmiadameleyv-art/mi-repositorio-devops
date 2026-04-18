pipeline {
    agent any

    stages {

        stage('Clonar Código') {
            steps {
                git branch: 'main',
                url: 'https://github.com/TUUSUARIO/mi-repositorio-devops.git'
            }
        }

        stage('Build Docker') {
            steps {
                sh 'sudo docker-compose down || true'
                sh 'sudo docker-compose up -d --build'
            }
        }

        stage('Verificar Contenedor') {
            steps {
                sh 'sudo docker ps'
            }
        }
    }
}
