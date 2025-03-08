pipeline {
    agent any
    stages {
        stage('Build') { 
            steps {   
                echo 'going to build...'
                sh '. env/bin/activate'
                sh 'pip install pandas'
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