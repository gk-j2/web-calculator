pipeline {
    agent { node { label 'master' } }

    stages {
        stage ('Cloning repository') {
            steps {
                sh "ssh-agent bash -c 'ssh-add /somewhere/yourkey; git clone git@github.com:gk-j2/web-calculator.git'"
            }
        }
        stage ('Build Docker Image') {
            steps {
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