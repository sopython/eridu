# -*- coding: utf-8 -*-

import time

import click
import schedule

from eridu.logger import logger
from eridu.config import FILTER_TAGS, SECONDS_BETWEEN_REQUESTS
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

        post_ids = get_post_ids(page)
        ids = split_post_ids(post_ids['items'])

        questions = get_questions(ids['question_ids'])
        questions = filter_posts_by_tag(questions['items'], tags)
        for question in questions:
            try:
                print(question)
            except UnicodeEncodeError:
                pass

        print('\n\n')

        answers = get_answers(ids['answer_ids'])
        answers = filter_posts_by_tag(answers['items'], tags)
        for answer in answers:
            try:
                print(answer)
            except UnicodeEncodeError:
                pass

        params['page'] += 1


    schedule.every(SECONDS_BETWEEN_REQUESTS).seconds.do(run, params=params)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
