pipeline {
    agent any
    environment {
        PERSONA = "Homero Simpson"
    }
    parameters {
        string(name: 'OBJETO', defaultValue: 'jarrón', description: 'Nombre del objeto')
        booleanParam(name: 'PLAYA', defaultValue: true, description: 'es rica la playa?')
        choice(name: 'COLOR', choices: ['rojo', 'verde', 'azul'], description: 'Color del objeto')
    }
    stages {

        stage('Build') { 
            steps { 
                    echo 'Building...'
                    echo "la persona se llama ${env.PERSONA}"
        }
        }

        stage('Test') {
            
            steps {
                script {
                try {
                 sh '''
                    . venv/bin/activate
                    which python
                    python -m pytest
                '''
                echo "el nombe del objecto es ${params.OBJETO}, laplaya es buena si o no ${params.PLAYA}, el color del objeto es ${params.COLOR}"
                currentBuild.result = 'SUCCESS'
                }                            
                catch (Exception e) {
                    echo "Error: ${e}"
                    currentBuild.result = 'FAILURE'
                }
                
            }
            }
            
        }

        stage('Deploy') {

            when {
                allof {
                    branch 'main'
                }
            }

            steps {
                echo 'Deploying.. succesfully'
            }
        }

    post {

        success {
            echo 'I will only say this if successful'
        }
        failure {
            echo 'I will only say this if failed'
        }

    }
}
}