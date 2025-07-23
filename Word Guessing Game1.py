import random
import string
#Anthony
print("_" * 30)
print("\n\n\nWord guessing game.")
print("_" * 30)
print()

# List of all the words that could guessed.
word = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew", "kiwi", "lemon",
"mango", "nectarine", "orange", "papaya", "pear", "plum", "quince", "raspberry", "strawberry", "tangerine",
"watermelon", "blueberry", "blackberry", "cantaloupe", "pineapple", "pomegranate", "coconut", "almond", "cashew", "peanut",
"walnut", "hazelnut", "pecan", "macadamia", "brazil", "acorn", "oak", "pine", "maple", "willow",
"birch", "cypress", "redwood", "sequoia", "fir", "cedar", "spruce", "chestnut", "juniper", "holly",
"ivy", "rose", "lily", "tulip", "daffodil", "sunflower", "daisy", "violet", "orchid", "carnation",
"marigold", "peony", "lavender", "jasmine", "chamomile", "iris", "azalea", "begonia", "geranium", "poppy",
"hydrangea", "petunia", "lilac", "bougainvillea", "zinnia", "gardenia", "fuchsia", "gerbera", "anemone", "primrose",
"buttercup", "pansy", "snapdragon", "dahlia", "amaryllis", "crocus", "magnolia", "camellia", "begonia", "geranium",
"hollyhock", "chrysanthemum", "aster", "delphinium", "calla", "lupine", "yarrow", "heather", "violet", "thistle", "car", "bus", "train", "plane", "ship", "bicycle", "motorcycle", "scooter", "skateboard", "rollerblades","subway", "tram", "taxi", "helicopter", "rocket", "spaceship", "hovercraft", "carriage", "rickshaw", "wagon",
"van", "jeep", "convertible", "minivan", "pickup", "SUV", "coupe", "sedan", "hatchback", "roadster",
"limousine", "sports car", "compact car", "luxury car", "electric car", "hybrid car", "SUV", "convertible", "jeep", "camper",
"motorhome", "RV", "motorbike", "moped", "snowmobile", "all-terrain vehicle", "dune buggy", "quad bike", "tuktuk", "bus stop",
"train station", "airport", "dock", "ferry", "jet ski", "kayak", "canoe", "rowing boat", "sailboat", "fishing boat",
"yacht", "catamaran", "dinghy", "speedboat", "cruise ship", "freighter", "cargo ship", "ocean liner", "container ship", "fishing trawler",
"submarine", "hovercraft", "tugboat", "pontoon", "catamaran", "schooner", "clipper", "ferryboat", "fishing raft", "sailing ship", "dog", "cat", "rabbit", "hamster", "guinea pig", "fish", "bird", "lizard", "snake", "turtle",
"frog", "hedgehog", "gerbil", "rat", "mouse", "chinchilla", "ferret", "cockroach", "ant", "beetle",
"butterfly", "moth", "dragonfly", "fly", "spider", "bee", "wasp", "ladybug", "termite", "dung beetle",
"scorpion", "centipede", "millipede", "cricket", "grasshopper", "cockroach", "worm", "slug", "snail", "newt",
"starfish", "sea urchin", "clam", "octopus", "squid", "jellyfish", "lobster", "crab", "shrimp", "eel",
"whale", "dolphin", "shark", "seal", "walrus", "manatee", "otter", "polar bear", "grizzly bear", "koala",
"kangaroo", "wallaby", "platypus", "wombat", "lemur", "giraffe", "zebra", "lion", "tiger", "cheetah",
"elephant", "hippopotamus", "rhinoceros", "buffalo", "deer", "moose", "bison", "coyote", "wolf", "fox", "mountain", "hill", "valley", "river", "stream", "lake", "pond", "ocean", "sea", "beach",
"desert", "forest", "jungle", "savanna", "tundra", "prairie", "steppe", "swamp", "marsh", "bog",
"wetland", "volcano", "earthquake", "tsunami", "tornado", "storm", "hurricane", "typhoon", "cyclone", "blizzard",
"fog", "snow", "hail", "rain", "sleet", "dew", "mist", "cloud", "sun", "moon",
"star", "comet", "asteroid", "meteor", "galaxy", "planet", "universe", "solar system", "nebula", "black hole",
"eclipse", "orbit", "telescope", "satellite", "asteroid belt", "constellation", "milky way", "andromeda", "meteor shower", "space station",
"spaceship", "rocket", "satellite", "planetarium", "astronaut", "space suit", "zero gravity", "exoplanet", "cosmic dust", "light year", "book", "novel", "short story", "poem", "play", "essay", "article", "journal", "newspaper", "magazine",
"dictionary", "encyclopedia", "biography", "autobiography", "memoir", "textbook", "manual", "guide", "recipe", "catalog",
"comic book", "graphic novel", "script", "research paper", "thesis", "dissertation", "letter", "invitation", "greeting card", "postcard",
"billboard", "advertisement", "flyer", "brochure", "pamphlet", "manual", "newsletter", "calendar", "almanac", "autograph",
"booklet", "handbook", "guidebook", "travel guide", "logbook", "diary", "journal", "planner", "notebook", "sketchbook",
"album", "catalog", "program", "text", "page", "chapter", "paragraph", "sentence", "word", "letter"]

# Getting the random word in the list.
random_word = random.choice(word)

# Getting how much tries they get.
Ask = int(input("How much tries do you want?: "))
print("\n")

# Attempts they used.
tries = 0

# Max attempts.
maxtries = Ask - 1

# Attempts left.
current = Ask

def Hints (tries):
    if tries == 1:
        print(f"The amount of letters in the word is {len(random_word)}")
    elif tries == 2:
        print(f"The first letter of the word is: {random_word[0]}")
    elif tries == 3:
        print(f"The second letter of the word is: {random_word[1]}")
    elif tries == 4:
        print(f"The thrid letter of the word is: {random_word[2]}")



while tries <= maxtries:
    print(f"{current} Tries Left")
    Guess = input("Guess the word: ")
    if Guess.lower() == random_word.lower():
        print("Correct!")
        break
    else:
        tries = tries + 1
        current = current - 1
        print("_" * 30)
        print()

    Hints(tries)

        
# Telling the word
if tries > maxtries:
    print(f"The word was {random_word}\nTry again")