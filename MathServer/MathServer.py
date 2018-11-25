import socket

class Conversion:
    def __init__(self, capacity):
        self.top = -1
        self.capacity = capacity
        self.array = []
        self.output = []
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}

    def isEmpty(self):
        return True if self.top == -1 else False

    def peek(self):
        return self.array[-1]

    def pop(self):
        if not self.isEmpty():
            self.top -= 1
            return self.array.pop()
        else:
            return "$"

    def push(self, op):
        self.top += 1
        self.array.append(op)

    def isOperand(self, ch):
        return ch.isdigit()

    def notGreater(self, i):
        try:
            a = self.precedence[i]
            b = self.precedence[self.peek()]
            return True if a <= b else False
        except KeyError:
            return False

    def infixToPostfix(self, exp):
        last_char = exp[0]
        count = 0
        for i in exp:
            if self.isOperand(i):
                if (count > 0 and last_char.isdigit()):
                    temp = self.output.pop()
                    self.output.append(temp+i)
                else:
                    self.output.append(i)
            elif i == '(':
                self.push(i)
            elif i == ')':
                while ((not self.isEmpty()) and self.peek() != '('):
                    a = self.pop()
                    self.output.append(a)
                if (not self.isEmpty() and self.peek() != '('):
                    return -1
                else:
                    self.pop()
            else:
                while (not self.isEmpty() and self.notGreater(i)):
                    self.output.append(self.pop())
                self.push(i)
            last_char = i
            count += 1
        while not self.isEmpty():
            self.output.append(self.pop())
        #"".join(self.output)

    def evaluatePostfix(self,exp):
        self.infixToPostfix(exp)
        Stack = []
        for i in self.output:
            if i.isdigit():
                Stack.append(int(i))
            else:
                op2 = Stack.pop()
                op1 = Stack.pop()
                if (i == '+'):
                    Stack.append(op1 + op2)
                elif (i == '-'):
                    Stack.append(op1 - op2)
                elif (i == '*'):
                    Stack.append(op1 * op2)
                elif (i == '/'):
                    Stack.append(op1 / op2)
        return (Stack.pop())

s= socket.socket()
port = 12345
s.bind(('',port))
s.listen(5)

while True:
    c, addr = s.accept()
    print("Got Connected", addr)
    msg = "Enter the the expression to be evaluated"
    byte = msg.encode()
    c.send(byte)
    byte = c.recv(1024)
    expression = byte.decode()
    obj = Conversion(len(expression))
    result = obj.evaluatePostfix(expression)
    #print(expression)
    msg = str(result)
    byte = msg.encode()
    c.send(byte)
    c.close()