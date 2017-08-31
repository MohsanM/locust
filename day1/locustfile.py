from locust import HttpLocust
from tasks import MyTasks

class MyLocust(HttpLocust):
    task_set = MyTasks 
    min_wait = 5000
    max_wait = 15000
    host = 'http://35.188.225.51:8081'