'''
Written by: Arwa Alsibaai
'''

import socket # import the socket module

# use the same host and port as the server
HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

def client_side():
    # create a socket object for the client
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT)) # connect the client socket to a server

    while True:

        # print the menu
        print("\nPython DB Menu\n\n1. Find customer\n2. Add customer\n3. Delete customer\n4. Update customer age\n5. Update customer address\n6. Update customer phone\n7. Print report\n8. Exit\n")

        select = input("Select: ") # accept input from the user, which will be the option they select
        select = select.strip() # in case the customer entered a space with the number

        print()

        # if the client selects option 1
        if select == "1":
            name = input ("\tCustomer name: ") # prompt the user for a name
            # the request sent to the server will include the option number and the name
            request = f"1,{name}"
            client.send(request.encode()) # send the request to the server
            response = client.recv(1024).decode() # store the response received from the server
            if response == "not found": # if the server sends "not found"
                print(f"\tServer response: {name} not found in database")
            else: # if the customer is found, the server sends the record of the customer
                print(f"\tServer response: {response}")

        # if the client selects option 2
        elif select == "2":
            # prompt the user for the customer data
            name = input ("\tCustomer name: ")
            age = input ("\tCustomer age: ")
            address = input ("\tCustomer address: ")
            phone = input ("\tCustomer phone number: ")
            # remove any leading or trailing spaces from the data the user entered
            name = name.strip()
            age = age.strip()
            address = address.strip()
            phone = phone.strip()
            # the request sent to the server will include the option number and the customer data
            request = f"2,{name},{age},{address},{phone}"
            client.send(request.encode()) # send the request to the server
            response = client.recv(1024).decode() # store the response received from the server
            if response == "exists": # if the server sends "exists"
                print(f"\tServer response: Customer already exists")
            else: # if the customer is added, the server sends a confirmation message
                print(f"\tServer response: {response}")

        # if the client selects option 3
        elif select == "3":
            name = input ("\tCustomer name: ") # prompt the user for a name
            # the request sent to the server will include the option number and the name
            request = f"3,{name}"
            client.send(request.encode()) # send the request to the server
            response = client.recv(1024).decode() # store the response received from the server
            if response == "dne": # if the server sends "dne"
                print(f"\tServer response: Customer does not exist")
            else: # if the customer exists and is deleted, the server sends a confirmation message
                print(f"\tServer response: {response}")

        # if the client selects option 4
        elif select == "4":
            name = input ("\tCustomer name: ") # prompt the user for a name
            new = input ("\tNew age: ") # prompt the user for the new age
            new = new.strip() # remove any leading or trailing spaces
            # the request sent to the server will include the option number, the name, and the update
            request = f"4,{name},{new}"
            client.send(request.encode()) # send the request to the server
            response = client.recv(1024).decode() # store the response received from the server
            if response == "not found": # if the server sends "not found"
                print(f"\tServer response: Customer not found")
            else: # if the customer data has been updated, the server sends a confirmation message
                print(f"\tServer response: {response}")

        # if the client selects option 5
        elif select == "5":
            name = input ("\tCustomer name: ") # prompt the user for a name
            new = input ("\tNew address: ") # prompt the user for the new address
            new = new.strip() # remove any leading or trailing spaces
            # the request sent to the server will include the option number, the name, and the update
            request = f"5,{name},{new}"
            client.send(request.encode()) # send the request to the server
            response = client.recv(1024).decode() # store the response received from the server
            if response == "not found": # if the server sends "not found"
                print(f"\tServer response: Customer not found")
            else: # if the customer data has been updated, the server sends a confirmation message
                print(f"\tServer response: {response}")

        # if the client selects option 6
        elif select == "6":
            name = input ("\tCustomer name: ") # prompt the user for a name
            new = input ("\tNew phone number: ") # prompt the user for the new phone number
            new = new.strip() # remove any leading or trailing spaces
            # the request sent to the server will include the option number, the name, and the update
            request = f"6,{name},{new}"
            client.send(request.encode()) # send the request to the server
            response = client.recv(1024).decode() # store the response received from the server
            if response == "not found": # if the server sends "not found"
                print(f"\tServer response: Customer not found")
            else: # if the customer data has been updated, the server sends a confirmation message
                print(f"\tServer response: {response}")

        # if the client selects option 7
        elif select == "7":
            # the request sent to the server will include the option number
            request = f"7,"
            client.send(request.encode()) # send the request to the server
            response = client.recv(10240).decode() # store the response received from the server
            print(f"{response}") # print the server's response

        # if the client selects option 8
        elif select == "8":
            # the request sent to the server will include the option number
            request = f"8,"
            client.send(request.encode()) # send the request to the server
            response = client.recv(1024).decode() # store the response received from the server
            print(f"\t{response}") # print the server's response
            break

        else:
            print("\tThis is not an option on the menu!")


    client.close() # close the connection

# run the client side program if this is the "main method"
if __name__ == "__main__":
    client_side()