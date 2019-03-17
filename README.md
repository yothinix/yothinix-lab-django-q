# Lab Django-Q

## Installing
To install the project clone this repository to your local then
1. `pipenv install`
2. `cd demo`
3. `python manage.py migrate` Migrate the database
4. `python manage.py createsuperuser` Create your desire superuser
5. `python manage.py runserver`


## Experiment
### Starting Worker
```
python manage.py qcluster
```

### Start Worker Monitor
```
python manage.py qmonitor
```

### Adding task to queue
```python
from django_q.tasks import async_task
from core.tasks import process_something # target function we want to run in queue


async_task(process_something)  # This will add the task to queue, then it will process
```

### Verify result
You can verify result via Django admin at http://localhost:8000/admin/django_q/


## Technical Note
- Task will stay on `Queued tasks` If the task is failed and add in `Failed tasks`, If the task success it will removed from `Queued tasks` and add in `Successful tasks`
- To config just add `django_q` in INSTALLED_APP in settings.py
- To config to use DjangoORM as broker, you need to add following setting in settings.py
```python
Q_CLUSTER = {
    'name': 'DjangORM',
    'workers': 4,
    'timeout': 90,
    'retry': 120,
    'queue_limit': 50,
    'bulk': 10,
    'orm': 'default'
}
```

## Reference
- https://github.com/Koed00/django-q
- https://django-q.readthedocs.io/en/latest/index.html
