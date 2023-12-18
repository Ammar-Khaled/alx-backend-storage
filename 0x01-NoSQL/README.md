0x01. NoSQL
===========

This repo is included in Specializations - Web Stack programming ― Back-end Course of **Holberton School** at **alx**. We will cover the `NoSQL` storage lessons.

Learning Objectives
-------------------

### General

*   What NoSQL means
*   What is difference between SQL and NoSQL
*   What is ACID
*   What is a document storage
*   What are NoSQL types
*   What are benefits of a NoSQL database
*   How to query information from a NoSQL database
*   How to insert/update/delete information from a NoSQL database
*   How to use MongoDB

Resources
---------

**Read or watch**:

*   [NoSQL Databases Explained](https://intranet.hbtn.io/rltoken/XDaZECz5EjsCTE7FuawqVw "NoSQL Databases Explained")
*   [What is NoSQL ?](https://intranet.hbtn.io/rltoken/96R3ey5fMYFEZvqCzfQpXA "What is NoSQL ?")
*   [Building Your First Application: An Introduction to MongoDB](https://intranet.hbtn.io/rltoken/KdQw7iu6r0ZxGq7xjg8XwA "Building Your First Application: An Introduction to MongoDB")
*   [MongoDB Tutorial 2 : Insert, Update, Remove, Query](https://intranet.hbtn.io/rltoken/DARNLVL94BA2VJq-8SOcjw "MongoDB Tutorial 2 : Insert, Update, Remove, Query")
*   [Aggregation](https://intranet.hbtn.io/rltoken/FSoKjBLrVK7dASzBtIPyew "Aggregation")
*   [Introduction to MongoDB and Python](https://intranet.hbtn.io/rltoken/oGMMglCCSi0a3_wZCJcAog "Introduction to MongoDB and Python")
*   [mongo Shell Methods](https://intranet.hbtn.io/rltoken/boIM7glDtG2o-AnkMkFHxQ "mongo Shell Methods")
*   [The mongo Shell](https://intranet.hbtn.io/rltoken/NteV2b6zrD8l8sKpNrQsRg "The mongo Shell")

More Info
---------

### Install MongoDB 4.2 in Ubuntu 18.04

[Official installation guide](https://intranet.hbtn.io/rltoken/w1QsUxCoOxvui7Ycr2aJfw "Official installation guide")

    $ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
    $ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
    $ sudo apt-get update
    $ sudo apt-get install -y mongodb-org
    ...
    $  sudo service mongod status
    mongod start/running, process 3627
    $ mongo --version
    MongoDB shell version v4.2.8
    git version: 43d25964249164d76d5e04dd6cf38f6111e21f5f
    OpenSSL version: OpenSSL 1.1.1  11 Sep 2018
    allocator: tcmalloc
    modules: none
    build environment:
        distmod: ubuntu1804
        distarch: x86_64
        target_arch: x86_64
    $  
    $ pip3 install pymongo
    $ python3
    >>> import pymongo
    >>> pymongo.__version__
    '3.10.1'
    

Potential issue if documents creation doesn’t work or this error: `Data directory /data/db not found., terminating` ([source](https://intranet.hbtn.io/rltoken/RuEv46l7OtXQZ3doQD7vjw "source") and [source](https://intranet.hbtn.io/rltoken/z_-s1Cfi7CdU-bemtQqQkQ "source"))

    $ sudo mkdir -p /data/db
    

Or if `/etc/init.d/mongod` is missing, please find here an example of the file:

Click to expand/hide file contents

