import random

verbs = {
    "etre": {
        "present": ["je suis", "tu es", "il est", "nous sommes", "vous etes", "ils sont"],
        "futur simple": ["je serai", "tu seras", "il sera", "nous serons", "vous serez", "ils seront"],
        "passe compose": ["j'ai ete", "tu as ete", "il a ete", "nous avons ete", "vous avez ete", "ils ont ete"],
        "imparfait": ["j'etais", "tu etais", "il etait", "nous etions", "vous etiez", "ils etaient"]
    },
    "avoir": {
        "present": ["j'ai", "tu as", "il a", "nous avons", "vous avez", "ils ont"],
        "futur simple": ["j'aurai", "tu auras", "il aura", "nous aurons", "vous aurez", "ils auront"],
        "passe compose": ["j'ai eu", "tu as eu", "il a eu", "nous avons eu", "vous avez eu", "ils ont eu"],
        "imparfait": ["j'avais", "tu avais", "il avait", "nous avions", "vous aviez", "ils avaient"]
    },
    "aller": {
        "present": ["je vais", "tu vas", "il va", "nous allons", "vous allez", "ils vont"],
        "futur simple": ["j'irai", "tu iras", "il ira", "nous irons", "vous irez", "ils iront"],
        "passe compose": ["je suis alle", "tu es alle", "il est alle", "nous sommes alles", "vous etes alles", "ils sont alles"],
        "imparfait": ["j'allais", "tu allais", "il allait", "nous allions", "vous alliez", "ils allaient"]
    },
    "venir": {
        "present": ["je viens", "tu viens", "il vient", "nous venons", "vous venez", "ils viennent"],
        "futur simple": ["je viendrai", "tu viendras", "il viendra", "nous viendrons", "vous viendrez", "ils viendront"],
        "passe compose": ["je suis venu", "tu es venu", "il est venu", "nous sommes venus", "vous etes venus", "ils sont venus"],
        "imparfait": ["je venais", "tu venais", "il venait", "nous venions", "vous veniez", "ils venaient"]
    },
    "prendre": {
        "present": ["je prends", "tu prends", "il prend", "nous prenons", "vous prenez", "ils prennent"],
        "futur simple": ["je prendrai", "tu prendras", "il prendra", "nous prendrons", "vous prendrez", "ils prendront"],
        "passe compose": ["j'ai pris", "tu as pris", "il a pris", "nous avons pris", "vous avez pris", "ils ont pris"],
        "imparfait": ["je prenais", "tu prenais", "il prenait", "nous prenions", "vous preniez", "ils prenaient"]
    },
    "partir": {
        "present": ["je pars", "tu pars", "il part", "nous partons", "vous partez", "ils partent"],
        "futur simple": ["je partirai", "tu partiras", "il partira", "nous partirons", "vous partirez", "ils partiront"],
        "passe compose": ["je suis parti", "tu es parti", "il est parti", "nous sommes partis", "vous etes partis", "ils sont partis"],
        "imparfait": ["je partais", "tu partais", "il partait", "nous partions", "vous partiez", "ils partaient"]
    },
    "voir": {
        "present": ["je vois", "tu vois", "il voit", "nous voyons", "vous voyez", "ils voient"],
        "futur simple": ["je verrai", "tu verras", "il verra", "nous verrons", "vous verrez", "ils verront"],
        "passe compose": ["j'ai vu", "tu as vu", "il a vu", "nous avons vu", "vous avez vu", "ils ont vu"],
        "imparfait": ["je voyais", "tu voyais", "il voyait", "nous voyions", "vous voyiez", "ils voyaient"]
    },
    "faire": {
        "present": ["je fais", "tu fais", "il fait", "nous faisons", "vous faites", "ils font"],
        "futur simple": ["je ferai", "tu feras", "il fera", "nous ferons", "vous ferez", "ils feront"],
        "passe compose": ["j'ai fait", "tu as fait", "il a fait", "nous avons fait", "vous avez fait", "ils ont fait"],
        "imparfait": ["je faisais", "tu faisais", "il faisait", "nous faisions", "vous faisiez", "ils faisaient"]
    },
    "dire": {
        "present": ["je dis", "tu dis", "il dit", "nous disons", "vous dites", "ils disent"],
        "futur simple": ["je dirai", "tu diras", "il dira", "nous dirons", "vous direz", "ils diront"],
        "passe compose": ["j'ai dit", "tu as dit", "il a dit", "nous avons dit", "vous avez dit", "ils ont dit"],
        "imparfait": ["je disais", "tu disais", "il disait", "nous disions", "vous disiez", "ils disaient"]
    },
    "pouvoir": {
        "present": ["je peux", "tu peux", "il peut", "nous pouvons", "vous pouvez", "ils peuvent"],
        "futur simple": ["je pourrai", "tu pourras", "il pourra", "nous pourrons", "vous pourrez", "ils pourront"],
        "passe compose": ["j'ai pu", "tu as pu", "il a pu", "nous avons pu", "vous avez pu", "ils ont pu"],
        "imparfait": ["je pouvais", "tu pouvais", "il pouvait", "nous pouvions", "vous pouviez", "ils pouvaient"]
    },
    "vouloir": {
        "present": ["je veux", "tu veux", "il veut", "nous voulons", "vous voulez", "ils veulent"],
        "futur simple": ["je voudrai", "tu voudras", "il voudra", "nous voudrons", "vous voudrez", "ils voudront"],
        "passe compose": ["j'ai voulu", "tu as voulu", "il a voulu", "nous avons voulu", "vous avez voulu", "ils ont voulu"],
        "imparfait": ["je voulais", "tu voulais", "il voulait", "nous voulions", "vous vouliez", "ils voulaient"]
    },
    "savoir": {
        "present": ["je sais", "tu sais", "il sait", "nous savons", "vous savez", "ils savent"],
        "futur simple": ["je saurai", "tu sauras", "il saura", "nous saurons", "vous saurez", "ils sauront"],
        "passe compose": ["j'ai su", "tu as su", "il a su", "nous avons su", "vous avez su", "ils ont su"],
        "imparfait": ["je savais", "tu savais", "il savait", "nous savions", "vous saviez", "ils savaient"]
    },
    "rentrer": {
        "present": ["je rentre", "tu rentres", "il rentre", "nous rentrons", "vous rentrez", "ils rentrent"],
        "futur simple": ["je rentrerai", "tu rentreras", "il rentrera", "nous rentrerons", "vous rentrerez", "ils rentreront"],
        "passe compose": ["je suis rentre", "tu es rentre", "il est rentre", "nous sommes rentres", "vous etes rentres", "ils sont rentres"],
        "imparfait": ["je rentrais", "tu rentrais", "il rentrait", "nous rentrions", "vous rentriez", "ils rentraient"]
    },
    "manger": {
        "present": ["je mange", "tu manges", "il mange", "nous mangeons", "vous mangez", "ils mangent"],
        "futur simple": ["je mangerai", "tu mangeras", "il mangera", "nous mangerons", "vous mangerez", "ils mangeront"],
        "passe compose": ["j'ai mange", "tu as mange", "il a mange", "nous avons mange", "vous avez mange", "ils ont mange"],
        "imparfait": ["je mangeais", "tu mangeais", "il mangeait", "nous mangions", "vous mangiez", "ils mangeaient"]
    },
    "aimer": {
        "present": ["j'aime", "tu aimes", "il aime", "nous aimons", "vous aimez", "ils aiment"],
        "futur simple": ["j'aimerai", "tu aimeras", "il aimera", "nous aimerons", "vous aimerez", "ils aimeront"],
        "passe compose": ["j'ai aime", "tu as aime", "il a aime", "nous avons aime", "vous avez aime", "ils ont aime"],
        "imparfait": ["j'aimais", "tu aimais", "il aimait", "nous aimions", "vous aimiez", "ils aimaient"]
    }
}

persons = ['je', 'tu', 'il', 'nous', 'vous', 'ils']
tenses = ['present', 'futur simple', 'passe compose', 'imparfait']

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

    print("Little French Verb Conjugation Game! -- Type 'STOP' to end the game.")
    while True:
        if not deck:
                print(f"You completed the game with a score of {score}. Congratulations!")
                print(f"You made {errors} errors out of {questions} questions.")
                deck = generate_question_deck()
                print("Deck reloaded.")
        q = deck.pop()
        questions += 1
        print(f"Questions remaining in the deck: {len(deck)}")
        guess = input(f"Conjugate '{q['verb']}' for the person '{q['person']}' in the tense '{q['tense']}'. Answer? ").strip().lower()
        if guess.upper() == 'STOP':
            print(f"You ended the game with a score of {score}.")
            break
        if guess == q['answer'].lower():
            score += 1
            print(f"Correct answer! Score: {score}")
        else:
            score -= 1
            errors += 1
            print(f"Wrong! The correct answer is: {q['answer']}. Score: {score}")
            deck.insert(errors-1, q)



conjugation_game()
