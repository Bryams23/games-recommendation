pipeline {
 agent any

    stages {

        stage('Build') { 
             when {
                        allOf {
                        env.BUILD_NUMBER == '1'
                        env.BRANCH_NAME == 'main'
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