pipeline {
    agent any
    stages {
        stage('Build') { 
            steps { 
                    echo 'Building...'
                    sh 'ls'
        }
        }
        stage('Test') {
            steps {
                sh '''
                    . venv/bin/activate
                    pip list
                    which python
                    python -m pytest
                '''
                
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}