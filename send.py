import pika

def main():
    # connect to rabbitmq localhost
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port="5672"))
    channel = connection.channel()

    # define queue name hello
    channel.queue_declare(queue="hello")

    # send hello world to hello queue
    channel.basic_publish(exchange="", routing_key="hello", body="Hello world")

    # close connection
    connection.close()


if __name__ == "__main__":
    main()