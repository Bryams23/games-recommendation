pipeline {
    agent any
    stages {
        stage('Build') { 
            steps { 
                sh '''
                    echo 'Building...'
                    . venv/bin/activate
                    pip install pytest
                    pip install python3.3
                '''  

        }
        }
        stage('Test') {
            steps {
                sh 'python -m pytest'
                
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying...'
            }
        }
    }
}