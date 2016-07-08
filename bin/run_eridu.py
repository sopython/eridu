# -*- coding: utf-8 -*-

import json
import time

import click
import schedule
import pika

from eridu.logger import logger
from eridu.config import FILTER_TAGS, SECONDS_BETWEEN_REQUESTS
from eridu.config import QUEUE_HOST, QUEUE_PORT, EXCHANGE, QUESTIONS_ROUTING_KEY, ANSWERS_ROUTING_KEY
from eridu.core import get_post_ids, split_post_ids, get_questions, get_answers, filter_posts_by_tag

@click.command()
@click.option('--start', default=1, help="Starting page for historic results.")
def main(start):
    """Console script for eridu"""
    logger.info('Starting main function in Eridu service.')

    page = start or 0
    params = {'page': page}
    tags = [s.strip() for s in FILTER_TAGS.split(',')]

    logger.info('Starting on page {}'.format(page))
    logger.info('Filtering to include the following tags: {}.'.format(tags))
    logger.info('Getting requests every {} seconds.'.format(SECONDS_BETWEEN_REQUESTS))

    def run(params):
        page = params.get('page')
        logger.info('Getting posts for page {}.'.format(page))

        connection = pika.BlockingConnection(pika.ConnectionParameters(
            host=QUEUE_HOST,
            port=QUEUE_PORT)
        )
        channel = connection.channel()

        channel.exchange_declare(exchange=EXCHANGE,
                                 type='topic')

        post_ids = get_post_ids(page)
        ids = split_post_ids(post_ids['items'])

        questions = get_questions(ids['question_ids'])
        questions = filter_posts_by_tag(questions['items'], tags)

        routing_key = QUESTIONS_ROUTING_KEY
        for question in questions:
            message = json.dumps(question)
            channel.basic_publish(exchange=EXCHANGE,
                                  routing_key=routing_key,
                                  body=message)

        answers = get_answers(ids['answer_ids'])
        answers = filter_posts_by_tag(answers['items'], tags)

        routing_key = ANSWERS_ROUTING_KEY
        for answer in answers:
            message = json.dumps(answer)
            channel.basic_publish(exchange=EXCHANGE,
                                  routing_key=routing_key,
                                  body=message)

        connection.close()

        params['page'] += 1


    schedule.every(SECONDS_BETWEEN_REQUESTS).seconds.do(run, params=params)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
