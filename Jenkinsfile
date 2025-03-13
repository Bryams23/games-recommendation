pipeline {
 agent any

    stages {

        stage('Build') { 
             when {
                        allOf {
                        expression{env.BUILD_NUMBER == '11'}
                        expression{env.BRANCH_NAME == 'main'}
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