from pymongo import MongoClient
from mongo_client import mongo
# client = MongoClient("mongodb://mongo:27017")

def run_seed():
    db = mongo["comics"]
    if db.heroes.count_documents({}) == 0:
        marvel = [
            # Superhéroes
            {"name": "Iron-Man"             , "real_name": "Tony Stark"         , "year": 1963, "universe": "marvel", "biography": "Inventor y multimillonario que lucha contra el mal con su armadura.", "equipment": ["Armadura", "Reactor ARC"]          , "front_page":"iron-man.jpg"},
            {"name": "Spider-Man"           , "real_name": "Peter Parker"       , "year": 1962, "universe": "marvel", "biography": "Joven con habilidades arácnidas que protege Nueva York."            , "equipment": ["Lanzatelarañas"]                   , "front_page":"spider-man.jpg"},
            {"name": "Captain America"      , "real_name": "Steve Rogers"       , "year": 1941, "universe": "marvel", "biography": "Súper soldado que lucha por la justicia."                           , "equipment": ["Escudo"]                           , "front_page":"capitan_america.jpg"},
            {"name": "Thor"                 , "real_name": "Thor Odinson"       , "year": 1962, "universe": "marvel", "biography": "Dios del trueno, protector de los Nueve Reinos."                    , "equipment": ["Mjolnir"]                          , "front_page":"thor.jpg"},
            {"name": "Black Widow"          , "real_name": "Natasha Romanoff"   , "year": 1964, "universe": "marvel", "biography": "Espía experta y miembro de los Vengadores."                         , "equipment": ["Aguijon electrico"]                , "front_page":"black_widow.jpg"},
            {"name": "Hawkeye"              , "real_name": "Clint Barton"       , "year": 1964, "universe": "marvel", "biography": "Arquero maestro y agente S.H.I.E.L.D."                              , "equipment": ["Arco y flechas"]                   , "front_page":""},
            {"name": "Hulk"                 , "real_name": "Bruce Banner"       , "year": 1962, "universe": "marvel", "biography": "Científico que se convierte en una fuerza imparable."               , "equipment": ["Pantalones"]                       , "front_page":""},
            {"name": "Scarlet Witch"        , "real_name": "Wanda Maximoff"     , "year": 1964, "universe": "marvel", "biography": "Usuaria del caos mágico con gran poder destructivo."                , "equipment": []                                   , "front_page":""},
            {"name": "Doctor Strange"       , "real_name": "Stephen Strange"    , "year": 1963, "universe": "marvel", "biography": "Hechicero supremo y defensor del multiverso."                       , "equipment": ["Ojo de Agamotto"]                  , "front_page":""},
            {"name": "Black Panther"        , "real_name": "T'Challa"           , "year": 1966, "universe": "marvel", "biography": "Rey de Wakanda con traje de vibranium."                             , "equipment": ["Traje", "Tecnología Wakandiana"]   , "front_page":""},

            # Villanos
            {"name": "Loki"                 , "real_name": None                 , "year": 1962, "universe": "marvel", "biography": "Dios del engaño y medio hermano de Thor."                           , "equipment": ["Cetro mágico"]                     , "front_page":""},
            {"name": "Thanos"               , "real_name": None                 , "year": 1973, "universe": "marvel", "biography": "Titán loco que busca el equilibrio universal."                      , "equipment": ["Guantelete del Infinito"]          , "front_page":""},
            {"name": "Ultron"               , "real_name": None                 , "year": 1968, "universe": "marvel", "biography": "IA creada por Tony Stark que se volvió contra la humanidad."        , "equipment": []                                   , "front_page":""},
            {"name": "Green Goblin"         , "real_name": "Norman Osborn"      , "year": 1964, "universe": "marvel", "biography": "Empresario loco con arsenal de calabazas bomba."                    , "equipment": ["Planeador", "Bombas"]              , "front_page":""},
            {"name": "Red Skull"            , "real_name": "Johann Schmidt"     , "year": 1941, "universe": "marvel", "biography": "Archienemigo del Capitán América, líder de Hydra."                  , "equipment": []                                   , "front_page":""},
            {"name": "Kingpin"              , "real_name": "Wilson Fisk"        , "year": 1967, "universe": "marvel", "biography": "Señor del crimen en Nueva York."                                    , "equipment": []                                   , "front_page":""},
            {"name": "Venom"                , "real_name": "Eddie Brock"        , "year": 1988, "universe": "marvel", "biography": "Periodista fusionado con un simbionte alienígena."                  , "equipment": []                                   , "front_page":""},
            {"name": "Killmonger"           , "real_name": "Erik Stevens"       , "year": 1998, "universe": "marvel", "biography": "Exiliado de Wakanda con sed de poder."                              , "equipment": ["Armadura"]                         , "front_page":""},
            {"name": "Hela"                 , "real_name": None                 , "year": 1964, "universe": "marvel", "biography": "Diosa asgardiana de la muerte."                                     , "equipment": ["Espadas del caos"]                 , "front_page":""},
            {"name": "Mystique"             , "real_name": "Raven Darkhölme"    , "year": 1978, "universe": "marvel", "biography": "Mutante cambiaformas peligrosa."                                    , "equipment": []                                   , "front_page":""},
        ]

        dc = [
            # Superhéroes
            {"name": "Batman"               , "real_name": "Bruce Wayne"        , "year": 1939, "universe": "dc"    , "biography": "Millonario que combate el crimen con inteligencia y gadgets."       , "equipment": ["Batsuit", "Batmobile"]             , "front_page":""},
            {"name": "Wonder Woman"         , "real_name": "Diana Prince"       , "year": 1941, "universe": "dc"    , "biography": "Princesa amazona y guerrera inmortal."                              , "equipment": ["Lazo de la verdad", "Brazaletes"]  , "front_page":""},
            {"name": "Green Lantern"        , "real_name": "Hal Jordan"         , "year": 1940, "universe": "dc"    , "biography": "Miembro del cuerpo intergaláctico con anillo de poder."             , "equipment": ["Anillo de poder"]                  , "front_page":""},
            {"name": "Aquaman"              , "real_name": "Arthur Curry"       , "year": 1941, "universe": "dc"    , "biography": "Rey de Atlantis con control del océano."                            , "equipment": ["Tridente"]                         , "front_page":""},
            {"name": "Cyborg"               , "real_name": "Victor Stone"       , "year": 1980, "universe": "dc"    , "biography": "Héroe mitad hombre mitad máquina."                                  , "equipment": ["Tecnología cibernética"]           , "front_page":""},
            {"name": "Green Arrow"          , "real_name": "Oliver Queen"       , "year": 1941, "universe": "dc"    , "biography": "Arquero experto con sentido de justicia social."                    , "equipment": ["Arco y flechas especiales"]        , "front_page":""},
            {"name": "Superman"             , "real_name": "Clark Kent"         , "year": 1938, "universe": "dc"    , "biography": "Hombre de acero defensor de la Tierra."                             , "equipment": []                                   , "front_page":""},
            {"name": "Flash"                , "real_name": "Barry Allen"        , "year": 1956, "universe": "dc"    , "biography": "Héroe más rápido que la luz."                                       , "equipment": []                                   , "front_page":""},
            {"name": "Martian Manhunter"    , "real_name": "J'onn J'onzz"       , "year": 1955, "universe": "dc"    , "biography": "Último sobreviviente de Marte."                                     , "equipment": []                                   , "front_page":""},
            {"name": "Shazam"               , "real_name": "Billy Batson"       , "year": 1939, "universe": "dc"    , "biography": "Niño que se transforma en un superhéroe adulto."                    , "equipment": []                                   , "front_page":""},

            # Villanos
            {"name": "Joker"                , "real_name": None                 , "year": 1940, "universe": "dc"    , "biography": "Maníaco del caos y archienemigo de Batman."                         , "equipment": ["Gas de la risa"]                   , "front_page":""},
            {"name": "Lex Luthor"           , "real_name": None                 , "year": 1940, "universe": "dc"    , "biography": "Genio multimillonario enemigo de Superman."                         , "equipment": ["Traje de poder"]                   , "front_page":""},
            {"name": "Harley Quinn"         , "real_name": "Harleen Quinzel"    , "year": 1992, "universe": "dc"    , "biography": "Ex psiquiatra con comportamiento impredecible."                     , "equipment": ["Martillo"]                         , "front_page":""},
            {"name": "Deathstroke"          , "real_name": "Slade Wilson"       , "year": 1980, "universe": "dc"    , "biography": "Asesino a sueldo mejorado físicamente."                             , "equipment": ["Espada", "Armas de fuego"]         , "front_page":""},
            {"name": "Two-Face"             , "real_name": "Harvey Dent"        , "year": 1942, "universe": "dc"    , "biography": "Fiscal convertido en criminal tras un accidente."                   , "equipment": ["Moneda"]                           , "front_page":""},
            {"name": "Bane"                 , "real_name": None                 , "year": 1993, "universe": "dc"    , "biography": "Brutal enemigo de Batman con fuerza sobrehumana."                   , "equipment": ["Veneno"]                           , "front_page":""},
            {"name": "Darkseid"             , "real_name": None                 , "year": 1970, "universe": "dc"    , "biography": "Tirano de Apokolips que busca la ecuación antivida."                , "equipment": []                                   , "front_page":""},
            {"name": "Riddler"              , "real_name": "Edward Nigma"       , "year": 1948, "universe": "dc"    , "biography": "Criminal obsesionado con acertijos."                                , "equipment": []                                   , "front_page":""},
            {"name": "Reverse Flash"        , "real_name": "Eobard Thawne"      , "year": 1963, "universe": "dc"    , "biography": "Némesis del Flash con poderes similares."                           , "equipment": []                                   , "front_page":""},
            {"name": "Black Adam"           , "real_name": "Teth-Adam"          , "year": 1945, "universe": "dc"    , "biography": "Anti-héroe poderoso con orígenes mágicos."                          , "equipment": []                                   , "front_page":""},
        ]

        db.heroes.insert_many(marvel + dc)
        print("Héroes cargados.")
    else:
        print("Ya existen héroes.")
