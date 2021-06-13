pipeline {
    agent { node { label 'master' } }

    stages {
        stage ('Build Docker Image') {
            steps {
                sh 'whoami'
                sh 'docker build -t web_calc_di:v1 .'
            }
        }
        stage ('Run Docker Image') {
            steps {
                sh 'docker run -it -p 80:80 web_calc_di:v1'
            }
        }
    }
}