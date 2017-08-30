from locust import TaskSet, task
import random 
import string 

def get_random_string(n):
	return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(n))

class MyTasks(TaskSet):
	@task 
	def lenght_5(self):
		random_string = get_random_string(5)
		json_response = dict()
		with self.client.get('/echo/' + random_string, name = 'Echo Api Get length(5)', catch_response = True)
			try: 
				json_response = response.json()
			except ValueError as e:
				response.failure('Could not pasre json response')
				return 

			if json_response['hello'] != random_string:
				response.failure('unexpected return value')
				return 

			response.success()

			

