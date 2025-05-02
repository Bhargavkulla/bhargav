pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'bhargav/microservice-demo'
        DOCKER_TAG = 'latest'
        K8S_DEPLOYMENT_NAME = 'microservice-deployment'
        K8S_NAMESPACE = 'default'
    }
    stages {
        stage('Declarative: Checkout SCM') {
            steps {
                checkout scm
            }
        }
        
        stage('Install Dependencies') {
            steps {
                script {
                    sh 'python3 -m venv venv'
                    sh '. venv/bin/activate && pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Ensure PYTHONPATH includes the root of your project
                    sh '''
                    export PYTHONPATH=${PYTHONPATH}:/var/lib/jenkins/workspace/bhargav
                    pytest tests/test_app.py --maxfail=1 --disable-warnings -q
                    '''
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKER_IMAGE:$DOCKER_TAG .'
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    sh 'docker push $DOCKER_IMAGE:$DOCKER_TAG'
                }
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    sh '''
                    kubectl apply -f k8s/deployment.yaml
                    kubectl apply -f k8s/service.yaml
                    '''
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
