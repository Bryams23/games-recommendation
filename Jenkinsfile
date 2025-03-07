pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
               sh 'python3 -m venv env' 
               sh 'source env/bin/activate'
               sh 'pip install pytest'
            }
        }
        stage('Test') {
            steps {
                sh 'python -m pytest'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}