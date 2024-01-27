import random

word_list = [
    "creeper",
    "skeleton",
    "zombie",
    "spider",
    "slime",
    "enderman",
    "witch",
    "cave spider",
    "ghast",
    "blaze",
    "pigman",
    "guardian",
    "elder guardian",
    "wither skeleton",
    "husk",
    "stray",
    "phantom",
    "drowned",
    "vex",
    "evoker",
    "vindicator",
    "pillager",
    "ravager",
    "shulker",
    "endermite",
    "polar bear",
    "dolphin",
    "turtle",
    "panda",
    "fox",
    "bee",
    "hoglin",
    "zoglin",
    "piglin",
    "piglin brute",
    "warden",
    "axolotl",
    "goat",
]
# Select a random word from the list

selected_word = random.choice(word_list)

# Initialize variables
attempts = 6
guessed_letters = []
word_progress = ["_"] * len(selected_word)

# Main game loop
while attempts > 0 and "_" in word_progress:
  # Display current word progress
  print(" ".join(word_progress))
  # Ask the user for a letter
  guess = input("Guess a letter: ").lower()
  if guess in guessed_letters:
    print("You've already guessed that letter.")
    continue

  guessed_letters.append(guess)
  if guess in selected_word:
    for i, letter in enumerate(selected_word):
      if letter == guess:
        word_progress[i] = guess
  else:
    attempts -= 1
    print(f"Wrong guess! You have {attempts} attempts left.")

if "_" not in word_progress:
  print("Congratulations! You guessed the word:", selected_word)
else:
  print("Sorry, you've run out of attempts. The word was:", selected_word)
