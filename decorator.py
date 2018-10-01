def decor(func):
  def wrap():
    name = input("Enter Name : ")
    print("=" * (len(name) + 10))
    func(name)
    print("=" * (len(name) + 10))
  return wrap

#@decor
def print_text(name):
    print("  Hello " + name + "!")

print_text = decor(print_text)
print_text()
#decorated()
