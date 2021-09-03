#!/usr/bin/python3
from typing_extensions import ParamSpecArgs
from flask import Flask, request
from werkzeug.exceptions import abort

appcalc = Flask(__name__)

def is_num(param1, param2) -> bool:
    if isinstance(param1, (int, float)) and isinstance(param2, (int, float)):
        return True
    else:
        return False

def is_oper(operation) -> bool:
    allowed = ["+","-","*","/","//","%","**"]
    if operation in allowed:
        return True
    else:
        return False

def is_good_input(param1, param2, param3) -> bool:
    if is_num(param1, param2) and is_oper(param3):
        return True
    else:
        return False

class Calculator(object):
    def __init__(self, num1, num2, oper):
        self.num1 = num1
        self.num2 = num2
        self.oper = oper

    def calculate(self):
        if self.oper == "+":
            return self.num1 + self.num2

        elif self.oper == "-":
            return self.num1 - self.num2

        elif self.oper == "*":
            return self.num1 * self.num2

        elif self.oper == "**":
            if self.num2 >= 0:
                return self.num1 ** int(self.num2)
            else:
                return "Error! <b> must be greater than or equal to zero!" 

        elif self.oper == "/":
            if self.num2 != 0:
                return self.num1 / self.num2
            else:
                return "Error! Division by zero!"

        elif self.oper == "//":
            if self.num2 != 0:
                return self.num1 // self.num2
            else:
                return "Error! Division by zero!"

        elif self.oper == "%":
            if self.num2 != 0:
                return self.num1 % self.num2
            else:
                return "Error! Division by zero!"

@appcalc.route('/calc/api/v1/calculate', methods=['POST'])
def send_answer():
    if not request.json or (not 'a' in request.json and not 'b' in request.json and not 'operation' in request.json):
        abort(400)
    param1 = request.json['a']
    param2 = request.json['b']
    param3 = request.json['operation']
    if is_good_input(param1, param2, param3):
        calc = Calculator(param1, param2, param3)
        result = calc.calculate()
        answer = {'answer': result}
        return answer, 201
    else:
        mes = {'answer': "Error! Input argument is not valide!"}
        return mes, 201

@appcalc.route('/calc/api/v1/signup', methods=['POST'])
class User(object):
    def __init__(self, name, email, login, password):
        self.name = name
        self.login = login
        self.email = email
        self.passw = password
        
def is_not_valid(json):
    if (not 'name' in request.json or not 'email' in request.json or not 'login' in request.json or not 'password' in request.json):
        return(True)
    else:
        if (not '@' in 'email'):
            return(True) 
        else:
            return(False)

def sign_up():
    if (not request.json or is_not_valid(request.json)):
        abort(400)
    params = []
    params.append(request.json['name'])
    params.append(request.json['login'])
    params.append(request.json['email'])
    params.append(request.json['password'])
    mr_chel = User(name = params[0], login = params[1], email = params[2], password = params[3])

if __name__ == '__main__':
    appcalc.run(host='0.0.0.0', port='80')