import random

print("="*50)
print("🎉 ADVANCED RANDOM MAD LIBS GENERATOR 🎉")
print("="*50)

# Word categories
words = {
    "place": ["zoo", "space", "jungle", "school", "beach"],
    "animal": ["monkey", "lion", "penguin", "dragon", "dog"],
    "adjective": ["crazy", "funny", "scary", "tiny", "giant"],
    "verb": ["dancing", "running", "shouting", "flying", "sleeping"],
    "food": ["pizza", "burger", "ice cream", "pasta", "cake"]
}

# Story templates
stories = {
    1: """
    🌍 Today I went to the {place}.
    I saw a {adjective} {animal} {verb} near the gate.
    It was eating {food} happily!
    """,

    2: """
    🏝 In the middle of the {place},
    a {animal} was {verb}.
    Everyone said it looked very {adjective}.
    Later, it asked for some {food}.
    """,

    3: """
    🎢 Yesterday at the {place},
    I met a {adjective} {animal}.
    It started {verb} and threw {food} everywhere!
    """
}

story_count = 0

def random_story(template):
    """Generate story with random words"""
    return template.format(
        place=random.choice(words["place"]),
        animal=random.choice(words["animal"]),
        adjective=random.choice(words["adjective"]),
        verb=random.choice(words["verb"]),
        food=random.choice(words["food"])
    )


def user_story(template):
    """Generate story with user inputs"""
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    food = input("Enter a food: ")

    return template.format(
        place=place,
        animal=animal,
        adjective=adjective,
        verb=verb,
        food=food
    )


while True:

    print("\nChoose an option:")
    print("1️⃣ Random Story")
    print("2️⃣ Create Your Own Story")
    print("3️⃣ Add New Words")
    print("4️⃣ Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        print("\nSelect story type (1-3)")
        story_choice = int(input("Enter story number: "))

        if story_choice in stories:
            story = random_story(stories[story_choice])
            print("\n✨ Your Story:")
            print(story)
            story_count += 1
        else:
            print("Invalid story number!")

    elif choice == "2":

        print("\nSelect story type (1-3)")
        story_choice = int(input("Enter story number: "))

        if story_choice in stories:
            story = user_story(stories[story_choice])
            print("\n✨ Your Story:")
            print(story)
            story_count += 1
        else:
            print("Invalid story number!")

    elif choice == "3":

        category = input("Enter category (place/animal/adjective/verb/food): ").lower()

        if category in words:
            new_word = input("Enter new word: ")
            words[category].append(new_word)
            print("✅ Word added successfully!")
        else:
            print("❌ Invalid category!")

    elif choice == "4":
        print(f"\n📊 Total stories generated: {story_count}")
        print("Goodbye! 👋")
        break

    else:
        print("❌ Invalid choice. Try again.")