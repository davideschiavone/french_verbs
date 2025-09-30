import random

verbs = {
    "etre": {
        "presente": ["je suis", "tu es", "il est", "nous sommes", "vous etes", "ils sont"],
        "futuro": ["je serai", "tu seras", "il sera", "nous serons", "vous serez", "ils seront"],
        "passe": ["j'ai ete", "tu as ete", "il a ete", "nous avons ete", "vous avez ete", "ils ont ete"]
    },
    "avoir": {
        "presente": ["j'ai", "tu as", "il a", "nous avons", "vous avez", "ils ont"],
        "futuro": ["j'aurai", "tu auras", "il aura", "nous aurons", "vous aurez", "ils auront"],
        "passe": ["j'ai eu", "tu as eu", "il a eu", "nous avons eu", "vous avez eu", "ils ont eu"]
    },
    "aller": {
        "presente": ["je vais", "tu vas", "il va", "nous allons", "vous allez", "ils vont"],
        "futuro": ["j'irai", "tu iras", "il ira", "nous irons", "vous irez", "ils iront"],
        "passe": ["je suis alle", "tu es alle", "il est alle", "nous sommes alles", "vous etes alles", "ils sont alles"]
    },
    "venir": {
        "presente": ["je viens", "tu viens", "il vient", "nous venons", "vous venez", "ils viennent"],
        "futuro": ["je viendrai", "tu viendras", "il viendra", "nous viendrons", "vous viendrez", "ils viendront"],
        "passe": ["je suis venu", "tu es venu", "il est venu", "nous sommes venus", "vous etes venus", "ils sont venus"]
    },
    "prendre": {
        "presente": ["je prends", "tu prends", "il prend", "nous prenons", "vous prenez", "ils prennent"],
        "futuro": ["je prendrai", "tu prendras", "il prendra", "nous prendrons", "vous prendrez", "ils prendront"],
        "passe": ["j'ai pris", "tu as pris", "il a pris", "nous avons pris", "vous avez pris", "ils ont pris"]
    },
    "partir": {
        "presente": ["je pars", "tu pars", "il part", "nous partons", "vous partez", "ils partent"],
        "futuro": ["je partirai", "tu partiras", "il partira", "nous partirons", "vous partirez", "ils partiront"],
        "passe": ["je suis parti", "tu es parti", "il est parti", "nous sommes partis", "vous etes partis", "ils sont partis"]
    },
    "voir": {
        "presente": ["je vois", "tu vois", "il voit", "nous voyons", "vous voyez", "ils voient"],
        "futuro": ["je verrai", "tu verras", "il verra", "nous verrons", "vous verrez", "ils verront"],
        "passe": ["j'ai vu", "tu as vu", "il a vu", "nous avons vu", "vous avez vu", "ils ont vu"]
    },
    "faire": {
        "presente": ["je fais", "tu fais", "il fait", "nous faisons", "vous faites", "ils font"],
        "futuro": ["je ferai", "tu feras", "il fera", "nous ferons", "vous ferez", "ils feront"],
        "passe": ["j'ai fait", "tu as fait", "il a fait", "nous avons fait", "vous avez fait", "ils ont fait"]
    },
    "dire": {
        "presente": ["je dis", "tu dis", "il dit", "nous disons", "vous dites", "ils disent"],
        "futuro": ["je dirai", "tu diras", "il dira", "nous dirons", "vous direz", "ils diront"],
        "passe": ["j'ai dit", "tu as dit", "il a dit", "nous avons dit", "vous avez dit", "ils ont dit"]
    },
    "pouvoir": {
        "presente": ["je peux", "tu peux", "il peut", "nous pouvons", "vous pouvez", "ils peuvent"],
        "futuro": ["je pourrai", "tu pourras", "il pourra", "nous pourrons", "vous pourrez", "ils pourront"],
        "passe": ["j'ai pu", "tu as pu", "il a pu", "nous avons pu", "vous avez pu", "ils ont pu"]
    },
    "vouloir": {
        "presente": ["je veux", "tu veux", "il veut", "nous voulons", "vous voulez", "ils veulent"],
        "futuro": ["je voudrai", "tu voudras", "il voudra", "nous voudrons", "vous voudrez", "ils voudront"],
        "passe": ["j'ai voulu", "tu as voulu", "il a voulu", "nous avons voulu", "vous avez voulu", "ils ont voulu"]
    },
    "savoir": {
        "presente": ["je sais", "tu sais", "il sait", "nous savons", "vous savez", "ils savent"],
        "futuro": ["je saurai", "tu sauras", "il saura", "nous saurons", "vous saurez", "ils sauront"],
        "passe": ["j'ai su", "tu as su", "il a su", "nous avons su", "vous avez su", "ils ont su"]
    },
    "rentrer": {
        "presente": ["je rentre", "tu rentres", "il rentre", "nous rentrons", "vous rentrez", "ils rentrent"],
        "futuro": ["je rentrerai", "tu rentreras", "il rentrera", "nous rentrerons", "vous rentrerez", "ils rentreront"],
        "passe": ["je suis rentre", "tu es rentre", "il est rentre", "nous sommes rentres", "vous etes rentres", "ils sont rentres"]
    },
    "manger": {
        "presente": ["je mange", "tu manges", "il mange", "nous mangeons", "vous mangez", "ils mangent"],
        "futuro": ["je mangerai", "tu mangeras", "il mangera", "nous mangerons", "vous mangerez", "ils mangeront"],
        "passe": ["j'ai mange", "tu as mange", "il a mange", "nous avons mange", "vous avez mange", "ils ont mange"]
    },
    "aimer": {
        "presente": ["j'aime", "tu aimes", "il aime", "nous aimons", "vous aimez", "ils aiment"],
        "futuro": ["j'aimerai", "tu aimeras", "il aimera", "nous aimerons", "vous aimerez", "ils aimeront"],
        "passe": ["j'ai aime", "tu as aime", "il a aime", "nous avons aime", "vous avez aime", "ils ont aime"]
    }
}

persons = ['je', 'tu', 'il', 'nous', 'vous', 'ils']
tenses = ['presente', 'futuro', 'passe']

def generate_question_deck():
    deck = []
    for verb in verbs:
        for tense in tenses:
            for idx, person in enumerate(persons):
                deck.append({
                    'verb': verb,
                    'tense': tense,
                    'person': person,
                    'answer': verbs[verb][tense][idx]
                })
    random.shuffle(deck)
    return deck

def conjugation_game():
    score = 0
    errors = 0
    questions = 0
    deck = generate_question_deck()

    print("Giochino di coniugazione francese. Scrivi STOP per uscire.")
    while True:
        if not deck:
                print(f"Hai completato il gioco con punteggio {score}. Complimenti!")
                print(f"Hai commesso {errors} errori in {questions} domande.")
                deck = generate_question_deck()
                print("Mazzo di domande ricaricato.")
        q = deck.pop()
        questions += 1
        print(f"Domande rimanenti nel mazzo: {len(deck)}")
        guess = input(f"Coniuga il verbo '{q['verb']}' per la persona '{q['person']}' al tempo '{q['tense']}'. Risposta? ").strip().lower()
        if guess.upper() == 'STOP':
            print(f"Hai terminato il gioco con punteggio {score}.")
            break
        if guess == q['answer'].lower():
            score += 1
            print(f"Risposta corretta! Punteggio: {score}")
        else:
            score -= 1
            errors += 1
            print(f"Sbagliato! La risposta corretta è: {q['answer']}. Punteggio: {score}")
            deck.insert(errors-1, q)



conjugation_game()
