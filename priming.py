# Used in the prompts to indicate the boundary between a prefix and its corresponding value
# NOTE: The prefix delimiter should not occur anywhere in the example value that follows a prefix
PREFIX_DELIMITER = ':'

ACRONYM_PROMPT_COMPONENTS = {
  "preamble": "An acronym is an abbreviation of several words in such a way that the abbreviation itself forms a pronounceable word.",
  "prefixes": [
    f"Here is a word{PREFIX_DELIMITER}",
    f"Here is an acronym of the word{PREFIX_DELIMITER}",
    ""
  ],
  "examples": [
    ["\"rap\"", "RAP - Recognizing Analogous Patterns"],
    ["\"mural\"", "MURAL - Magnifying Urban Realities Affecting Lives"],
    ["\"wow\"", "WOW - Walking On Water"],
    ["\"happy\"", "HAPPY - Having A Purpose Promises Youth"],
    ["\"weapon\"", "WEAPON - Wieldable Equipment for Aggressive Purposes Or Neutralization"],
    ["\"hope\"", "HOPE - Holding Optimistic Possibilities Endlessly"],
    ["\"youth\"", "YOUTH - Young Outstanding Unique Trailblazers of Humanity"],
    ["\"wave\"", "WAVE - Water Affecting Vital Environments"],
    ["\"fly\"", "FLY - Freely Leaving Yesterday"],
    ["\"acoustic\"", "ACOUSTIC - Actively Creating Our Unique Sounds To Intoxicate the Crowd"],
    ["\"murder\"", "MURDER - Maliciously Undertaken Ruthless Deadly Executioner's Rage"],
    ["\"love\"", "LOVE - Living Overtly Via Empathy"],
    ["\"music\"", "MUSIC - Making Up Sounds Intuitively and Creatively"],
    ["\"punk\"", "PUNK - Passionate Unconventional Non-conformist Kid"],
    ["\"safety\"", "SAFETY - Stopping All Fatal Efforts Towards You"],
    ["\"Kilimanjaro\"", "KILIMANJARO - Keen Individuals Leading In Marvelous Adventures, Navigating and Journeying Across the Rugged Outdoors"],
    ["\"forgive\"", "FORGIVE - Finding Opportunities to Release Grudges, Inspiring Virtue and Empathy"],
    ["\"cheetahs\"", "CHEETAHS - Cunning Hunters, Energetic and Efficient with Terrific Agility and High Speeds"],
    ["\"radio\"", "RADIO - Receiving Audio Data with Instant Output"],
    ["\"win\"", "WIN - Whatever It Takes"],
    ["\"money\"", "MONEY - Made Only by Nearly Exploiting Yourself"],
    ["\"time\"", "TIME - The Inevitable Memorializer of Events"],
    ["\"change\"", "CHANGE - Cultivating Higher Ambitions and New Goals for Evolution"],
    ["\"risk\"", "RISK - Reward Is Seldom Known"],
    ["\"lyric\"", "LYRIC - Let Your Rhythm Instill Courage"],
    ["\"code\"", "CODE - Completely Optimized Data Exchange"],
    ["\"New York\"", "NEW YORK - No Evil Within, Your Own Righteous Kingdom"],
    ["\"tortoise\"", "TORTOISE - The Old Reptile Takes Ownership of Its Sluggish Existence"],
    ["\"skateboard\"", "SKATEBOARD - Sport Known Among Thrill-seekers Everywhere Because Of Adrenaline Rushes Delivered"],
    ["\"love is blind\"", "LOVE IS BLIND - Letting Our Vulnerability Expose Imperfections Shows that Beauty Lies In Noticing Differences"],
    ["\"dumb luck\"", "DUMB LUCK - Destiny Unleashes Miracles, Bringing Life's Unforeseen Consequences Kindly"],
    ["\"yo-yo\"", "YO-YO - Yanking Over Your Orbit"],
    ["\"mannequin\"", "MANNEQUIN - Mobile, Adjustable, Nondescript, and Naked Embodiment that Questions Universal Identity Norms"],
    ["\"Midas touch\"", "MIDAS TOUCH - Making It Desirable And Successful Through Original, Unique, and Creative Habits"]
  ]
}



CHAIN_PROMPT_COMPONENTS = {
  "preamble": "A word chain is a sequence of eight words where each word in the sequence is semantically related to the word that precedes it.",
  "prefixes": [
    f"Here is a word{PREFIX_DELIMITER}",
    f"Here is an example of a word chain beginning with it{PREFIX_DELIMITER}",
    ""
  ],
  "examples": [
    [
      "\"fresh\"",
      "fresh, fruit, orange, juice, blender, kitchen, chef, kiss"
    ],
    [
      "\"bat\"",
      "bat, ball, baseball, field, hill, mountain, cave, stalactite"
    ],
    [
      "\"run\"",
      "run, exercise, muscle, strength, power, voltage, current, affairs"
    ],
    [
      "\"rise\"",
      "rise, sun, flower, soil, farm, wheat, dough, cookie"
    ],
    [
      "\"oil\"",
      "oil, barrel, trade, war, peace, treaty, sign, pen"
    ],
    [
      "\"light\"",
      "light, feather, bird, nest, home, sweet, candy, corn"
    ],
    [
      "\"wave\"",
      "wave, ocean, beach, sand, castle, royalty, flag, pole"
    ],
    [
      "\"letter\"",
      "letter, write, read, book, library, school, cafeteria, lunch lady"
    ],
    [
      "\"joystick\"",
      "joystick, video game, fun, happy, smile, teeth, shark, tank"
    ],
    [
      "\"soul\"",
      "soul, body, heart, beat, dance, floor, shoe, sole"
    ],
    [
      "\"slow-mo\"",
      "slow-mo, capture, cage, bird, sing, voice, speech, podium"
    ],
    [
      "\"mini golf\"",
      "mini golf, hole, ground, dirt, shovel, snow, ice, cube"
    ]
  ]
}


EXPLODE_PROMPT_COMPONENTS = {
  "preamble": "A same-sounding phrase is a phrase that sounds like another word or phrase.",
  "prefixes": [
    f"Here is a word{PREFIX_DELIMITER}",
    f"Here is a same-sounding phrase for the word{PREFIX_DELIMITER}"
  ],
  "examples": [
    ["\"defeat\"", 'da feet (as in "the" feet)'],
    ["\"defeat\"", "deaf eat (can't hear while eating)"],
    ["\"surprise\"", 'Sir Prize (a knight whose name is Prize)'],
    ["\"surprise\"", 'serf prize (award given to a feudal laborer)'],
    ["\"weapon\"", 'weep on (to cry on)'],
    ["\"weapon\"", 'wee pawn (a tiny chess piece)'],
    ["\"stabilize\"", 'stable eyes (a steady gaze)'],
    ["\"adoration\"", 'add oration (to include a formal speech)'],
    ["\"ridiculous\"", 'ridicule us (to shame us collectively)'],
    ["\"ridiculous\"", 'ridicule less (to be less scornful)'],
    ["\"sensation\"", 'sensei shun (to avoid your martial arts teacher)'],
    ["\"sensation\"", 'sin say shun (to admit your sins and become a pariah)'],
    ["\"recognize\"", "wreck on eyes (so visually outrageous that it's painful)"],
    ["\"recognize\"", 'wreck on ice (to wipe out on a frozen pond)'],
    ["\"recognize\"", 're-cognize (to fix broken gears in a clock)'],
    ["\"American\"", "I'm arrogant (self-admission of haughtiness)"],
    ["\"American\"", 'aim Eric can (Eric is a skilled marksman)'],
    ["\"recollection\"", 'wreck collection (cleanup after a traffic accident)'],
    ["\"euthanasia\"", 'youth in Asia (youngsters in Asia)'],
    ["\"depend\"", 'deep end (deep section of a swimming pool)'],
    ["\"gemini\"", 'gem in eye (a precious stone lodged in the cornea)'],
    ["\"example\"", 'egg sample (a trial tasting of an egg)'],
    ["\"initiate\"", 'and then she ate (and she subsequently ate)'],
    ["\"innuendo\"", 'in your window (perched on your windowsill)'],
    ["\"moustache\"", 'must ask (need to inquire)'],
    ["\"mystery\"", 'missed hurry (overlooked haste)'],
    ["\"expressway\"", 'express whey (a speedy delivery of milk byproduct)'],
    ["\"expressway\"", 'express sway (to demonstrate influence)'],
    ["\"expressway\"", 'ex-press way (a path without news media)'],
    ["\"committed\"", 'come mitted (to show up in boxing gloves, ready to fight)'],
    ["\"committed\"", 'comet kid (an aspiring astronaut)'],
    ["\"mismanaged\"", 'mess-managed (overseen by a mess)'],
    ["\"topics\"", 'top picks (best selections)'],
    ["\"topics\"", 'two pics (two pictures)'],
    ["\"defender\"", 'defend her (protect her)'],
    ["\"extraordinary\"", 'X-ray or dairy? (a choice between radiology or milk)'],
    ["\"capitalize\"", 'capital eyes (honed-in on financial assets)'],
    ["\"capitalize\"", "capital lies (misinformation from the country's administrative center)"],
    ["\"provoking\"", 'pro-vogue king (a monarch in support of voguing)'],
    ["\"provoking\"", 'provoke king (a master antagonizer)'],
    ["\"Tibet\"", 'tie bet (an evenly matched wager)'],
    ["\"Tibet\"", 'Thai bat (a bat from Thailand)'],
    ["\"immediate\"", 'I mediate (I intervene)'],
    ["\"immediate\"", 'Imma date it (as in "I\'m going to write today\'s date on it")'],
    ["\"paper\"", 'pay peer (to give a friend money)'],
    ["\"paper\"", 'pa pure (dad is clean)'],
    ["\"beer\"", 'be here (to be present)'],
    ["\"secondary\"", 'sickened dairy (milk that has gone bad)'],
    ["\"secondary\"", 'seek a deary (to search for a grandchild)'],
    ["\"occasion\"", 'oak case in (to box something in with oak wood)'],
    ["\"automatic\"", 'auto Matt sick (Matt instantly becomes ill)']
  ]
}



POV_PROMPT_COMPONENTS = {
  "preamble": "A \"hot take\" is a perspective that is novel and thought-provoking. Some hot takes are lighthearted and humorous, while others may be provocative or polarizing.",
  "prefixes": [
    f"Here is a topic{PREFIX_DELIMITER}",
    f"Here is a hot takes about it{PREFIX_DELIMITER}"
  ],
  "examples": [
    [
      "fast food",
      "Fast food is a game of Russian roulette with your taste buds and digestive system.",
    ],
    [
      "mythology",
      "Mythology is a treasure trove of dad jokes.",
       
    ],
    [
      "gummy bears",
      "Gummy bears are the perfect snack for people who like to chew their food into submission.",
    ],
    [
      "cell phones",
      "Cell phones have turned people into terrible listeners.",
    ],
    [
      "GMOs",
      "GMOs are the product of bored scientists who need a new hobby.",
    ]
  ]
}



SCENE_PROMPT_COMPONENTS = {
  "preamble": "Sensory details are details that appeal to the five senses: vision, hearing, touch, smell, and taste. Sensory details make our writing more interesting and vivid, and the most effective sensory details are ones that are creative yet concrete and evocative. For each thing below, we provide a list of sensory details that evoke that thing.",
  "prefixes": [
    f"Here is a thing{PREFIX_DELIMITER}",
    f"Here are some sensory details that evoke that thing{PREFIX_DELIMITER}"
  ],
  "examples": [
    [
      "NYC subway car",
      "\n".join([
        "A discarded slushie cup dripping red liquid onto a seat",
        "The conductor saying something over the speaker, but the sound is too muffled to make out what they're saying",
        "A person doing acrobatic maneuvers on the grab bars",
        "Rats scurrying through the train tracks",
        "A busker giving a mediocre performance"
      ])
    ],
    [
      "tech company office",
      "\n".join([
        "A group of software engineers lounging in 'nap pods'",
        "Your boss joining a meeting from a desk that is attached to a treadmill",
        "The crinkling of snack wrappers as a custodial worker replenishes the free snacks in the kitchen",
        "Kombucha and cold brew on tap",
        "Modern, angular furniture that isn't very comfortable"
      ])
    ],
    [
      "my abuela",
      '\n'.join([
        "A giant pot of rice and beans simmering on the stove",
        "A tiny radio on the counter playing music from her home country",
        "A rosary hanging on the wall",
        "Her speaking to me in Spanish and me responding in English",
        "The sound of knitting needles gently clanking together"
      ])
    ],
    [
      "standing in line at the DMV",
      '\n'.join([
        "An anxious teenager who is visibly dissatisfied with their new license photo but too nervous to ask to retake it",
        "A pen with a plastic spoon taped to it to prevent people from taking it",
        "A very loud air conditioning unit that is doing a poor job of cooling the place down",
        "A woman with screaming children talking on the phone",
        "A vaguely musty smell"
      ])
    ],
    [
      "boarding a plane",
      '\n'.join([
        "A faint smell of jet fumes as the plane taxis toward the runway",
        "The pilot's voice over the speaker saying, 'Attention passengers, this is your pilot speaking...'",
        "A young child repeatedly opening and closing the window shade",
        "A tiny dog stuffed in a carrier beneath the seat",
        "A flight attendant explaining the emergency evacuation procedures to the people seated in the exit row"
      ])
    ],
    [
      "a Korean spa",
      '\n'.join([
        "The smell of eucalyptus and hot wood",
        "The sound of a shocked gasp when a guest realizes that they have accidentally stepped into the cool bath instead of the hot bath",
        "A heap of discarded white towels",
        "A food court that sells all of the Korean food staples",
        "Matching spa uniforms"
      ])
    ]
  ]
}



SIMILE_PROMPT_COMPONENTS = {
  "preamble": "A good simile contains a concrete image that illustrates the concept we want to convey without being too obvious. Good similes are unexpected and evocative. Below are some examples of good similes.",
  "prefixes": [
    f"Here is a concept{PREFIX_DELIMITER}",
    f"Here is a simile that illustrates it{PREFIX_DELIMITER}"
  ],
  "examples": [
    [
      "a helping hand",
      "I just come around to help like Batman's utility belt."
    ],
    [
      "pizza",
      "Pizza is like a symphony of flavors, with each ingredient representing a note in a complex harmony that dances across the tongue."
    ],
    [
      "struggling through life",
      "Life is like making a diamond—finding treasure in the pressure and doing a whole lot of shaping and shining."
    ],
    [
      "silence",
      "The silence was like a deep, still pool of water, reflecting nothing but its own serene emptiness, yet hiding unfathomable truths beneath its surface."
    ],
    [
      "a long-distance relationship",
      "A long-distance relationship is like playing tennis against a wall. It's doable, but pales in comparison to having an in-person companion."
    ],
    [
      "something going differently than you anticipated",
      "The unexpected turn of events was like a sudden gust of wind inside a Buddhist temple, scattering the grains of the meticulously arranged sand mandala that was my future."
    ],
    [
      "pretending",
      "Pretending was like an elaborate dance—even when the steps were rehearsed to perfection, the rhythm always felt slightly off, and the movements lacked the elusive grace that comes from spontaneous expression."
    ],
    [
      "a croaky voice",
      "The man's voice was like a rusty hinge that had not been oiled for years, emitting a groan of protest with every movement."
    ],
    [
      "notoriety is short-lived",
      "Glory is like a circle in the water, which never ceases to enlarge itself until it expands endlessly into nothing."
    ],
    [
      "a drizzle",
      "The rain was like a delicate veil, casting a misty shroud over the familiar landscape, lending an air of mystery to the mundane."
    ],
    [
      "exhaustion",
      "Every step I took felt like wading through molasses, and the even slightest exertions left me gasping for breath."
    ],
    [
      "unpleasant memories",
      "Like a cloud of noxious fumes, the memories suffused every waking moment with their acrid stench, obscuring the present and casting a shadow over the future."
    ],
    [
      "something bothering you",
      "It was like a loose thread on a sweater, inconspicuous but insistent, tugging at the fabric of my psyche until it finally threatened to unravel everything."
    ],
    [
      "a beautiful lady",
      "Her beauty hangs upon the cheek of night, like a rich jewel in an Ethiop's ear."
    ]
  ]
}



UNEXPECT_PROMPT_COMPONENTS = {
  "preamble": "For each scene below, we provide an example of how you can incorporate additional details to give that scene an unexpected twist.",
  "prefixes": [
    f"Here is a scene{PREFIX_DELIMITER}",
    f"Here is an unexpected twist{PREFIX_DELIMITER}"
  ],
  "examples": [
    ["rapping", "rapping in morse code"],
    ["a parking ticket", "a parking ticket that is written in Sanskrit and folded into an origami swan"],
    ["snorkeling", "snorkeling in a massive bathtub filled with champagne"],
    ["a door", "a door that only opens when you sing the national anthem of Equatorial Guinea"],
    ["grinding a skateboard", "grinding a skateboard on Titanic railings"],
    ["eating ramen", "eating ramen with chopsticks that are made out of icicles"],
    ["painting a mural", "painting a mural on the ceiling of a commercial airliner"],
    ["playing piano", "playing piano in the middle of the mosh pit at a metal concert"],
    ["a church", "a church that is made out of Jenga blocks"],
    ["sleeping", "sleeping in a hammock that is tied between two stop signs"],
    ["a Bonsai tree", "a Bonsai tree that is made out of broccoli"],
    ["playing soccer", "playing soccer with a bowling ball on a field that is made out of Lego bricks"]
  ]
}



UNFOLD_PROMPT_COMPONENTS = {
  "preamble": "",
  "prefixes": [
    f"Here is a target word{PREFIX_DELIMITER}",
    f"Here are some ways the target word appears in other words and phrases{PREFIX_DELIMITER}"
  ],
  "examples": [
    [
      "space",
      '\n'.join([
        "outer space",
        "space suit",
        "Space Age (historical period)",
        "backspace",
        "space heater",
        "parking space",
        "space-time continuum",
        "Space Invaders (video game)",
        "crawl space",
        "latent space",
        "Lost in Space (TV series)"
      ])
    ],
    [
      "back",
      '\n'.join([
        "backup",
        "backpack",
        "back-to-back",
        "comeback",
        "throwback",
        "the straw that broke the camel's back",
        "back and forth",
        "callback",
        "backgammon",
        "back against the wall",
        "back burner",
        "circle back",
        "dial back",
        "have someone's back"
      ])
    ],
    [
      "run",
      '\n'.join([
        "run away",
        "home run",
        "run for one's money",
        "dry run",
        "run the show",
        "on the run",
        "run a red light",
        "run in circles",
        "run for office",
        "running on fumes",
        "still waters run deep",
        "runny nose"
      ])
    ],
    [
      "brain",
      '\n'.join([
        "brainstorm",
        "brain freeze",
        "brain dead",
        "pick someone's brain",
        "brain fart",
        "Pinky and The Brain (TV series)",
        "brain bucket",
        "brain tumor",
        "rack one's brain",
        "brain teaser",
        "brain cramp",
        "scatterbrained"
      ])
    ],
    [
      "jump",
      '\n'.join([
        "jump-start",
        "jump the gun",
        "jump at the chance",
        "jump the shark",
        "jump ship",
        "jump rope",
        "jump on the bandwagon",
        "jumpsuit",
        "jump out of one's skin",
        "jump to conclusions",
        "jump for joy",
        "hop, skip, and a jump"
      ])
    ],
    [
      "free",
      '\n'.join([
        "free will",
        "Free Willy (1993 film)",
        "scot-free",
        "free-for-all",
        "freestyle",
        "free time",
        "freeloader",
        "free agent",
        "freehand",
        "free range",
        "home free",
        "free rein",
        "if you love someone, set them free"
      ])
    ],
    [
      "light",
      '\n'.join([
        "spotlight",
        "lightsaber",
        "Northern Lights (Aurora Borealis)",
        "light year",
        "light at the end of the tunnel",
        "traffic light",
        "make light of",
        "gaslight",
        "light as a feather",
        "red-light district",
        "in light of",
        "daylight",
        "lights-out"
      ])
    ],
    [
      "i",
      '\n'.join([
        "I-beam",
        "dot the i's and cross the t's",
        "iPhone",
        "I-95 (interstate)",
        "I, Robot (2004 film)",
        "i.e.",
        "IHOP (restaurant)"
      ])
    ],
    [
      "force",
      '\n'.join([
        "workforce",
        "tour de force",
        "force field",
        "force-feed",
        "force of habit",
        "force quit",
        "force someone's hand",
        "by force",
        "brute force",
        "force of nature",
        "a force to be reckoned with",
        "may the Force be with you (quote from Star Wars franchise)"
      ])
    ],
    [
      "bar",
      '\n'.join([
        "raise the bar",
        "bar of gold",
        "bar fight",
        "bar exam",
        "bar of soap",
        "bartender",
        "handlebar",
        "barcode",
        "wine bar",
        "bar mitzvah"
      ])
    ],
    [
      "2",
      '\n'.join([
        "2-for-1",
        "two peas in a pod",
        "two-ply",
        "catch-22",
        "one-two combo",
        "two-party system",
        "two wrongs don't make a right",
        "two cents",
        "lesser of two evils",
        "two-faced",
        "it takes two to tango",
        "two-sided",
        "two-step",
        "put two and two together",
        "two sides of the same coin",
        "two-timer"
      ])
    ],
    [
      "chain",
      '\n'.join([
        "chain reaction",
        "chain-link fence",
        "food chain",
        "chain gang",
        "chain of events",
        "ball and chain",
        "chain mail",
        "chainsaw",
        "fast food chain",
        "email chain",
        "yank someone's chain",
        "off the chain"
      ])
    ],
    [
      "break",
      '\n'.join([
        "breakthrough",
        "break a leg",
        "break even",
        "break the cycle",
        "lunch break",
        "break a sweat",
        "break a promise",
        "lucky break",
        "break the bank",
        "icebreaker",
        "break bread",
        "break in",
        "break up",
        "spring break",
        "clean break",
        "break someone's heart"
      ])
    ],
    [
      "king",
      '\n'.join([
        "king bed",
        "king of the hill",
        "king-sized",
        "The Lion King (1994 film)",
        "kingpin",
        "King Kong (fictional character)",
        "fit for a king",
        "king of the jungle",
        "king of spades"
      ])
    ],
    [
      "x",
      '\n'.join([
        "X marks the spot",
        "X-Men (fictional superhero team)",
        "Malcolm X (human rights activist)",
        "X-rated",
        "Generation X (demographic cohort)",
        "X-ray",
        "X-mas (Christmas)",
        "X Games (action sports event)",
        "Xbox (video game console)",
        "Solve for x"
      ])
    ]
  ]
}

def construct_prompt(prompt_components, inputs):
    lines = []
    
    # Some tasks dont have preambles
    if 'preamble' in prompt_components and prompt_components['preamble']:
        lines.append(prompt_components['preamble'])
    
    current_prefix_index = None
    
    # adding the user_input to the examples
    for values in prompt_components['examples'] + [inputs]:
        for i, value in enumerate(values):
            prefix = prompt_components['prefixes'][i] if i < len(prompt_components['prefixes']) else None
            if prefix:
                lines.append(f"{prefix} {value}")
            else:
                lines.append(value)
            current_prefix_index = i
    
    if current_prefix_index is not None and current_prefix_index < len(prompt_components['prefixes']) - 1:
        next_prefix = prompt_components['prefixes'][current_prefix_index + 1]
        if next_prefix:
            lines.append(next_prefix)
    
    return '\n'.join(lines)



