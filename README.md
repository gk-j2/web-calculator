<h1 align="center">web-calculator</h1>

<h3 align="center">Описание</h3>
web-calculator - микросервис, предоставляющий API для выполения простейших математических вычислений. Реализована поддержка операций сложения, вычитания, умножения, возведения в степень, деления, извлечения целой части деления и остатка от делелния.

<h3 align="center">Использование</h3>
web-calculator работает по протоколу HTTP и принимает запросы на 80 порту. web-calculator в качестве входных параметров ожидает json-файл вида:

```json
"a":number_1,
"b":number_2,
"operation":"allowed_operation"
```

Параметры number_1 и number_2 должны быть числами,"operation" - строка операции, которая разрешена в микросервисе.

Для использования можно использовать curl в следующем виде:
```bash
curl -i -H "Content-Type: application/json" -X POST -d '{"a":number_1,"b":number_2,"operation":"allowed_operation"}' "http://127.0.0.1"
```
В данном случае адрес назначения 127.0.0.1 может быть заменен на любой необходимый для вас.

В качестве ответа отправляется json-файл с ответом. Ответом может быть как число, так и строка с ошибкой.
```json
"answer":answer
```

web-calculator может использоваться локально на компьютере. Для этого необходимо установить необходимые зависимости, который находятся в файле src/requirements.txt, а затем запустить скрипт web_calc.py.

```bash
pip3 install --no-cache-dir -r requirements.txt
python3 web_calc.py
```

Реализована поддержка использования Docker. Для этого сначала необходимо запустить сборку образа Docker, а затем запустить этот образ. Важно, чтобы иерархия проекта была соблюдена.

```bash
docker build -t web_calc_di:v1 .'
docker run --name=application -d -p 80:80 web_calc_di:v1'
```

В дополнение реализована поддержка непрерывной интеграции с помощью Jenkins. Jenkins установлен локально. В нем реализован pipeline с несколькими ветвями. Ветка master развертывается на удаленном агенте Jenkins в облаке. Ветка develop развертывается на локальном мастере Jenkins.


<h3 align="center">Примеры использования</h3>

Запрос №1:

```bash
curl -i -H "Content-Type: application/json" -X POST -d '{"a":2,"b":3,"operation":"+"}' "http://127.0.0.1"
```

Ответ на запрос №1:

```http
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 13
Server: Werkzeug/2.0.1 Python/3.7.10
Date: Mon, 14 Jun 2021 03:53:16 GMT

{"answer":5}
```

Запрос №2:

```bash
curl -i -H "Content-Type: application/json" -X POST -d '{"a":2,"b":3,"operation":"log"}' "http://127.0.0.1"
```

Ответ на запрос №2:

```http
HTTP/1.0 201 CREATED
Content-Type: application/json
Content-Length: 50
Server: Werkzeug/2.0.1 Python/3.7.10
Date: Mon, 14 Jun 2021 04:03:44 GMT

{"answer":"Error! Input argument is not valide!"}
```
