pipeline {
    agent any
    stages {
        stage('Build') {
             when {
                    expression { env.VIRTUAL_ENV == 'null' }
                }
               echo "Es totalmente nulo"
            }   
            steps {    
               sh '. env/bin/activate'
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