pipeline {
    agent { node { label 'webapp' } }

    stages {
        stage ('Stop and delete running docker container') {
            script {
                if (docker ps -q) {
                    sh 'docker kill $(docker ps -q)'
                    sh 'docker rm $(docker ps -a -q)'
                }
            }
        }
        stage ('Build Docker Image') {
            steps {
                sh 'docker build -t web_calc_di:v1 .'
            }
        }
        stage ('Run Docker Image') {
            steps {
                sh 'docker run -d -p 80:80 web_calc_di:v1'
            }
        }
    }
}
