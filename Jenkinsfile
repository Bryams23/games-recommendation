pipeline {
 agent any

    stages {

        stage('Build') { 
            BUILD_NUMBER = sh(script: 'echo $BUILD_NUMBER', returnStdout: true).trim()
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