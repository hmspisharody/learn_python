def decor(func):
	name = input ("Enter Name : ")
	def wrap():
		print("=" * (len(name) + 10))
		print(func(name))
		print("=" * (len(name) + 10))
	return wrap

@decor
def print_text(name):
	return f"Hello, {name}!"

print_text()
#decorated()
