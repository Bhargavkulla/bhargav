pipeline {
    agent any

    environment {
        VENV_PATH = 'venv'
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Remove any existing virtual environment
                    sh 'rm -rf venv'

                    // Create a new virtual environment
                    sh 'python3 -m venv venv'

                    // Activate the virtual environment
                    sh '. venv/bin/activate'

                    // Install dependencies from requirements.txt
                    sh 'pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Set PYTHONPATH and run the tests
                    sh 'export PYTHONPATH=$PYTHONPATH:/var/lib/jenkins/workspace/bhargav && pytest tests/test_app.py --maxfail=1 --disable-warnings -q'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build Docker image
                    sh 'docker build -t bhargavkulla/bhargav:latest .'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Push Docker image to Docker Hub
                    sh 'docker push bhargavkulla/bhargav:latest'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    // Deploy Docker image to Kubernetes
                    sh 'kubectl apply -f kubernetes/deployment.yaml'
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
