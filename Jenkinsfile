pipeline {
    agent any
    stages {
        stage('Build') { 
            steps {   
                echo 'going to build...'
                sh '. venv/bin/activate'
                sh 'pip3 install pytest'
                sh 'pip3 list'
        }
        }
        stage('Test') {
            steps {
                sh 'python3 -m pytest'
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