pipeline {
    agent any

    stages {
        stage("Code clone") {
            steps {
                echo "this is cloning the code"
                git url: "https://github.com/shreyal11/blog-platform.git", branch: "main"
                echo "code clone successfully"
            }
        }

        stage("build") {
            steps {
                echo "this is building the code"
                sh "docker build -t blog-flask:latest ./backend"
                echo "successfully building"
            }
        }

        stage("push dockerhub") {
            steps {
                echo "This is pushing to Docker Hub"
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhubcred',
                    passwordVariable: 'dockerhubPass',
                    usernameVariable: 'dockerhubUser'
                )]) {
                    sh "echo ${dockerhubPass} | docker login -u ${dockerhubUser} --password-stdin"
                    sh "docker image tag blog-flask:latest ${dockerhubUser}/blog-flask:latest"
                    sh "docker push ${dockerhubUser}/blog-flask:latest"
                }
            }
        }

        stage("Deploy") {
            steps {
                echo "Deploying the code"
                sh "docker compose up -d"
            }
        }
    }
}
