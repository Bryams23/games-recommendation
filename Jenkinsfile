pipeline {
    agent any
    stages {
        stage('Build') {
            steps {             
               sh '. env/bin/activate'
               sh 'pip list'
            }
        }
        stage('Test') {
            steps {
                //sh 'python -m pytest'
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