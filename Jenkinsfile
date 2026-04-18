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
                sh 'cd $WORKSPACE && sudo docker-compose down || true'
                sh 'cd $WORKSPACE && sudo docker-compose up -d --build'
            }
        }

        stage('Verificar') {
            steps {
                sh 'sudo docker ps'
            }
        }
    }
}
