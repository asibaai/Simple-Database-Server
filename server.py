'''
Written by: Arwa Alsibaai
'''

import socket # import the socket module

# create host and port variables to bind the server to
HOST = socket.gethostbyname(socket.gethostname())
PORT = 9999

def server_side():
    # create a socket object for the server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT)) # bind the socket to a host and a port to specify that the socket is a server
    server.listen(1) # let the server listen to requests from the client

    records = [] # initialize the list that will hold the records
    # read the records from the data.txt file
    with open("data.txt", "r") as file:
        for line in file: # for each line in the file
            if line.rstrip().split("|")[0]=="": # if the name isn't provided in the record, do not add it
                continue
            record = line.rstrip().split("|") # split a line into a record
            for i in range(4): # for each field in the record
                record[i] = record[i].strip() # remove any leading or trailing spaces
            records.append(tuple(record)) # add the record as a tuple to the list of records
    #print(records)

    communication, address = server.accept() # accept connection from a client
    print(f"Connected to {address}") # print the address of the client the server connected to
    client = True # check whether the client is connected

    while True:

        if not client: # if the client disconnected, the server accepts another client
            communication, address = server.accept() # accept connection from a client
            print(f"Connected to {address}") # print the address of the client the server connected to
            client = True
        
        request = communication.recv(1024).decode() # the server accepts a request from the client

        if request: # if the server receives a request
            data = request.split(',') # the request will contain multiple data in one request (seperated by a space)

            # if the client selects option 1
            if (data[0] == "1"):
                found = False # i want to keep track of whether the customer was found
                # iterate through the records to look for the customer
                for i in range(len(records)): 
                    if data[1] == records[i][0]: # if the customer name was found in the records, send a reponse of the customer record
                        response = f"{records[i][0]} | {records[i][1]} | {records[i][2]} | {records[i][3]}"
                        communication.send(response.encode()) # send the response to the client
                        found = True
                        break
                if not found: # if i do not find the customer, the server response will be "not found"
                    response = "not found"
                    communication.send(response.encode()) # send the response to the client

            # if the client selects option 2
            if (data[0] == "2"):
                found = False # i want to keep track of whether the customer exists
                # iterate through the records to see if the customer exists
                for i in range(len(records)): 
                    if data[1] == records[i][0]: # if the customer name was found in the records, send a reponse of the customer record
                        response = "exists"
                        communication.send(response.encode()) # send the response to the client
                        found = True
                        break
                if not found: # if the customer does not exist, they will be added
                    if data[1] == '':
                        response = "Customer must have a name"
                        communication.send(response.encode()) # send the response to the client
                    else: 
                        newrecord = data[1],data[2],data[3],data[4]
                        records.append(newrecord)
                        response = "Customer has been added"
                        communication.send(response.encode()) # send the response to the client

            # if the client selects option 3
            if (data[0] == "3"):
                found = False # i want to keep track of whether the customer exists
                # iterate through the records to look for the customer
                for i in range(len(records)): 
                    if data[1] == records[i][0]: # if the customer name was found in the records, delete the record
                        records.remove(records[i])
                        response = "Customer has been deleted"
                        communication.send(response.encode()) # send the response to the client
                        found = True
                        break
                if not found: # if i do not find the customer, they do not exist, so the server response will be "dne"
                    response = "dne"
                    communication.send(response.encode()) # send the response to the client

            # if the client selects option 4
            if (data[0] == "4"):
                found = False # i want to keep track of whether the customer was found
                # iterate through the records to look for the customer
                for i in range(len(records)): 
                    if data[1] == records[i][0]: # if the customer name was found in the records, change the age
                        records[i] = records[i][0],data[2],records[i][2],records[i][3] # create a new tuple with the new age
                        response = f"{data[1]}'s age has been updated"
                        communication.send(response.encode()) # send the response to the client
                        found = True
                        break
                if not found: # if i do not find the customer, the server response will be "not found"
                    response = "not found"
                    communication.send(response.encode()) # send the response to the client

            # if the client selects option 5
            if (data[0] == "5"):
                found = False # i want to keep track of whether the customer was found
                # iterate through the records to look for the customer
                for i in range(len(records)): 
                    if data[1] == records[i][0]: # if the customer name was found in the records, change the address
                        records[i] = records[i][0],records[i][1],data[2],records[i][3] # create a new tuple with the new address
                        response = f"{data[1]}'s address has been updated"
                        communication.send(response.encode()) # send the response to the client
                        found = True
                        break
                if not found: # if i do not find the customer, the server response will be "not found"
                    response = "not found"
                    communication.send(response.encode()) # send the response to the client

            # if the client selects option 6
            if (data[0] == "6"):
                found = False # i want to keep track of whether the customer was found
                # iterate through the records to look for the customer
                for i in range(len(records)): 
                    if data[1] == records[i][0]: # if the customer name was found in the records, change the phone number
                        records[i] = records[i][0],records[i][1],records[i][2],data[2] # create a new tuple with the new phone number
                        response = f"{data[1]}'s phone number has been updated"
                        communication.send(response.encode()) # send the response to the client
                        found = True
                        break
                if not found: # if i do not find the customer, the server response will be "not found"
                    response = "not found"
                    communication.send(response.encode()) # send the response to the client

            # if the client selects option 7
            if (data[0] == "7"):
                records.sort() # sort the records
                respnse = "\t** Python DB contents **" # create a new string for the response
                for record in records: # for each record
                    # concatenate string variable with new formatted customer record
                    respnse += f"\n\t{record[0]} | {record[1]} | {record[2]} | {record[3]}"
                communication.send(respnse.encode()) # send the response to the client

            # if the client selects option 8
            if (data[0] == "8"):
                client = False # the client disconnected
                response = "Goodbye!\n"
                communication.send(response.encode()) # send the response to the client
                communication.close() # close the communication socket
                print(f"Disconnected from {address}") # print that the client disconnected from the server

# run the server side program if this is the "main method"
if __name__ == "__main__":
    print(f"Starting server...")
    server_side()