import random

subjects = [
    "The government",
    "A new study",
    "The local community",
    "Scientists",
    "Researchers",
    "The tech industry",
    "Ronaldo",
]

actions = [
    "announced a breakthrough in",
    "is concerned about",
    "celebrated the success of",
    "is investigating",
    "released a report on",
    "is developing new technology for",
    "won the championship in",
]

places_or_things = [
    "at Red Fort",
    "regarding climate change",
    "in the field of AI",
    "about public health",
    "in renewable energy",
    "in sports",
    "in football",
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    places_or_thing = random.choice(places_or_things)
    news_article = f"BREAKING NEWS!!:{subject} {action} {places_or_thing}."
    print("\n" + news_article)

    user_input = (
        input("Press Enter to generate another news article or type 'exit' to quit: ")
        .strip()
        .lower()
    )
    if user_input == "exit":
        break

print("Thank you for using the fake news generator!")
