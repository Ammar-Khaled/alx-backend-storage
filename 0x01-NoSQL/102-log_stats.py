#!/usr/bin/env python3
"""
Improve 12-log_stats.py by adding the top 10 of the most present IPs
in the collection nginx of the database logs:
  The IPs top must be sorted (like in the README example)
"""
if __name__ == '__main__':

    from pymongo import MongoClient

    connection_string = 'mongodb://127.0.0.1:27017/'

    client = MongoClient(connection_string)

    logs = client.logs

    nginx = logs.get_collection('nginx')

    x = nginx.count_documents({})

    methods = {'GET': 0, "POST": 0, "PUT": 0, "PATCH": 0, "DELETE": 0}
    ips = dict()
    status_number = 0
    for doc in nginx.find({'method':
                          {'$in': ["GET", "POST", "PUT", "PATCH", "DELETE"]}}):
        methods[doc['method']] += 1
        if (doc['method'] == 'GET' and doc['path'] == '/status'):
            status_number += 1

    for doc in nginx.find({}):
        if doc['ip'] in ips.keys():
            ips[doc['ip']] += 1
        else:
            ips[doc['ip']] = 1

    ips = dict(sorted(ips.items(), key=lambda ip: ip[1]))

    print(f"{x} logs")
    for k, v in methods.items():
        print(f"    method {k}: {v}")
    print(f'{status_number} status check')
    print('IPs:')
    i = 0
    for k, v in reversed(list(ips.items())[-10:]):
        if i < 10:
            print(f'\t{k}: {v}')
            i += 1
        else:
            break
