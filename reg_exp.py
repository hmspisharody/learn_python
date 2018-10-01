import re

string = "This is a Pig. Let's modify this Pig"

pattern = r"Pig"

match = re.match("This", string) #returns an object
print(match.span())
print(match.start())
print(match.end())
print(match.group())

search = re.search("Pig", string) #returns an object
print(search.span())
print(search.start())
print(search.end())
print(search.group())

f_all = re.findall("Pig", string) #returns a list
print(f_all) 

repl = "Horse"

new_string = re.sub(pattern, repl, string)
print(new_string)

#metacharacters
string = "This is a House. That is a Horse."
pattern = r"Ho.se" #'.' represents any character other than '\n'
print(re.sub(pattern, "Dog", string))

pattern = r"^gr.y$" #'^' represents start and '$' represents end of the string 
if re.match(pattern, "gray"):
    print("Match 1")
if re.match(pattern, "grey"):
    print("Match 2")
if re.match(pattern, "Stingray"):
    print("Match 3") # This won't print because start is not satisfied

#Character classes
pattern = r"[aeiou]" #any of the character inside []

if re.match(pattern, "sugar"):
    print("Match #1")
if re.match(pattern, "asphalt"):
    print("Match #2")
if re.search(pattern, "rhythm"):
    print("Match #3")
if re.search(pattern, "wonderful"):
    print("Match #4")

pattern = r"[A-Za-z][0-9]" #[A-Z], [a-z], [0-9]  caps, lowercase, number
if re.match(pattern, "90Days"): #won't satisfy as start is not <alpha><num>
    print("Number and alphabet")
if re.match(pattern, "A9fury"):
    print("Alphabet and number")
if re.match(r"[^0-9a-z]", "ABsomerandom234234"):
    print("starts with a non-numeric, non-smallercase")

#More metacharacters : 0 or more(*), 1 or more($), 0 or 1(?), x to y {x,y}

if re.match(r"[aeiou]*", "rhythm"):
    print("0 or more of vowels to start with")
if re.match(r"[aeiou]+", "rhythm"):
    print("This won't get printed - one or more")
if re.match(r"[aeiour]$", "rhythm"):
    print("This will get printed - 1 or more")
pattern = r"ice(-)?cream"
if re.match(pattern, "ice--cream"):
    print("This won't get printed - 0 or 1")
if re.match(r"[aeiou]?", "artillery"):
    print("This will get printed - 0 or 1")
if re.match(r"[aeiou]{,2}", "aegis"):
    print("0-2 vowels to start with")

pattern = r"(?P<greet>hello)(?:h)(a|e)"

match = re.match(pattern, "hellohari")

if match:
    print(match.groups()) # h won't be in this
    print(match.group("greet"))
match = re.match(pattern, "helloheri")
if match:
    print(match.groups())
    print(match.group(2))

pattern = r"(abc...)\1\1" #\ and group number

if re.match(pattern, "abcdefabcdef"):
    print("2 times")
if re.match(pattern, "abcdefabcdefabcdef"):
    print("3 times")
    


