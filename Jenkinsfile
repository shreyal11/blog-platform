pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/shreyal11/blog-platform.git'
            }
        }

        stage('Build Docker Containers') {
            steps {
                sh 'docker-compose up --build -d'
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
            echo 'Blog platform deployed successfully with Jenkins!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
