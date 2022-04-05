# Jenkins

### Что такое Дженкинс?
Jenkins — это автономный сервер автоматизации с открытым исходным кодом, который можно использовать для автоматизации всех видов задач, связанных с созданием, тестированием, доставкой или развертыванием программного обеспечения.
Jenkins можно установить с помощью собственных системных пакетов, Docker или даже запустить отдельно на любом компьютере с установленной средой выполнения Java (JRE).

## Установка 

Установщики Jenkins доступны для нескольких дистрибутивов Linux.

* Debian/Ubuntu
* Fedora/RedHat/CentOS

**Минимальные аппаратные требования:**

* 256 МБ оперативной памяти
* 1 ГБ дискового пространства (хотя 10 ГБ — рекомендуемый минимум при запуске Jenkins в качестве контейнера Docker)

**Рекомендуемая конфигурация оборудования для небольшой команды:**

* 4 ГБ+ оперативной памяти
* 50 ГБ+ места на диске

**Необходимое ПО:**
* Java 8 или Java 11

### Установка Docker

```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
sudo apt update
sudo apt install docker-ce
sudo usermod -aG docker $USER
newgrp docker 
```

### Установка JAVA 11

```bash
sudo apt update
sudo apt install -y openjdk-11-jdk
```

### Установка Jenkins

```bash
curl -fsSL https://pkg.jenkins.io/debian/jenkins.io.key | sudo tee /usr/share/keyrings/jenkins-keyring.asc > /dev/null
echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] https://pkg.jenkins.io/debian binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list > /dev/null
sudo apt-get update
sudo apt-get install jenkins
```

После выполненных действий будет установлен Docker и Jenkins. Jenkins имеет веб-интерфейс, который запускается по умолчанию на порту 8080. Далее необходимо провести первоначальную конфигурацию администратора.

При первоначальном доступе необходимо разблокировать Jenkins строкой-паролем, которая хранится в файле */var/lib/jenkins/secrets/initialAdminPassword*.

Далее при установке потребуется выбрать устанавливать или нет плагины. Я рекомендую их установить,потому что большинство этих плагинов используется в каждом пайплайне.

После установки плагинов необходимо указать администратора для jenkins, введя логин, пароль, e-mail.

Далее в явном виде указываем URL,который будет использоваться для jenkins. Jenkins установлен. 

## Настройка доступа до репозитория по ssh

Сначала необходимо сгенерировать открытый и закрытый ключь с помощью команды:

```bash
ssh-keygen -C "<e-mail@mail.ru>"
```

Далее необходимо добавить открытый ключ, который хранится в файле *~/.ssh/id_rsa.pub* в SSH ключи доступа репозитория.

## Написание веб приложения

В качестве веб-приложения выберем простейшее API, которое реализует простейшие функции калькулятора. (https://github.com/gk-j2/web-calculator)

## Написание пайплайна

1. Перейтив пункт меню *New Item*
2. Выбрать "*Pipeline*" и ввести имя пайплайна
3. Отметить галочку "*GitHub project*" и внести URL репозитория проекта
4. В меню "*Build Triggers*" отметить галочку "*PollSCM*", которая указывает Дженкинсу проверять изменения в репозитории по расписанию
5. В расписании укажем "\* \* \* \* \*", что означает проверять каждую минуту

Далее необходимо указать сам пайплайн. Лучшими практиками является подход IaC - Infrastructure as a Code. Поэтому напишем пайлайн как код Groovy и сохраним его в этом же репозитории. Обычно пайплайны помещают в файлы Jenkinsfile, аналогично Dockerfile.

Сначала мы объявляем пайплайн. С помощью *agent* мы указываем какие агенты могут выполнять данный пайплайн. Jenkins имеет возможность подключать удаленных агентов, например в облаке,и обращаться к ним по меткам (lable).

Далее идет объявление этапов (stages) пайплайна. Один этам (stage) имеет название, и шаги (steps), которые выполняются в рамках данного этапа. Эти шаги являются командами Linux, которые мог бы выполнять программист для сборки и деплоя своего приложения.

В данном случае разбито на 3 этапа: удаление старого контейнера с приложением, сборка докер образа и запуск контейнера с приложением на основе этого докер образа.

```groovy
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
```

6. В меню "*Pipeline*" в выпадающем списке "*Defenition*" необходимо выбрать пункт "*Git*" откуда будет браться файл конфигурации, затем указать непосредственно URL Git, добавить учетные данные для доступа в этот репозиторий с конфигурацией, выбрать ветку и путь где хранится файл конфигурации.

Таким образом пайплайн настроен и можжно переходить к тестам.
