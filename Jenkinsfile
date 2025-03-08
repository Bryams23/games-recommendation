pipeline {
    agent any
    stages {
        stage('Build') { 
            steps {   
                echo 'going to build...'
                sh 'rm -rf env'
                sh 'python3 -m venv env'
                sh 'source env/bin/activate'
                sh 'pip install pytest'
        }
        }
        stage('Test') {
            steps {
                sh 'python -m pytest'
                echo 'testing...tt'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}