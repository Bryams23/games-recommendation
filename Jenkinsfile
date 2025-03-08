pipeline {
    agent any
    stages {
        stage('Build') { 
            steps {   
                echo 'going to build...'
                sh 'rm -rf env'
                sh 'ls'
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