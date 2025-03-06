pipeline {
    agent {
        docker {
            image 'node:14'        }
    }
    stages {
        stage('Build') {
            steps {
                echo 'node --version'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}