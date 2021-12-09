import math

print()

print("Type one of the following: how are you, tell a joke, do a square root\n")

while True:
  command = input("YOU: ")

  if command.lower() == "how are you":
    print("BOT: I'm doing great")
  elif command.lower() == "tell a joke":
    print("BOT: What do you call 2000 mockingbirds?")
    input("YOU: ")
    print("BOT: two kilo mockingbird")
  elif command.lower() == "do a square root":
    print("BOT: type a positive number")
    num = float(input("YOU: "))
    print(f"BOT: the square root of {num} is {math.sqrt(num)}")
  else:
    print("BOT: I don't understand")
