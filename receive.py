import pika, os, sys

# callback function that is triggered whenever message is received
def callback(ch, method, properties, body):
    to_print = f"received {body}"
    print(to_print)


def main():
    # connect to rabbitmq
    connection = pika.BlockingConnection(pika.ConnectionParameters(host="localhost", port="5672"))
    channel = connection.channel()

    # declare queue hello
    channel.queue_declare(queue="hello")

    # define callback when consuming
    channel.basic_consume(queue="hello", auto_ack=True, on_message_callback=callback)

    # start consuming, its a looping process
    channel.start_consuming()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)