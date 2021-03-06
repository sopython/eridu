import os


ACCESS_KEY = os.environ.get('STACKEXCHANGE_REQUESTS_KEY')
SITE = os.environ.get('ERIDU_SITE', 'stackoverflow')

POST_IDS_URL = "https://api.stackexchange.com/2.2/posts"
POST_IDS_NUMBER = int(os.environ.get('ERIDU_POST_IDS_NUMBER', 100))
POST_IDS_FILTER = os.environ.get('ERIDU_POST_IDS_FILTER', '!3tz1WbZW5IHcz*twZ')
POST_IDS_SORT = os.environ.get('ERIDU_POST_IDS_SORT', 'creation')
POST_IDS_ORDER = os.environ.get('ERIDU_POST_IDS_ORDER', 'asc')

QUESTIONS_URL = "https://api.stackexchange.com/2.2/questions/{}"
QUESTIONS_FILTER = os.environ.get('ERIDU_QUESTIONS_FILTER', '!OfZM.T7F9gRuLlvhzHoyC1Fyd3oEOAMszsZJXvHk4mw')
QUESTIONS_SORT = os.environ.get('ERIDU_QUESTIONS_SORT', 'creation')
QUESTIONS_ORDER = os.environ.get('ERIDU_QUESTIONS_ORDER', 'asc')

ANSWERS_URL = "https://api.stackexchange.com/2.2/answers/{}"
ANSWERS_FILTER = os.environ.get('ERIDU_ANSWERS_FILTER', '!Fcazzsr2b3Mo6cWaRk)J*C-n25')
ANSWERS_SORT = os.environ.get('ERIDU_ANSWERS_SORT', 'creation')
ANSWERS_ORDER = os.environ.get('ERIDU_ANSWERS_ORDER', 'asc')

FILTER_TAGS = os.environ.get('ERIDU_FILTER_TAGS', 'python,python-2.x,python-3.x')
SECONDS_BETWEEN_REQUESTS = int(os.environ.get('ERIDU_SECONDS_BETWEEN_REQUESTS', 300))

QUEUE_HOST = os.environ.get('ERIDU_RABBITMQ_HOST', 'rabbitmq')
QUEUE_PORT = int(os.environ.get('ERIDU_RABBITMQ_PORT', 5672))
EXCHANGE = os.environ.get('ERIDU_RABBITMQ_EXCHANGE', 'eridu')
QUESTIONS_ROUTING_KEY = os.environ.get('ERIDU_RABBITMQ_QUESTIONS_ROUTING_KEY', 'posts.historical.questions')
ANSWERS_ROUTING_KEY = os.environ.get('ERIDU_RABBITMQ_ANSWERS_ROUTING_KEY', 'posts.historical.answers')
