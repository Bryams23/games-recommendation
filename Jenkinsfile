pipeline {
    agent any
    stages {
        stage('Build') {
            steps {             
               sh '. env/bin/activate'
               echo '$VIRTUAL_ENV'
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