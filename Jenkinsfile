pipeline {
    agent { node { label 'webapp' } }

    stages {
        stage ('Stop and delete running docker container') {
            sh 'docker ps -f name=zookeeper -q | xargs --no-run-if-empty docker container stop'
            sh 'docker container ls -a -fname=zookeeper -q | xargs -r docker container rm'
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
