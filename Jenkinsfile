pipeline {
    agent any
    stages {
        stage('Build') { 
            steps {   
                echo 'going to build...'
                sh 'pip list'
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