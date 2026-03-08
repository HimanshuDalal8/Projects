import random

print("🎉 Welcome to Random Mad Libs Generator!\n")

# Word categories
words = {
    "place": ["zoo", "space", "jungle", "school", "beach"],
    "animal": ["monkey", "lion", "penguin", "dragon", "dog"],
    "adjective": ["crazy", "funny", "scary", "tiny", "giant"],
    "verb": ["dancing", "running", "shouting", "flying", "sleeping"],
    "food": ["pizza", "burger", "ice cream", "pasta", "cake"]
}

# Story templates
stories = [
    """
    Today I went to the {place}.
    I saw a {adjective} {animal} {verb} near the gate.
    It was eating {food} happily!
    """,

    """
    In the middle of the {place},
    a {animal} was {verb}.
    Everyone said it looked very {adjective}.
    Later, it asked for some {food}.
    """,

    """
    Yesterday at the {place},
    I met a {adjective} {animal}.
    It started {verb} and threw {food} everywhere!
    """
]

while True:
    # Pick random story
    story_template = random.choice(stories)

    # Fill random words
    story = story_template.format(
        place=random.choice(words["place"]),
        animal=random.choice(words["animal"]),
        adjective=random.choice(words["adjective"]),
        verb=random.choice(words["verb"]),
        food=random.choice(words["food"])
    )

    print("\n✨ Here is your random story:")
    print(story)

    again = input("Generate another story? (yes/no): ").lower()
    if again != "yes":
        print("Goodbye! 👋")
        break