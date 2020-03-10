def init():
	global form
	form = {}

def set(name, val):
	form[name] = val

def upd(name, val):
	try:
		form[name] = val
	except KeyError:
		print("映射中没有这个值！")
		return None

def get(name):
	try:
		return form[name]
	except KeyError:
		print("映射中没有这个值！")
		return None