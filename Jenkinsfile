pipeline {
    agent any

    stages {
        stage('Show Workspace Files') {
            steps {
                sh 'pwd'
                sh 'ls -R'
            }
        }

        stage('Restart Blog Platform') {
            steps {
                sh 'docker compose down || true'
                sh 'docker compose up --build -d'
            }
        }

        stage('Check Running Containers') {
            steps {
                sh 'docker ps'
            }
        }
    }

    post {
        success {
            echo 'Blog platform restarted successfully with Jenkins!'
        }
        failure {
            echo 'Pipeline failed. Check console output.'
        }
    }
}
