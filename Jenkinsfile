pipeline {
 agent any
 parameters {
    string(name: 'BRANCH_NAME', defaultValue: 'main', description: 'branch name')
}

    stages {

        stage('Build') { 
             when {
                    allOf {
                        expression {
                            params.BRANCH_NAME == 'main'
                        }
                        environment name: 'BUILD_NUMBER', value: '16'
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
                python -m pytest.segundo_test
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