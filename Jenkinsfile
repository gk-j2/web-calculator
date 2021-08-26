pipeline {
<<<<<<< HEAD
    agent { node { label 'webapp' } }
=======
    agent { node { label 'master' } }
>>>>>>> 286862ae8117da57ca7f5dec005847adb23e6892

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
<<<<<<< HEAD
}
=======
}
>>>>>>> 286862ae8117da57ca7f5dec005847adb23e6892
