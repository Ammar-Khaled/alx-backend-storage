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

    methods = {'GET': 0, "POST": 0, "PUT": 0, "PATCH": 0, "DELETE": 0}

    status_number = 0
    for doc in nginx.find({'method': {'$in':
                          ["GET", "POST", "PUT", "PATCH", "DELETE"]}}):
        methods[doc['method']] += 1
        if (doc['method'] == 'GET' and doc['path'] == '/status'):
            status_number += 1

    print(f"{x} logs")
    print('Methods:')
    for k, v in methods.items():
        print(f"    method {k}: {v}")
    print(f'{status_number} status check')
