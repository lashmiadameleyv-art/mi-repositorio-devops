pipeline {
    agent any

    stages {

        stage('Actualizar Código') {
            steps {
                checkout scm
            }
        }

        stage('Rebuild y Deploy') {
            steps {
                sh 'cd $WORKSPACE && docker-compose down || true'
                sh 'cd $WORKSPACE && docker-compose up -d --build'
            }
        }

        stage('Verificar') {
            steps {
                sh 'docker ps'
            }
        }
    }
}
