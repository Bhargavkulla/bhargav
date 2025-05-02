pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'bhargavakulla/java-microservice'
        DOCKER_REGISTRY = 'docker.io'
        KUBERNETES_NAMESPACE = 'default'
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from GitHub
                git branch: 'main', url: 'https://github.com/Bhargavkulla/bhargav.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Create a Python virtual environment
                    sh 'python3 -m venv venv'

                    // Activate the virtual environment
                    sh '. venv/bin/activate'

                    // Install dependencies
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Set PYTHONPATH to the current working directory (where app is located)
                    sh 'export PYTHONPATH=$PYTHONPATH:$(pwd) && pytest tests/test_app.py --maxfail=1 --disable-warnings -q'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t $DOCKER_REGISTRY/$DOCKER_IMAGE .'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Login to Docker Hub
                    withDockerRegistry([credentialsId: 'docker-hub-credentials']) {
                        sh 'docker push $DOCKER_REGISTRY/$DOCKER_IMAGE'
                    }
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Apply Kubernetes manifests
                    sh 'kubectl apply -f k8s/deployment.yaml'
                    sh 'kubectl apply -f k8s/service.yaml'
                }
            }
        }
    }
}
