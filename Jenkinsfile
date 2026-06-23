pipeline {
    agent any

    stages {
        stage('Build Blog App Image') {
            steps {
                sh 'docker build -t blog-platform-app ./backend'
            }
        }

        stage('Remove Old Container') {
            steps {
                sh 'docker rm -f blog-app || true'
            }
        }

        stage('Run Blog App Container') {
            steps {
                sh 'docker run -d --name blog-app -p 5000:5000 blog-platform-app'
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
            echo 'Blog app deployed successfully with Jenkins!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}
