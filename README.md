# rabbitmq2solr

rabbitmq2solr is a simple utility that consumes messages from a RabbitMQ queue and index to Solr.
Messages are expected to be JSON documents that send to Solr update endpoint. If indexing fails, the message is sent to a dead letter queue for later use.
The messages that sent to DLQ, delivered as persistent messages. This job will exit when the queue is empty.

# Environment Variables

- `MQ_HOST`: The hostname of the RabbitMQ server.
- `MQ_PORT`: The port of the RabbitMQ server. Optional. Default: 5672.
- `MQ_USER`: The username to use when connecting to the RabbitMQ server.
- `MQ_PASS`: The password to use when connecting to the RabbitMQ server.
- `MQ_VHOST`: The virtual host to use when connecting to the RabbitMQ server.
- `MQ_QUEUE`: The name of the queue to consume messages from.
- `MQ_QUEUE_DURABLE`: Whether or not the queue should be durable. Optional. Default: True.
- `MQ_DLQ_EXCHANGE`: The exchange of the dead letter queue to use. If index errors occur, messages will be moved to this queue.
- `MQ_DLQ_ROUTING_KEY`: The routing key of the dead letter queue to use.
- `SOLR_BASE_URL`: The base url of the Solr server. Example: http://localhost:8983/solr (without trailing slash).
- `SOLR_COLLECTION`: The name of the Solr collection to index to. Optional. Default: Routing key of message.
- `LOG_LEVEL`: The log level to use. Optional. Default: DEBUG.
- `CONSUMER_POOL_SIZE`: The number of concurrent consumers to use.