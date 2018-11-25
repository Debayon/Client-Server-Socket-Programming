import socket
import threading
import datetime

class Customers:
    no_of_customers = 0
    def __init__(self,product_bought,qty,addr,port):
        self.product_bought = product_bought
        self.qty = qty
        self.cli_addr = addr
        self.cli_port = port
        self.time = self.time_stamper()
        self.Increment_Customers()
        self.customer_no = Customers.no_of_customers

    def Print_Client(self):
        print("*****Customer%d*****" %self.customer_no)
        print(self.product_bought)
        print(self.qty)
        print(self.cli_addr)
        print(self.cli_port)
        print(self.time)
    def Increment_Customers(self):
        Customers.no_of_customers += 1
    def time_stamper(self):
        return str(datetime.datetime.now().strftime("%A, %d. %B %Y %I:%M%p"))

def Thread_Handler(c, addr, item_list, customer_list):  # item
    bought = 1

    msg = "Thank You for connecting"
    byte = msg.encode()
    c.send(byte)
    print(item_list)
    byte = c.recv(1024)
    message = byte.decode()
    item = message[0]
    quantity = int(message[1:])
    print(item)
    lock.acquire()  #lcoking for synchronization
    print(quantity)
    # item_list["mango"] = item_list["mango"] - quantity
    if (item == 'm'):
        sav = item_list["mango"]
        item_list["mango"] = item_list["mango"] - quantity
        if (item_list["mango"] < 0):
            item_list["mango"] = sav
            print("Requested quantity of mango is not available")
            bought = -1
        if (bought > 0):
            customer = Customers("Mango", quantity,addr[0],addr[1])
            customer_list.append(customer)
    if (item == 'o'):
        sav = item_list["orange"]
        item_list["orange"] = item_list["orange"] - quantity
        if (item_list["orange"] < 0):
            item_list["orange"] = sav
            print("Requested quantity of orange is not available")
            bought = -1
        if (bought > 0):

            customer = Customers("Orange", quantity,addr[0],addr[1])
            customer_list.append(customer)
    if (item == 'g'):
        sav = item_list["guava"]
        item_list["guava"] = item_list["guava"] - quantity
        if (item_list["guava"] < 0):
            item_list["guava"] = sav
            print("Requested quantity of guava is not available")
            bought = -1
        if (bought > 0):
            customer = Customers("Guava", quantity,addr[0],addr[1])
            customer_list.append(customer)
    if (item == 'p'):
        sav = item_list["petrol"]
        item_list["petrol"] = item_list["petrol"] - quantity
        if (item_list["petrol"] < 0):
            item_list["petrol"] = sav
            print("Requested quantity of petrol is not available")
            bought = -1
        if (bought > 0):
            customer = Customers("Petrol", quantity,addr[0],addr[1])
            customer_list.append(customer)
    input()
    lock.release()

    print("Available Items")
    print("Product\tQuantity")
    print("Mango\t%d" % item_list["mango"])
    print("Orange\t%d" % item_list["orange"])
    print("Guava\t%d" % item_list["guava"])
    print("Petrol\t%d" % item_list["petrol"])
    print("\n")
    for i in customer_list:
        i.Print_Client()
    c.close()


# variables
item_list = {'mango':30,'orange':30,'guava':30,'petrol':30}
mango = 30
orange=30
guava=30
petrol=30
sav=0
bought=1
customer_list = []
thread_list = []
# variables





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

lock = threading.Lock()

while True:
    c, addr = s.accept()
    print("Got Connected", addr)
    t = threading.Thread(target=Thread_Handler,args=(c,addr,item_list,customer_list))  #item_list
    t.start()
    #(client_IP,client_port) = s.getsockname()
    #print("****CLIENT IP and Port")
    #print(client_IP)
    #print(client_port)
    #print("****CLIENT IP and Port")
