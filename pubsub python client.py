# this is a simply python client publisher pubsub code.
#it is very basic and it is intented for quick uderstanding of how pubsub works
#additional functionalities can be added to it.

from google.cloud import pubsub_v1
import random
import time


PROJECT="<your-product"         
topic = "<your-topic"             


publisher = pubsub_v1.PublisherClient()     
topicpath = publisher.topic_path(PROJECT, topic)



def publish(publisher, topic, message):
    data = message.encode('utf-8')
    return publisher.publish(topic_path,  data)



def callback(message_future):
    if message_future.exception(timeout=30):
        print('Publishing message on {} threw an Exception {}.'.format(
            topic_name, message_future.exception()))
    else:
        print(message_future.result())


if __name__ == '__main__':
    while True:
        message_future = publish(publisher, topic_path, line)
        message_future.add_done_callback(callback)
        sleep_time = 4
        time.sleep(sleep_time)
