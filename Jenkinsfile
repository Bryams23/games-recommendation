pipeline {
 agent any
 parameters {
    string(name: 'BRANCH_NAME', defaultValue: 'main', description: 'branch name')
}

    stages {

        stage('Build') { 
             when {
                    anyOf {
                        expression {
                            params.BRANCH_NAME == 'master'
                        }
                        environment name: 'BUILD_NUMBER', value: '23'
                    }
                        }
            steps { 
                
                echo 'building'
         
        }
        }

        stage('Test') {
            
            steps {
                echo "${env.BUILD_NUMBER}"
                sh '''. env/bin/activate
                python -m pytest tests/segundo_test.py
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