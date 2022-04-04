pipeline {
    agent any

    stages {
        stage ('Stop and delete running docker container') {
            steps {
                sh 'docker ps -f name=application -q | xargs --no-run-if-empty docker container stop'
                sh 'docker container ls -a -fname=application -q | xargs -r docker container rm'
            }
        }
        stage ('Build Docker Image') {
            steps {
                sh 'docker build -t web_calc_di:v1 .'
            }
        }
        stage ('Run Docker Image') {
            steps {
                sh 'docker ps'
                sh 'docker run --name=application -d -p 80:80 web_calc_di:v1'
            }
        }
    }
}
