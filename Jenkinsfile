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
                echo "${build}"
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