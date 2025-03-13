pipeline {
 agent any
    stages {

        stage('Build') { 
            steps { 
                echo 'building'
                sh '''. venv/bin/activate
                python -m pip install pytest            
                '''
                
                
        }
        }

        stage('Test') {
            
            steps {
                echo 'testing'
                sh '''. venv/bin/activate
                pytest
                '''
            }
            
        }

        stage('Deploy') {
            steps {
            echo 'deploying sdasdasf'

        }
}
    }
}