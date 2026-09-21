# Simple-Database-Server
A client/server application that performs one-to-one communication. The server loads a database and listens for client requests to manipulate the database.


The server application loads the database from a plain text disk file called data.txt which holds customer records. It then listens for requests from the client application. When the client application starts, it provides a user interface consisting of a menu of requests. These are simple commands that find, add, delete, and update customers. There is also an option to print a a report of all customers and to exit. The server runs in an infinite loop so the client can simply connect again after exiting.

There is a data.txt file to test the application.
Note that the test file is not neat and includes things such as leading and trailing spaces and missing values in some fields. This is for error-checking purposes. Additional spaces are skipped, and entries without a name are also skipped, as can be seen when running the program.

To the run the application, you will need two separate terminals. 

First, on one terminal, run the following command: python server.py (or python3 server.py)

On the other terminal, run the following command: python client.py (or python3 client.py)

Note that the server does not support concurrency nor thread control and thus it can only communicate with one client at a time.
