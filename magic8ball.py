import random

print("What is your name, stranger?")
name = input()

print("\nWhat is your question?")
question = input()

answer = ""
random_number = random.randint(1, 9)

answers = ['Yes - definitely.', 'It is decidedly so', 'Without a doubt.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'My sources say no.', 'Outlook not so good.', 'Very doubtful.']

if question == "":
  print("Magic 8-Ball cannot answer without a question! Try again\n")
else:
  if name == "":
    name = "Stranger"
  print("\n" + name + " asks: " + question)
  print("\nMagic 8-Ball's answer: " + answers[random_number])