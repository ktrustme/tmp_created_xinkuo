from django.shortcuts import render

# Create your views here.

error_msgs = {'malform':'Malformed HTTP request', 'divbyzero':'Divided By Zero!',\
    'unknown': 'Unknown Exception'}

def initialize(request):
    context = {} 
    context['displayed_num'] = 0
    context['last_pressed'] = '0' 
    context['last_op'] = '+' 
    context['last_num'] = '0' 
    return render(request, 'calculator/calculator.html',context)


def calculate(request):
    context = {} 
    context['displayed_num'] = 0
    context['last_pressed'] = '0' 

    #input validation.
    try:
        displayed_num = request.GET['displayed_num'] 
        last_op = request.GET['last_op']
        last_num= request.GET['last_num']
        last_pressed = request.GET['last_pressed']
    except Exception:
        displayed_num = '0' 
        last_op = '+' 
        last_num= '0' 
        last_pressed = '0' 
        context['displayed_num'] = error_msgs['malform'] 
        context['last_op'] = last_op
        context['last_num'] = last_num
        context['last_pressed'] = last_pressed
        return render(request, 'calculator/calculator.html',context)


    try:
        if displayed_num in error_msgs.values():
            displayed_num = 0;
            last_op = '+' 
            last_num= '0' 
            last_pressed = '0' 

        try:
            #pressed buton is a num
            input_num = request.GET['num_button']
            if is_op((last_pressed)):
                displayed_num = int(input_num)
                last_pressed = input_num
            else:
                displayed_num = int(displayed_num) * 10 + int(input_num)
                last_pressed = input_num
                
        except KeyError:
            input_op = request.GET['op_button']
            #pressed button is an op 
            if input_op =='C':
                displayed_num = '0' 
                last_op = '+' 
                last_num= '0' 
                last_pressed = '0' 
                print('ha')
            elif is_op(request.GET['last_pressed']):
                #if last pressed button is a op, error
                last_pressed = input_op
                last_op = input_op
            else:
                #if last pressed button is a num, go ahead 
                #calculate the expression
                last_num = request.GET['last_num']
                last_op = request.GET['last_op']

                calculate_result= calculate_exp(last_num, last_op, displayed_num)
                if input_op == '=':
                    displayed_num = calculate_result
                    last_op = input_op
                    last_pressed = '=' 
                    last_num = calculate_result 
                else:
                    displayed_num = calculate_result
                    last_op = input_op
                    last_pressed = input_op
                    last_num = calculate_result 
        except Exception:
            pass
    except ZeroDivisionError:
        displayed_num = error_msgs['divbyzero']
        print("HA 0")
    except Exception:
        displayed_num = error_msgs['unknown']

    context['displayed_num'] = displayed_num
    context['last_op'] = last_op
    context['last_num'] = last_num
    context['last_pressed'] = last_pressed
    
    return render(request, 'calculator/calculator.html',context)
    
def is_num(c):
    if ord(c) in xrange(ord('0'), ord('9')+1): 
        return True
    return False
    
def is_op(c):
    if c == '*' or c == '+' or c == '-' or c == '/' or c == 'C' or c == '=':
        return True;
    return False

def calculate_exp(num1, op, num2):
    options = {'+': plus, '-': minus, '*': multi, '/': divide,'=':asign}
    if(op in options):
        return options[op](int(num1), int(num2))
    else:
        raise Exception('Unknown exception when evaluating')

def plus(num1, num2):
    return num1 + num2

def multi(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def minus(num1, num2):
    return num1 - num2

def asign(num1, num2):
    return num2;

