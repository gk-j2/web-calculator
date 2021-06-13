pipeine {
    agent master

    stages {
        stage ('Cloning repository') {
            steps {
                mkdir /tmp/app
                cd /tmp/app
                git clone "git@github.com:gk-j2/web-calculator.git"
            }
        }
        stage ('Build Docker Image') {
            steps {
                echo "Start build docker image"
                docker build -t "web_calc_di:v1" .
                echo "End build docker image"
            }
        }
        stage ('Run Docker Image') {
            steps {
                echo "Start run docker image"
                docker run -it -p "80:80" "web_calc_di:v1"
            }
        }
    }
}