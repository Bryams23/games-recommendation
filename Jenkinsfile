pipeline {
 agent any

    stages {

        stage('Build') { 
             when {
                        allOf {
                        build '12'
                        branch 'main'
                }
                        }
            steps { 
                
                echo 'building'
         
        }
        }

        stage('Test') {
            
            steps {
                echo 'testing'
                sh '''. env/bin/activate
                python -m pytest 
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