#!/usr/bin/python3
from typing_extensions import ParamSpecArgs
from flask import Flask, request
from werkzeug.exceptions import abort

appcalc = Flask(__name__)

def check_input_num(num):
    if not isinstance(num, (int, float)):
        return 0
    return 1

def check_operation(operation):
    allowed = ["+","-","*","/","//","%","**"]
    if operation not in allowed:
        return 0
    return 1

def calculate(file_json):
    check_a = check_input_num(file_json['a'])
    check_b = check_input_num(file_json['b'])
    check_oper = check_operation(file_json['operation'])
    if check_a and check_b and check_oper:
        a = file_json['a']
        b = file_json['b']
        operation = file_json['operation']
        if operation == "+":
            return a+b
        elif operation == "-":
            return a-b
        #elif operation == "*":
        #    return a*b
        elif operation == "**":
            if b >= 0:
                return a**int(b)
            else:
                return "Error! <b> be greater than or equal to zero!"   
        elif operation == "/":
            if b != 0:
                return a/b
            else:
                return "Error! Division by zero!"
        elif operation == "//":
            if b != 0:
                return a//b
            else:
                return "Error! Division by zero!"
        elif operation == "%":
            if b != 0:
                return a%b
            else:
                return "Error! Division by zero!"
    else:
        return ("Error! Input argument is not valide!")


@appcalc.route('/', methods=['POST'])
def send_answer():
    if not request.json or (not 'a' in request.json and not 'b' in request.json and not 'operation' in request.json):
        abort(404)
    result = calculate(request.json)
    answer = {'answer': result}
    return answer, 201

if __name__ == '__main__':
    appcalc.run(host='0.0.0.0', port='80')