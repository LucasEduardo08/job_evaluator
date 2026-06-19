pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                echo 'Projeto clonado'
            }
        }

        stage('Instalar') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Testes') {
            steps {
                sh 'pytest'
            }
        }

    }
}