pipeline {
 agent any

    stages {

        stage('Build') { 

            steps { 
                
                echo 'building'
                allOf {
                    when {
                        env.BUILD_NUMBER == '1'
                        env.BRANCH_NAME == 'main'
                        }
                }
           

         
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