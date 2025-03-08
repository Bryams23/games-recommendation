pipeline {
    agent any
    stages {
        stage('Build') {
            steps {       
               sh 'ls'       
               sh '. env/bin/activate'
               when {
                    expression { env.VIRTUAL_ENV == 'null' }
                }
               echo "Es totalmente nulo"
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