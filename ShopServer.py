import socket
#import threading

class Customers:
    no_of_customers = 0
    def __init__(self,product_bought,qty):
        self.product_bought = product_bought
        self.qty = qty
        self.cli_addr = "default"
        self.cli_port = "default"
        self.time = "default"
        self.Increment_Customers()
        self.customer_no = Customers.no_of_customers

    def Print_Client(self):
        print("*****Customer%d*****" %self.customer_no)
        print(self.product_bought)
        print(self.qty)
        #print(self.cli_addr)
    def Increment_Customers(self):
        Customers.no_of_customers += 1


# variables
item_list = {'mango':30,'orange':30,'guava':30,'petrol':30}
mango = 30
orange=30
guava=30
petrol=30
sav=0
bought=1
object_list = []
thread_list = []
# variables



#def Thread_Handler(c,addr,lock,items):




s= socket.socket()
#host = socket.gethostbyname()
port = 12345
s.bind(('',port))

s.listen(5)


print("Available Items")
print("Product\tQuantity")
print("Mango\t%d" % mango)
print("Orange\t%d" % orange)
print("Guava\t%d" % guava)
print("Petrol\t%d" % petrol)

while True:
    c, addr = s.accept()
    print("Got Connected", addr)
    #lock = threading.Lock()
    #t = threading.Thread(target=Thread_Handler,args=(c,addr,lock,item_list))
    #t.start()
    #(client_IP,client_port) = s.getsockname()
    #print("****CLIENT IP and Port")
    #print(client_IP)
    #print(client_port)
    #print("****CLIENT IP and Port")
    bought = 1

    msg = "Thank You for connecting"
    byte = msg.encode()
    c.send(byte)
    byte = c.recv(1024)
    message = byte.decode()
    item = message[0]
    quantity = int(message[1:])
    print(item)
    print(quantity)
    if (item == 'm'):
        sav = mango
        mango = mango - quantity
        if (mango < 0):
            mango = sav
            print("Requested quantity of mango is not available")
            bought = -1
        if (bought > 0):
            customer = Customers("Mango", quantity)
            object_list.append(customer)
    if (item == 'o'):
        sav = orange
        orange = orange - quantity
        if (orange < 0):
            orange = sav
            print("Requested quantity of orange is not available")
            bought = -1
        if (bought > 0):
            customer = Customers("Orange", quantity)
            object_list.append(customer)
    if (item == 'g'):
        sav = guava
        guava = guava - quantity
        if (guava < 0):
            guava = sav
            print("Requested quantity of guava is not available")
            bought = -1
        if (bought > 0):
            customer = Customers("Guava", quantity)
            object_list.append(customer)
    if (item == 'p'):
        sav = petrol
        petrol = petrol - quantity
        if (petrol < 0):
            petrol = sav
            print("Requested quantity of petrol is not available")
            bought = -1
        if (bought > 0):
            customer = Customers("Petrol", quantity)
            object_list.append(customer)
    print("Available Items")
    print("Product\tQuantity")
    print("Mango\t%d" % mango)
    print("Orange\t%d" % orange)
    print("Guava\t%d" % guava)
    print("Petrol\t%d" % petrol)
    print("\n")
    for i in object_list:
        i.Print_Client()

    c.close()