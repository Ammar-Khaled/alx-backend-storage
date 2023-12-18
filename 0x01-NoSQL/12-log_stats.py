#!/usr/bin/env python3
"""
This project module contains a Python script that provides
some stats about Nginx logs stored in MongoDB.
"""

if __name__ == '__main__':

    from pymongo import MongoClient

    connection_string = 'mongodb://127.0.0.1:27017/'

    client = MongoClient(connection_string)

    logs = client.logs

    nginx = logs.get_collection('nginx')

    x = nginx.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print(f"{x} logs")
    print('Methods:')
    for method in methods:
        print('\t{}: {}'.format(method, nginx.count_documents({"method": method})))
    print('{} status check'.format(nginx.count_documents({'method': 'GET', "path": "/status"})))
