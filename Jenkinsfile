pipeline {
    agent any

    stages {
        stage("Code clone") {
            steps {
                echo "Cloning the code"
                git url: "https://github.com/shreyal11/blog-platform.git", branch: "main"
                echo "Code cloned successfully"
            }
        }

        stage("Build Docker Image") {
            steps {
                echo "Building Docker image"
                sh "docker build -t blog-flask:latest ./backend"
                echo "Docker image built successfully"
            }
        }

        stage("Push to Docker Hub") {
            steps {
                echo "Pushing image to Docker Hub"
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhubcred',
                    usernameVariable: 'DOCKERHUB_USER',
                    passwordVariable: 'DOCKERHUB_PASS'
                )]) {
                    sh '''
                        echo "$DOCKERHUB_PASS" | docker login -u "$DOCKERHUB_USER" --password-stdin
                        docker tag blog-flask:latest "$DOCKERHUB_USER"/blog-flask:latest
                        docker push "$DOCKERHUB_USER"/blog-flask:latest
                    '''
                }
            }
        }

        stage("Remove Old Container") {
            steps {
                echo "Removing old blog container if it exists"
                sh "docker rm -f blog-flask || true"
            }
        }

        stage("Run New Container") {
            steps {
                echo "Running new blog container"
                sh "docker run -d --name blog-flask -p 5000:5000 blog-flask:latest"
            }
        }

        stage("Check Running Containers") {
            steps {
                echo "Checking running containers"
                sh "docker ps"
            }
        }
    }

    post {
        success {
            echo "Pipeline executed successfully!"
        }
        failure {
            echo "Pipeline failed. Check console output."
        }
    }
}
