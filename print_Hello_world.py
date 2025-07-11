def hello(to="world"):
    print("Hello,", to)

def main():
    print(
        "Did you know that Earth has a gravitational force?",
        "And this keeps us all down to Earth.",
        sep="\n"
    )
    print(
        "Well, every planet has its own varying gravity.",
        "But what does this mean to you?",
        "Well, I can show you something cool.",
        sep="\n"
    )

    # Get user's weight
    try:
        weight = float(input("Mind sharing your weight (kg's only)? 🙂 "))
    except ValueError:
        print("Oops! That's not a valid number.")
        return

    # Planetary gravity relative to Earth
    gravity_factors = {
        "Mercury": 0.38,
        "Venus": 0.91,
        "Earth": 1.00,
        "Moon": 0.17,
        "Mars": 0.38,
        "Jupiter": 2.34,
        "Saturn": 1.06,
        "Uranus": 0.92,
        "Neptune": 1.19,
        "Sun": 27.9
    }

    planet_chosen = input("Can you name a planet from our solar system, or the Moon or the Sun? ").strip().title()

    # Fix common lowercase entries
    if planet_chosen.lower() == "moon":
        planet_chosen = "Moon"
    elif planet_chosen.lower() == "sun":
        planet_chosen = "Sun"

    if planet_chosen in gravity_factors:
        adjusted_weight = weight * gravity_factors[planet_chosen]
        print(f"🌍 Your weight on {planet_chosen} would be approximately {adjusted_weight:.2f} kg")
    else:
        print("🚨 Oops! I don't recognize that as a valid planet or celestial body. Try again maybe?")

# -- Initial greetings --
hello()
name = input("Hi, your name please? ").strip().capitalize()
hello(name)

# -- Mood check --
try:
    mood_input = int(input("Hey!! how you doin'? (great(1)/ nothing(0)): "))
except ValueError:
    print("That's not 0 or 1, cheeky space cadet! Let's just assume you're neutral 🙂")
    mood_input = 0

if mood_input == 1:
    print("Wonderful!", "Check this out ↓", sep="\n")
else:
    print("Let's make your day...", "Buckle your seat belts! 🚀", sep="\n")

# -- Enter main universe --
main()

print("Isn't it cool ",
      f"Have a nice day Mr./Mrs. {name}!", 
      sep="\n"
      );
