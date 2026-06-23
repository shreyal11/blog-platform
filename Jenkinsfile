pipeline {
    agent any

    stages {
        stage('Show Workspace Files') {
            steps {
                sh 'pwd'
                sh 'ls -R'
            }
        }

        stage('Restart Existing Blog Containers') {
            steps {
                sh 'docker stop blog-flask blog-mysql || true'
                sh 'docker start blog-mysql blog-flask'
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
            echo 'Blog platform containers restarted successfully with Jenkins!'
        }
        failure {
            echo 'Pipeline failed. Check console output.'
        }
    }
}
