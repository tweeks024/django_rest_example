import requests



base_url = "http://localhost:8000/"
endpoint = "api/updates/"

def get_list():
	r = requests.get(base_url + endpoint)
	data = r.json()
	for obj in data:
		print(obj['id'])
		r = requests.get(base_url + endpoint + str(obj['id']))
		print(r.json())
	#return data


def create_update():
	new_data = {
		'user': 1,
		'content': 'another cool new update',

	}

	r = requests.post(base_url + endpoint, data=new_data)
	print(r.status_code)
	print(r.headers)
	if r.status_code == requests.codes.ok:
		return r.json()


print(create_update())

print(get_list())
