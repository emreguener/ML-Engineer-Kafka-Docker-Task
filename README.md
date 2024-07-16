# ML-Engineer-Kafka-Docker-Task
A data pipeline project for ML Engineer task using Kafka and Docker to scrape, process, and serve data via REST API.

# TASK 1: Kafka Installation and Basic Operations using Docker and Kafka CLI

## Objective

- Install Kafka using Docker.
- Create a Kafka topic using Kafka CLI command.
- Send a message to the Kafka topic using Kafka CLI command.
- Listen to messages produced on the Kafka topic using Kafka CLI command.

## Steps

### 1. Install Kafka using Docker

Create a `docker-compose.yml` file to set up Kafka and Zookeeper.

```yaml
version: '3.9'

services:
  zookeeper:
    image: wurstmeister/zookeeper
    container_name: zookeeper
    ports:
      - "2181:2181"

  kafka:
    image: wurstmeister/kafka
    container_name: kafka
    ports:
      - "9092:9092"
    environment:
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: OUTSIDE://localhost:9092
      KAFKA_LISTENER_SECURITY_PROTOCOL_MAP: OUTSIDE:PLAINTEXT
      KAFKA_LISTENERS: OUTSIDE://0.0.0.0:9092
      KAFKA_INTER_BROKER_LISTENER_NAME: OUTSIDE
    depends_on:
      - zookeeper
```

`Start Kafka and Zookeeper:`
```
cd /path/to/your/docker-compose.yml
docker-compose up -d
docker exec -it <your_kafka_container_id> /bin/bash
```

`
Create a Kafka Topic using Kafka CLI
Connect to the Kafka container and create a topic named sample_topic:
`
```
kafka-topics.sh --bootstrap-server localhost:9092 --topic your_topic_name --create --partitions 3 --replication-factor 1
```

![image](https://github.com/user-attachments/assets/a8746133-00fe-4bd9-ab82-aaafb98bd2fe)


`
Send a Message to Kafka Topic using Kafka CLI
Use the Kafka Console Producer to send a message to sample_topic:
`
```
kafka-console-producer.sh --bootstrap-server localhost:9092 --topic your_topic_name
```

![image](https://github.com/user-attachments/assets/0e429298-cd88-45ba-b13f-876753f51bf9)


`
Listen to Messages from Kafka Topic using Kafka CLI
Use the Kafka Console Consumer to listen to messages from sample_topic:
`
```
kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic sample_topic --from-beginning
```

![image](https://github.com/user-attachments/assets/7a6a74b5-8ba7-4912-954f-fd2ede0ec40e)



# TASK 2: Data Scraping, Kafka Integration, and REST API Service

## Objective

- Scrape data from the provided URL.
- Write the scraped data to the Kafka topic in JSON format at 1-second intervals.
- Save the data written to the Kafka topic in a JSON file.
- Write a REST API service to serve the data from the JSON file.


`
Run the Data Scraping and Kafka Producer Script
Make sure Kafka and Zookeeper are running, then execute the data scraping script:
`
```
python scrape_send_save.py
```

`
Run the Flask Application
Start the Flask application to serve the data:
`
```
python app.py
```

`
Access the REST API
`

Get all products: http://localhost:5000/products

Get a specific product by name: http://localhost:5000/products/ExampleProductName



# TASK 3: Dockerizing the Application
This project is dockerized in Dockerfile and can be containerized and run using Docker.

