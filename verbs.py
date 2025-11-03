import random

verbs = {
    "etre": {
        "present": ["je suis", "tu es", "il est", "nous sommes", "vous etes", "ils sont"],
        "futur simple": ["je serai", "tu seras", "il sera", "nous serons", "vous serez", "ils seront"],
        "passe compose": ["j'ai ete", "tu as ete", "il a ete", "nous avons ete", "vous avez ete", "ils ont ete"],
        "imparfait": ["j'etais", "tu etais", "il etait", "nous etions", "vous etiez", "ils etaient"],
        "conditionnel": ["je serais", "tu serais", "il serait", "nous serions", "vous seriez", "ils seraient"]
    },
    "avoir": {
        "present": ["j'ai", "tu as", "il a", "nous avons", "vous avez", "ils ont"],
        "futur simple": ["j'aurai", "tu auras", "il aura", "nous aurons", "vous aurez", "ils auront"],
        "passe compose": ["j'ai eu", "tu as eu", "il a eu", "nous avons eu", "vous avez eu", "ils ont eu"],
        "imparfait": ["j'avais", "tu avais", "il avait", "nous avions", "vous aviez", "ils avaient"],
        "conditionnel": ["j'aurais", "tu aurais", "il aurait", "nous aurions", "vous auriez", "ils auraient"]
    },
    "aller": {
        "present": ["je vais", "tu vas", "il va", "nous allons", "vous allez", "ils vont"],
        "futur simple": ["j'irai", "tu iras", "il ira", "nous irons", "vous irez", "ils iront"],
        "passe compose": ["je suis alle", "tu es alle", "il est alle", "nous sommes alles", "vous etes alles", "ils sont alles"],
        "imparfait": ["j'allais", "tu allais", "il allait", "nous allions", "vous alliez", "ils allaient"],
        "conditionnel": ["j'irais", "tu irais", "il irait", "nous irions", "vous iriez", "ils iraient"]
    },
    "venir": {
        "present": ["je viens", "tu viens", "il vient", "nous venons", "vous venez", "ils viennent"],
        "futur simple": ["je viendrai", "tu viendras", "il viendra", "nous viendrons", "vous viendrez", "ils viendront"],
        "passe compose": ["je suis venu", "tu es venu", "il est venu", "nous sommes venus", "vous etes venus", "ils sont venus"],
        "imparfait": ["je venais", "tu venais", "il venait", "nous venions", "vous veniez", "ils venaient"],
        "conditionnel": ["je viendrais", "tu viendrais", "il viendrait", "nous viendrions", "vous viendriez", "ils viendraient"]
    },
    "prendre": {
        "present": ["je prends", "tu prends", "il prend", "nous prenons", "vous prenez", "ils prennent"],
        "futur simple": ["je prendrai", "tu prendras", "il prendra", "nous prendrons", "vous prendrez", "ils prendront"],
        "passe compose": ["j'ai pris", "tu as pris", "il a pris", "nous avons pris", "vous avez pris", "ils ont pris"],
        "imparfait": ["je prenais", "tu prenais", "il prenait", "nous prenions", "vous preniez", "ils prenaient"],
        "conditionnel": ["je prendrais", "tu prendrais", "il prendrait", "nous prendrions", "vous prendriez", "ils prendraient"]
    },
    "partir": {
        "present": ["je pars", "tu pars", "il part", "nous partons", "vous partez", "ils partent"],
        "futur simple": ["je partirai", "tu partiras", "il partira", "nous partirons", "vous partirez", "ils partiront"],
        "passe compose": ["je suis parti", "tu es parti", "il est parti", "nous sommes partis", "vous etes partis", "ils sont partis"],
        "imparfait": ["je partais", "tu partais", "il partait", "nous partions", "vous partiez", "ils partaient"],
        "conditionnel": ["je partirais", "tu partirais", "il partirait", "nous partirions", "vous partiriez", "ils partiraient"]
    },
    "voir": {
        "present": ["je vois", "tu vois", "il voit", "nous voyons", "vous voyez", "ils voient"],
        "futur simple": ["je verrai", "tu verras", "il verra", "nous verrons", "vous verrez", "ils verront"],
        "passe compose": ["j'ai vu", "tu as vu", "il a vu", "nous avons vu", "vous avez vu", "ils ont vu"],
        "imparfait": ["je voyais", "tu voyais", "il voyait", "nous voyions", "vous voyiez", "ils voyaient"],
        "conditionnel": ["je verrais", "tu verrais", "il verrait", "nous verrions", "vous verriez", "ils verraient"]
    },
    "faire": {
        "present": ["je fais", "tu fais", "il fait", "nous faisons", "vous faites", "ils font"],
        "futur simple": ["je ferai", "tu feras", "il fera", "nous ferons", "vous ferez", "ils feront"],
        "passe compose": ["j'ai fait", "tu as fait", "il a fait", "nous avons fait", "vous avez fait", "ils ont fait"],
        "imparfait": ["je faisais", "tu faisais", "il faisait", "nous faisions", "vous faisiez", "ils faisaient"],
        "conditionnel": ["je ferais", "tu ferais", "il ferait", "nous ferions", "vous feriez", "ils feraient"]
    },
    "dire": {
        "present": ["je dis", "tu dis", "il dit", "nous disons", "vous dites", "ils disent"],
        "futur simple": ["je dirai", "tu diras", "il dira", "nous dirons", "vous direz", "ils diront"],
        "passe compose": ["j'ai dit", "tu as dit", "il a dit", "nous avons dit", "vous avez dit", "ils ont dit"],
        "imparfait": ["je disais", "tu disais", "il disait", "nous disions", "vous disiez", "ils disaient"],
        "conditionnel": ["je dirais", "tu dirais", "il dirait", "nous dirions", "vous diriez", "ils diraient"]
    },
    "pouvoir": {
        "present": ["je peux", "tu peux", "il peut", "nous pouvons", "vous pouvez", "ils peuvent"],
        "futur simple": ["je pourrai", "tu pourras", "il pourra", "nous pourrons", "vous pourrez", "ils pourront"],
        "passe compose": ["j'ai pu", "tu as pu", "il a pu", "nous avons pu", "vous avez pu", "ils ont pu"],
        "imparfait": ["je pouvais", "tu pouvais", "il pouvait", "nous pouvions", "vous pouviez", "ils pouvaient"],
        "conditionnel": ["je pourrais", "tu pourrais", "il pourrait", "nous pourrions", "vous pourriez", "ils pourraient"]
    },
    "vouloir": {
        "present": ["je veux", "tu veux", "il veut", "nous voulons", "vous voulez", "ils veulent"],
        "futur simple": ["je voudrai", "tu voudras", "il voudra", "nous voudrons", "vous voudrez", "ils voudront"],
        "passe compose": ["j'ai voulu", "tu as voulu", "il a voulu", "nous avons voulu", "vous avez voulu", "ils ont voulu"],
        "imparfait": ["je voulais", "tu voulais", "il voulait", "nous voulions", "vous vouliez", "ils voulaient"],
        "conditionnel": ["je voudrais", "tu voudrais", "il voudrait", "nous voudrions", "vous voudriez", "ils voudraient"]
    },
    "savoir": {
        "present": ["je sais", "tu sais", "il sait", "nous savons", "vous savez", "ils savent"],
        "futur simple": ["je saurai", "tu sauras", "il saura", "nous saurons", "vous saurez", "ils sauront"],
        "passe compose": ["j'ai su", "tu as su", "il a su", "nous avons su", "vous avez su", "ils ont su"],
        "imparfait": ["je savais", "tu savais", "il savait", "nous savions", "vous saviez", "ils savaient"],
        "conditionnel": ["je saurais", "tu saurais", "il saurait", "nous saurions", "vous sauriez", "ils sauraient"]
    },
    "rentrer": {
        "present": ["je rentre", "tu rentres", "il rentre", "nous rentrons", "vous rentrez", "ils rentrent"],
        "futur simple": ["je rentrerai", "tu rentreras", "il rentrera", "nous rentrerons", "vous rentrerez", "ils rentreront"],
        "passe compose": ["je suis rentre", "tu es rentre", "il est rentre", "nous sommes rentres", "vous etes rentres", "ils sont rentres"],
        "imparfait": ["je rentrais", "tu rentrais", "il rentrait", "nous rentrions", "vous rentriez", "ils rentraient"],
        "conditionnel": ["je rentrerais", "tu rentrerais", "il rentrerait", "nous rentrerions", "vous rentreriez", "ils rentreraient"]
    },
    "manger": {
        "present": ["je mange", "tu manges", "il mange", "nous mangeons", "vous mangez", "ils mangent"],
        "futur simple": ["je mangerai", "tu mangeras", "il mangera", "nous mangerons", "vous mangerez", "ils mangeront"],
        "passe compose": ["j'ai mange", "tu as mange", "il a mange", "nous avons mange", "vous avez mange", "ils ont mange"],
        "imparfait": ["je mangeais", "tu mangeais", "il mangeait", "nous mangions", "vous mangiez", "ils mangeaient"],
        "conditionnel": ["je mangerais", "tu mangerais", "il mangerait", "nous mangerions", "vous mangeriez", "ils mangeraient"]
    },
    "aimer": {
        "present": ["j'aime", "tu aimes", "il aime", "nous aimons", "vous aimez", "ils aiment"],
        "futur simple": ["j'aimerai", "tu aimeras", "il aimera", "nous aimerons", "vous aimerez", "ils aimeront"],
        "passe compose": ["j'ai aime", "tu as aime", "il a aime", "nous avons aime", "vous avez aime", "ils ont aime"],
        "imparfait": ["j'aimais", "tu aimais", "il aimait", "nous aimions", "vous aimiez", "ils aimaient"],
        "conditionnel": ["j'aimerais", "tu aimerais", "il aimerait", "nous aimerions", "vous aimeriez", "ils aimeraient"]
    },
    "finir": {
        "present": ["je finis", "tu finis", "il finit", "nous finissons", "vous finissez", "ils finissent"],
        "futur simple": ["je finirai", "tu finiras", "il finira", "nous finirons", "vous finirez", "ils finiront"],
        "passe compose": ["j'ai fini", "tu as fini", "il a fini", "nous avons fini", "vous avez fini", "ils ont fini"],
        "imparfait": ["je finissais", "tu finissais", "il finissait", "nous finissions", "vous finissiez", "ils finissaient"],
        "conditionnel": ["je finirais", "tu finirais", "il finirait", "nous finirions", "vous finiriez", "ils finiraient"]
    },
    "devoir": {
        "present": ["je dois", "tu dois", "il doit", "nous devons", "vous devez", "ils doivent"],
        "futur simple": ["je devrai", "tu devras", "il devra", "nous devrons", "vous devrez", "ils devront"],
        "passe compose": ["j'ai du", "tu as du", "il a du", "nous avons du", "vous avez du", "ils ont du"],
        "imparfait": ["je devais", "tu devais", "il devait", "nous devions", "vous deviez", "ils devaient"],
        "conditionnel": ["je devrais", "tu devrais", "il devrait", "nous devrions", "vous devriez", "ils devraient"]
    },
    "regarder": {
        "present": ["je regarde", "tu regardes", "il regarde", "nous regardons", "vous regardez", "ils regardent"],
        "futur simple": ["je regarderai", "tu regarderas", "il regardera", "nous regarderons", "vous regarderez", "ils regarderont"],
        "passe compose": ["j'ai regarde", "tu as regarde", "il a regarde", "nous avons regarde", "vous avez regarde", "ils ont regarde"],
        "imparfait": ["je regardais", "tu regardais", "il regardait", "nous regardions", "vous regardiez", "ils regardaient"],
        "conditionnel": ["je regarderais", "tu regarderais", "il regarderait", "nous regarderions", "vous regarderiez", "ils regarderaient"]
    },
    "ecouter": {
        "present": ["j'ecoute", "tu ecoutes", "il ecoute", "nous ecoutons", "vous ecoutez", "ils ecoutent"],
        "futur simple": ["j'ecouterai", "tu ecouteras", "il ecoutera", "nous ecouterons", "vous ecouterez", "ils ecouteront"],
        "passe compose": ["j'ai ecoute", "tu as ecoute", "il a ecoute", "nous avons ecoute", "vous avez ecoute", "ils ont ecoute"],
        "imparfait": ["j'ecoutais", "tu ecoutais", "il ecoutait", "nous ecoutions", "vous ecoutiez", "ils ecoutaient"],
        "conditionnel": ["j'ecouterais", "tu ecouterais", "il ecouterait", "nous ecouterions", "vous ecouteriez", "ils ecouteraient"]
    },
    "donner": {
        "present": ["je donne", "tu donnes", "il donne", "nous donnons", "vous donnez", "ils donnent"],
        "futur simple": ["je donnerai", "tu donneras", "il donnera", "nous donnerons", "vous donnerez", "ils donneront"],
        "passe compose": ["j'ai donne", "tu as donne", "il a donne", "nous avons donne", "vous avez donne", "ils ont donne"],
        "imparfait": ["je donnais", "tu donnais", "il donnait", "nous donnions", "vous donniez", "ils donnaient"],
        "conditionnel": ["je donnerais", "tu donnerais", "il donnerait", "nous donnerions", "vous donneriez", "ils donneraient"]
    },
    "chercher": {
        "present": ["je cherche", "tu cherches", "il cherche", "nous cherchons", "vous cherchez", "ils cherchent"],
        "futur simple": ["je chercherai", "tu chercheras", "il cherchera", "nous chercherons", "vous chercherez", "ils chercheront"],
        "passe compose": ["j'ai cherche", "tu as cherche", "il a cherche", "nous avons cherche", "vous avez cherche", "ils ont cherche"],
        "imparfait": ["je cherchais", "tu cherchais", "il cherchait", "nous cherchions", "vous cherchiez", "ils cherchaient"],
        "conditionnel": ["je chercherais", "tu chercherais", "il chercherait", "nous chercherions", "vous chercheriez", "ils chercheraient"]
    },
    "trouver": {
        "present": ["je trouve", "tu trouves", "il trouve", "nous trouvons", "vous trouvez", "ils trouvent"],
        "futur simple": ["je trouverai", "tu trouveras", "il trouvera", "nous trouverons", "vous trouverez", "ils trouveront"],
        "passe compose": ["j'ai trouve", "tu as trouve", "il a trouve", "nous avons trouve", "vous avez trouve", "ils ont trouve"],
        "imparfait": ["je trouvais", "tu trouvais", "il trouvait", "nous trouvions", "vous trouviez", "ils trouvaient"],
        "conditionnel": ["je trouverais", "tu trouverais", "il trouverait", "nous trouverions", "vous trouveriez", "ils trouveraient"]
    },
    "lire": {
        "present": ["je lis", "tu lis", "il lit", "nous lisons", "vous lisez", "ils lisent"],
        "futur simple": ["je lirai", "tu liras", "il lira", "nous lirons", "vous lirez", "ils liront"],
        "passe compose": ["j'ai lu", "tu as lu", "il a lu", "nous avons lu", "vous avez lu", "ils ont lu"],
        "imparfait": ["je lisais", "tu lisais", "il lisait", "nous lisions", "vous lisiez", "ils lisaient"],
        "conditionnel": ["je lirais", "tu lirais", "il lirait", "nous lirions", "vous liriez", "ils liraient"]
    },
    "ecrire": {
        "present": ["j'ecris", "tu ecris", "il ecrit", "nous ecrivons", "vous ecrivez", "ils ecrivent"],
        "futur simple": ["j'ecrirai", "tu ecriras", "il ecrira", "nous ecrirons", "vous ecrirez", "ils ecriront"],
        "passe compose": ["j'ai ecrit", "tu as ecrit", "il a ecrit", "nous avons ecrit", "vous avez ecrit", "ils ont ecrit"],
        "imparfait": ["j'ecrivais", "tu ecrivais", "il ecrivait", "nous ecrivions", "vous ecriviez", "ils ecrivaient"],
        "conditionnel": ["j'ecrirais", "tu ecrirais", "il ecrirait", "nous ecririons", "vous ecririez", "ils ecriraient"]
    },
    "comprendre": {
        "present": ["je comprends", "tu comprends", "il comprend", "nous comprenons", "vous comprenez", "ils comprennent"],
        "futur simple": ["je comprendrai", "tu comprendras", "il comprendra", "nous comprendrons", "vous comprendrez", "ils comprendront"],
        "passe compose": ["j'ai compris", "tu as compris", "il a compris", "nous avons compris", "vous avez compris", "ils ont compris"],
        "imparfait": ["je comprenais", "tu comprenais", "il comprenait", "nous comprenions", "vous compreniez", "ils comprenaient"],
        "conditionnel": ["je comprendrais", "tu comprendrais", "il comprendrait", "nous comprendrions", "vous comprendriez", "ils comprendraient"]
    },
    "croire": {
        "present": ["je crois", "tu crois", "il croit", "nous croyons", "vous croyez", "ils croient"],
        "futur simple": ["je croirai", "tu croiras", "il croira", "nous croirons", "vous croirez", "ils croiront"],
        "passe compose": ["j'ai cru", "tu as cru", "il a cru", "nous avons cru", "vous avez cru", "ils ont cru"],
        "imparfait": ["je croyais", "tu croyais", "il croyait", "nous croyions", "vous croyiez", "ils croyaient"],
        "conditionnel": ["je croirais", "tu croirais", "il croirait", "nous croirions", "vous croiriez", "ils croiraient"]
    },
    "mettre": {
        "present": ["je mets", "tu mets", "il met", "nous mettons", "vous mettez", "ils mettent"],
        "futur simple": ["je mettrai", "tu mettras", "il mettra", "nous mettrons", "vous mettrez", "ils mettront"],
        "passe compose": ["j'ai mis", "tu as mis", "il a mis", "nous avons mis", "vous avez mis", "ils ont mis"],
        "imparfait": ["je mettais", "tu mettais", "il mettait", "nous mettions", "vous mettiez", "ils mettaient"],
        "conditionnel": ["je mettrais", "tu mettrais", "il mettrait", "nous mettrions", "vous mettriez", "ils mettraient"]
    }
}

persons = ['je', 'tu', 'il', 'nous', 'vous', 'ils']
tenses = ['present', 'futur simple', 'passe compose', 'imparfait', 'conditionnel']

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
