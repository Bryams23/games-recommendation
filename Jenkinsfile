pipeline {
    agent any
    stages {
        stage('Build') {
            when {
                expression { env.VIRTUAL_ENV == 'null' }
            }   
            steps {   
                echo 'totalmente nulo' 
                sh '. env/bin/activate'
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