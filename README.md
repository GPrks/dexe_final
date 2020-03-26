# Set Up Instructions for App

Used Python 3.6 for the implementation.

**The ``python`` below refers to Python3.6, you can use ``python3`` EV instead**<br>

## Set Up the Environment

- Create the environment <br>
    - Inside parent dir ``dexe_final/`` open terminal and type:
    ``../dexe_final$ python -m venv venv``<br>
    - it created a python virtual environment, inside ``../dexe_final/venv/`` folder <br>

- Activate Virtual Environment on **Windows**: <br>
    - ``../dexe_final> cd venv/Scripts``<br>
    - ``../dexe_final/venv/Scripts> activate``<br>
    After that a symbol ``<venv>`` will appear

- Activate Virtual Environment on **Linux**: <br>
    - ``../dexe_final$ cd venv/bin``<br>
    - ``../dexe_final/venv/bin/$ source activate``<br>
    After that a symbol ``<venv>`` will appear

- Install requirements <br>
    - Inside the project there is a **requirements.txt** file <br>
    - Open terminal and type ``../dexe_final$ pip install -r requirements.txt``

## Configurations - Kafka, MySQL

- Config your App (config.py) <br>
    
    Go to config.py and change the credentials there are
    
    - for Kafka: <br>
        - kafka.host : Kafka server address
        - kafka.topic: the topic to subscribe
            
    - for MySQL: <br>
        - MySQL.host : MySQL server "ip:port"
        - MySQL.user: db username
        - MySQL.pass: db password
        - MySQL.schema: the schema

## Run the application

    ../dexe_final$ python main.py

 
#### Congratulations!
##### Your Kafka-MySQL pipeline is running

# MySQL scripts
`StoredProcedure.sql` includes the hourly margin aggregator `hourly_margin_aggregation`()

`EventScheduler.sql` includes event that runs the procedure **every 1hour at 00:00**