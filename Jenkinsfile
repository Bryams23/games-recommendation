pipeline {
 agent any

    stages {

        stage('Build') { 
             when {
                    branch 'main'
                        }
            steps { 
                
                echo 'building'
         
        }
        }

        stage('Test') {
            
            steps {
                echo "${env.BUILD_NUMBER}"
                sh '''. env/bin/activate
                python -m pytest.segundo_test.py
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