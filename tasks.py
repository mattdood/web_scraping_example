from celery import Celery
from celery.schedules import crontab # scheduler

app = Celery('tasks')

@app.task
def add(x, y):
    return x + y

# scheduled task execution
# docs.celeryproject.org/en/stable/userguide/periodic-tasks.html
app.conf.beat_schedule = {
    # executes every 1 minute
    'scraping-task-one-min': {
        'task': 'tasks.<task here>',
        'schedule': crontab()
    },
    # executes every 15 minutes
    # 'scraping-task-fifteen-min': {
    #     'task': 'tasks.<task here>',
    #     'schedule': crontab(minute='*/15')
    # },
    # executes daily at midnight
    # 'scraping-task-midnight-daily': {
    #     'task': 'tasks.<task here>',
    #     'schedule': crontab(minute=0, hour=0)
    # }
}