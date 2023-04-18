import discord 
import nest_asyncio 
nest_asyncio.apply()
from discord.ui import Button, View
from discord.ext import commands


intents = discord.Intents.all()
intents.messages = True
intents.members = True
intents.typing = True
client = discord.Client(intents=intents)

score = 0


@client.event
async def on_ready():
    print("Le bot est connecté.")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    global score

    message.content = message.content.lower()


    if message.content.startswith("!bot"):
      await message.channel.send("```Bonjour et bienvenue, vous avez lancé le bot Botblebee qui a été créé par Lucas YALMAN et Mohamed YAICH.\n\nVous avez accès à un quiz pour cela, vous avez à disposition la commande !fr pour lancer en français ou alors !en pour lancer le jeu en anglais.```\nhttps://media.tenor.com/Xw9NRtyNMb4AAAAC/simpson.gif")

    # LANCEMENT QUIZZ

    if message.content.startswith("!en"):
        await message.channel.send("```Welcome to Botblebee\nYou have the possibility to experiment 3 levels easy, medium and hard, your goal is to obtain as many points as you can !\n \n \nCOMMANDS LIST:\n\n!game to start the quiz.\n!fr to change the language to french.\n!help if you’re just struggling (Warning : !help is just available for level 1).\n!mypoints shows your current points.\n!restart to restart the game.\n!rank to see your ranking.```")
        score = 0

    if message.content == "!fr":
      await message.channel.send("```Bienvenue dans le quiz **trouver un nom**\nNous vous proposons 3 niveaux de jeu qui sont indépendants des autres, il faut donc finir le niveau 1 pour accéder au 2 ! \n \n \nLISTES DES COMMANNDES :\n\n!jeu pour commencer \n!aide si vous avez beoin d'indices (ne marche qu'au niveau 1)\n!mespoints affiche vos points actuels\n!classement affiche le classement final\n!recommencer pour recommencer du début```")
      score = 0



    # INDICE

    if message.content.startswith("!help"):
        await message.channel.send("You have decided to make your life easier but this is your choice, you'll have a penalty of 0.5 points for each clue you'll use !\n```Write the question number where you have a problem (ex: !h1 to !h6)```")
    if message.content.startswith("!h1"):
        await message.channel.send("**I'm an object and help to the perception of the eye**\n")
        score = score - 0.5
    if message.content.startswith("!h2"):
        await message.channel.send("**Sailors like me**\n")
        score = score - 0.5
    if message.content.startswith("!h3"):
        await message.channel.send("**A riddle with a certain letter of the alphabet..**\n")
        score = score - 0.5
    if message.content.startswith("!h4"):
        await message.channel.send("**When you look up you can see me, but not for too long or you’ll regret it **\n")
        score = score - 0.5
    if message.content.startswith("!h5"):
        await message.channel.send("**I’m hiding from the sun**\n")
        score = score - 0.5
    if message.content.startswith("!h6"):
        await message.channel.send("**I can appear when it’s very hot, and I leave immediately I think you no longer need help, it’s logic...**\n")
        score = score - 0.5
        
        

    if message.content.startswith("!aide"):
        await message.channel.send("Vous avez décidé de vous faciliter la vie mais tel est votre choix, vous aurez un malus de 0.5 points à chaque indice utilisé !\n```Écrivez le numero de la question là où vous avez un problème (ex: !a1 à !a6)```")
    
    if message.content.startswith("!a1"):
        await message.channel.send("**Je suis un objet et j'aide à la vision des choses**\n")
        score = score - 0.5
    if message.content.startswith("!a2"):
        await message.channel.send("**Les marins m'apprécient**\n")
        score = score - 0.5
    if message.content.startswith("!a3"):
        await message.channel.send("**un jeu de mot avec une certaine lettre de l'alphabet..**\n")
        score = score - 0.5
    if message.content.startswith("!a4"):
        await message.channel.send("**Quand tu lèves les yeux tu peux m'apercevoir, mais pas trop longtemps sinon tu le regretteras !**\n")
        score = score - 0.5
    if message.content.startswith("!a5"):
        await message.channel.send("**Je fuis le soleil**\n")
        score = score - 0.5
    if message.content.startswith("!a6"):
        await message.channel.send("**Je peux apparaître quand il fait très chaud, et je repars aussitôt venu je pense que tu n'as plus besoin d'aide, c'est logique...**\n")
        score = score - 0.5


    #FRANCAIS
     #NIVEAU2

    if message.content.startswith("!jeu"):
        await message.channel.send("```Question 1 :\nJe grossis et je ne prends pas de poids. Qui suis-je ?\nChoix 1 : Une Loupe\nChoix 2 : Des Lunettes de soleil\nChoix 3 : Des Lunettes de vue```")

    if message.content == "une loupe":
        await message.channel.send("Bien joué !\nhttps://media.tenor.com/juSKPTv4zXcAAAAC/will-smith-magnifying-glass.gif")
        await message.channel.send("```Question 2 :\nQuand tu as besoin de moi, tu me jettes. Quand tu n'as plus besoin de moi, tu me ramènes.\n1) Une encre\n2) Une ancre\n3) Une enclume```")
        score = score + 1
    if message.content == "des lunettes de soleil":
        await message.channel.send("Mauvaise Réponse !\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 2 :\nQuand tu as besoin de moi, tu me jettes. Quand tu n'as plus besoin de moi, tu me ramènes.\n1) Une encrePoubelle\n2) Une ancre\n3) Une enclume  ```")
        score = score + 0
    if message.content == "des lunettes de vue":
        await message.channel.send("Mauvaise Réponse !\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 2 :\nQuand tu as besoin de moi, tu me jettes. Quand tu n'as plus besoin de moi, tu me ramènes.\n1) l'encre\n2) Une ancre\n3) Une enclume ```")
        score = score + 0
    if message.content == "une ancre":
        await message.channel.send("Bonne réponse !\nhttps://media.tenor.com/TSFcZns60VUAAAAd/dropping-anchor-ship.gif")
        await message.channel.send("```Question 3 :\nQuelle est la lettre la plus tranchante ?\n1) La F\n2) La H\n3) La T```") 
        score = score + 1
    if message.content == "une enclume":
        await message.channel.send("Mauvaise Réponse !\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 3 :\nQuelle est la lettre la plus tranchante ?\n1) La F\n2) La H\n3) La T```") 
        score = score + 0
    if message.content == "l'encre":
        await message.channel.send("Mauvaise Réponse !\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 3 :\nQuelle est la lettre la plus tranchante ?\n1) La F\n2) La H\n3) La T```")        
        score = score + 0
    if message.content == "la h":
        await message.channel.send("Bonne Réponse.\nhttps://media.tenor.com/ThHQFQoLB64AAAAj/lewa-toa.gif")
        await message.channel.send("```Question 4 :\nQu'est ce qui peut traverser une vitre sans jamais la briser ?\n1) La Chaleur \n2) Le vent\n3) Les Rayons de Soleil```")
        score = score + 1
    if message.content == "la f":
        await message.channel.send("Mauvaise Réponse !\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 4 :\nQu'est ce qui peut traverser une vitre sans jamais la briser ?\n1) La Chaleur \n2) Le vent\n3) Les Rayons de Soleil```")
        score = score + 0
    if message.content == "la t":
        await message.channel.send("Mauvaise Réponse !\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 4 :\nQu'est ce qui peut traverser une vitre sans jamais la briser ?\n1) La Chaleur \n2) Le vent\n3) Les Rayons de Soleil```")
        score = score + 0
    if message.content == "les rayons de soleil":
        await message.channel.send("On touche enfin le bout !\nhttps://media.tenor.com/KN65IEw0TqMAAAAd/parhelie-soleil.gif")
        await message.channel.send("```Question 5 :\nQu'est ce qui est plus grand que la Tour Eiffel, mais n'a pas de poids ?\n1) Son ombre\n2) Elle-même\n3) Sa perception```")
        score = score + 1
    if message.content == "le vent":
        await message.channel.send("Mauvaise Réponse !\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 5 :\nQu'est ce qui est plus grand que la Tour Eiffel, mais n'a pas de poids ?\n1) Son ombre\n2) Elle-même\n3) Sa perception```")
        score = score + 0
    if message.content == "la chaleur":
        await message.channel.send("Mauvaise Réponse !\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 5 :\nQu'est ce qui est plus grand que la Tour Eiffel, mais n'a pas de poids ?\n1) Son ombre\n2) Elle-même\n3) Sa perception```")
        score = score + 0
    if message.content == "son ombre":
        await message.channel.send("Bravo, cette question était technique.\nhttps://media.tenor.com/GPfZynG5fZIAAAAC/shadow.gif")
        await message.channel.send("```Question 6 : Je peux faire peur aux enfants mais au chocolat ils m'adorent à n'en pas finir... qui suis-je ?```\n1) Un orage \n2) La pluie \n3) un éclair")
        score = score + 1
    if message.content == "elle-meme":
        await message.channel.send("Mauvaise Réponse !\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 6 : Je peux faire peur aux enfants mais au chocolat ils m'adorent à n'en pas finir... qui suis-je ?```\n1) Un orage\n2) La pluie\n3) un éclair")
        score = score + 0
    if message.content == "sa perception":
        await message.channel.send("Mauvaise Réponse !\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 6 : Je peux faire peur aux enfants mais au chocolat ils m'adorent à n'en pas finir... qui suis-je ?```\n1) Un orage\n2) La pluie \n3) un éclair")
        score = score + 0
    if message.content == "un éclair":
        await message.channel.send("Vous avez finalement fini toutes les questions vous pouvez toujours relancer via la commande **!recommencer** ou passer au !niveau2.\nhttps://media.tenor.com/SL2dB-FCP3QAAAAM/the-flash-flash-running.gif")        
        score = score + 1
    if message.content == "un orage":
        await message.channel.send("Mauvaise Réponse !\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("Vous avez finalement fini toutes les questions vous pouvez toujours relancer via la commande **!recommencer** ou passer au !niveau2.\n")        
        score = score + 0
    if message.content == "la pluie":
        await message.channel.send("Mauvaise Réponse !\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("Vous avez finalement fini toutes les questions vous pouvez toujours relancer via la commande **!recommencer** ou passer au !niveau2.\n")
        score = score + 0


      #NIVEAU2

    if message.content.startswith("!niveau2"):
        await message.channel.send("```Question 7 : Je suis quelque chose qui t'appartient mais que les gens utilisent plus que toi, qui suis-je ?\n1) Ta voix\n2) Ton prénom\n3) Ton age ```")
    if message.content == "ton prénom" :
        await message.channel.send("Bonne Réponse ! Bravo.\nhttps://media.tenor.com/EmFFZGJ6IkwAAAAC/quel-nom-compliqu%C3%A9-nom.gif")
        await message.channel.send("```Question 8 : Je grandis sans être vivant. Je n'ai pas de poumon, mais j'ai besoin d'air pour vivre. L'eau, même si je n'ai pas de bouche, me tue, qui suis-je ?\n1) Le feu\n2) Un poisson\n3) Un trou noir```")
        score = score + 1
    if message.content == "ton age":
        await message.channel.send("Mauvaise Réponse !\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 8 : Je grandis sans être vivant. Je n'ai pas de poumon, mais j'ai besoin d'air pour vivre. L'eau, même si je n'ai pas de bouche, me tue, qui suis-je ?\n1) Le feu\n2) Un poisson\n3) Un trou noir```")
        score = score + 0
    if message.content == "ta voix":
        await message.channel.send("Mauvaise Réponse !\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 8 : Je grandis sans être vivant. Je n'ai pas de poumon, mais j'ai besoin d'air pour vivre. L'eau, même si je n'ai pas de bouche, me tue, qui suis-je ?\n1) Le feu\n2) Un poisson\n3) Un trou noir```")
        score = score + 0
    if message.content == "le feu":
        await message.channel.send("Bonne Réponse !\nhttps://media.tenor.com/vxFNoJHV3I4AAAAC/chiquichico.gif")
        await message.channel.send("```Question 9 : En étant cassé je suis plus utile que quand je ne le suis pas, qui suis-je ?\n1) Un Oeuf\n2) Du Bois\n3) Un coquillage```")
        score = score + 1
    if message.content == "un trou noir":
        await message.channel.send("Mauvaise Réponse !\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 9 : En étant cassé je suis plus utile que quand je ne le suis pas, qui suis-je ?\n1) Un Oeuf\n2) Du Bois\n3) Un coquillage```")
        score = score + 0
    if message.content == "un poisson":
        await message.channel.send("Mauvaise Réponse !\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 9 : En étant cassé je suis plus utile que quand je ne le suis pas, qui suis-je ?\n1) Un Oeuf\n2) Du Bois\n3) Un coquillage```")
        score = score + 0

    if message.content == "un oeuf":
        await message.channel.send("Bonne Réponse ! Bravo.\nhttps://media.tenor.com/66Q2g0rug9IAAAAM/tim-micallef-tim.gif")
        await message.channel.send("```Question 10 : Je suis un mois où les personnes dorment moins, qui suis-je ?\n1) Août\n2) Décembre\n3) Février```")
        score = score + 1
    if message.content == "un coquillage":
        await message.channel.send("Mauvaise Réponse !\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 10 : Je suis un mois où les personnes dorment moins, qui suis-je ?\n1) Août\n2) Décembre\n3) Février```")
        score = score + 0
    if message.content == "du bois":
        await message.channel.send("Mauvaise Réponse !\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 10 : Je suis un mois où les personnes dorment moins, qui suis-je ?\n1) Août\n2) Décembre\n3) Février```")
        score = score + 0

    if message.content == "février":
        await message.channel.send("Bonne Réponse !\nhttps://media.tenor.com/iW05S-arQ0cAAAAi/valentine-valentines.gif")
        await message.channel.send("```Question 11 : Je suis grand quand je suis jeune et petit quand je suis vieux. Je rayonne de vie et le vent est mon plus grand ennemi. Que suis-je ?\n1) Du papier\n2) Un humain\n3) Une Bougie```")
        score = score + 1
    if message.content == "août":
        await message.channel.send("Mauvaise Réponse !\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 11 : Je suis grand quand je suis jeune et petit quand je suis vieux. Je rayonne de vie et le vent est mon plus grand ennemi. Que suis-je ?\n1) Du papier\n2) Un humain\n3) Une Bougie```")
        score = score + 0
    if message.content == "décembre":
        await message.channel.send("Mauvaise Réponse !\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 11 : Je suis grand quand je suis jeune et petit quand je suis vieux. Je rayonne de vie et le vent est mon plus grand ennemi. Que suis-je ?\n1) Du papier\n2) Un humain\n3) Une Bougie```")
        score = score + 0
    if message.content == "une bougie":
        await message.channel.send("Bonne Réponse !\nhttps://media.tenor.com/Fira0s7iRWcAAAAC/frozen-candle.gif")
        await message.channel.send("```Question 12 : Monsieur et Madame Janin ont ont 6 fils. Ils ont tous une sœur, combien y-a-t-il de personne dans cette famille ?\n1) sept\n2) huit\n3) neuf```")
        score = score + 1
    if message.content == "du papier":
        await message.channel.send("Mauvaise Réponse !\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 12 : Monsieur et Madame Janin ont ont 6 fils. Ils ont tous une sœur, combien y-a-t-il de personne dans cette famille ?\n1) sept\n2) huit\n3) neuf```")
        score = score + 0
    if message.content == "un humain":
        await message.channel.send("Mauvaise Réponse !\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 12 : Monsieur et Madame Janin ont ont 6 fils. Ils ont tous une sœur, combien y-a-t-il de personne dans cette famille ?\n1) sept\n2) huit\n3) neuf```")
        score = score + 0
    if message.content == "sept":
        await message.channel.send("Mauvaise Réponse !\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Vous avez complété le niveau 2, vous pouvez continuer en allant au !niveau3```")
        score = score + 0
    if message.content == "huit":
        await message.channel.send("Mauvaise Réponse !\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Vous avez complété le niveau 2, vous pouvez continuer en allant au !niveau3```")
        score = score + 0
    if message.content == "neuf":
        await message.channel.send("Bonne Réponse !\nhttps://media.tenor.com/lp1PwlO3UFsAAAAC/benzema-karim.gif")
        await message.channel.send("```Vous avez complété le niveau 2, vous pouvez continuer en allant au !niveau3```")
        score = score + 1



      #NIVEAU3

    if message.content == "!niveau3":
        await message.channel.send("```Question 13 : Résoudre l'équation suivante : 3x - 9 = 0\n1) Solution = 3\n2) Solution = 3/4\n3) Solution = -2```")

    if message.content == "solution = 3":
        await message.channel.send("Bonne Réponse !\nhttps://media.tenor.com/StJOsOlTM48AAAAC/good-answer-hades.gif")
        await message.channel.send("```Question 14 : Déterminez la limite suivante : (2x - 1) / (x² + 5) avec x qui tend vers +infini.\n1) Solution = +Infini\n2) Solution = 2\n3) Solution = 0```")
        score = score + 1
    if message.content == "solution = 3/4":
        await message.channel.send("Mauvaise Réponse ! Bien tenté\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 14 : Déterminez la limite suivante : (2x - 1) / (x² + 5) avec x qui tend vers +infini.\n1) Solution = +Infini\n2) Solution = 2\n3) Solution = 0```")
        score = score + 0
    if message.content == "solution = -2":
        await message.channel.send("Mauvaise Réponse ! Bien tenté\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 14 : Déterminez la limite suivante : (2x - 1) / (x² + 5) avec x qui tend vers +infini.\n1) Solution = +Infini\n2) Solution = 2\n3) Solution = 0```")
        score = score + 0
    if message.content == "solution = 0":
        await message.channel.send("Bonne Réponse !\nhttps://media.tenor.com/StJOsOlTM48AAAAC/good-answer-hades.gif")
        await message.channel.send("```Question 15 : Qui a réalisé cette oeuvre ? (Nature morte au pichet vert (1865))\n1) Vincent Van Gogh\n2) Cézanne\n$3) Gauguin``` https://upload.wikimedia.org/wikipedia/commons/5/52/Cezanne_-_Stilleben_mit_gr%C3%BCnem_Gef%C3%A4%C3%9F_und_Zinnkanne.jpg")
        score = score + 1
    if message.content == "solution = 2":
        await message.channel.send("Mauvaise Réponse ! Bien tenté\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 15 : Qui a réalisé cette oeuvre ? (Nature morte au pichet vert (1865))\n1) Vincent Van Gogh\n2) Cézanne\n$3) Gauguin``` https://upload.wikimedia.org/wikipedia/commons/5/52/Cezanne_-_Stilleben_mit_gr%C3%BCnem_Gef%C3%A4%C3%9F_und_Zinnkanne.jpg")
        score = score + 0
    if message.content == "solution = +infini":
        await message.channel.send("Mauvaise Réponse ! Bien tenté\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 15 : Qui a réalisé cette oeuvre ? (Nature morte au pichet vert (1865))\n1) Vincent Van Gogh\n2) Cézanne\n$3) Gauguin``` https://upload.wikimedia.org/wikipedia/commons/5/52/Cezanne_-_Stilleben_mit_gr%C3%BCnem_Gef%C3%A4%C3%9F_und_Zinnkanne.jpg")
        score = score + 0
    if message.content == "gauguin":
        await message.channel.send("Mauvaise Réponse ! Bien tenté\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 16 : Citez le pays se trouvant entre l'Inde et la Chine.\n1) Le Népal\n2) Le Sri Lanka\n3) Le Taïwan```")
        score = score + 0
    if message.content == "vincent van gogh":
        await message.channel.send("Mauvaise Réponse ! Bien tenté\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 16 : Citez le pays se trouvant entre l'Inde et la Chine.\n1) Le Népal\n2) Le Sri Lanka\n3) Le Taïwan```")
        score = score + 0
    if message.content == "cézanne":
        await message.channel.send("Bonne Réponse !\nhttps://media.tenor.com/StJOsOlTM48AAAAC/good-answer-hades.gif")
        await message.channel.send("```Question 16 : Citez le pays se trouvant entre l'Inde et la Chine.\n1) Le Népal\n2) Le Sri Lanka\n3) Le Taïwan```")
        score = score + 1
    if message.content == "le sri lanka":
        await message.channel.send("Mauvaise Réponse ! Bien tenté\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 17 : Citez le premier président de France.\n1) Président Louis-Napoléon Bonaparte\n2) Président Adolphe Thiers\n3) Président Napoléon II```")
        score = score + 0
    if message.content == "le taiwan":
        await message.channel.send("Mauvaise Réponse ! Bien tenté\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 17 : Citez le premier président de France.\n1) Président Louis-Napoléon Bonaparte\n2) Président Adolphe Thiers\n3) Président Napoléon II```")
        score = score + 0
    if message.content == "le népal":
        await message.channel.send("Bonne Réponse !\nhttps://media.tenor.com/QwmIR-_m3WIAAAAC/nepal.gif+")
        await message.channel.send("```Question 17 : Citez le premier président de France.\n1) Président Louis-Napoléon Bonaparte\n2) Président Adolphe Thiers\n3) Président Napoléon II```")
        score = score + 1
    if message.content == "président thiers":
        await message.channel.send("Mauvaise Réponse ! Bien tenté\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 18 : Quel est le meilleur joueur de foot ?\n1) Lionel Messi\n2) CR7```")        
        score = score + 0
    if message.content == "président napoléon ii":
        await message.channel.send("Mauvaise Réponse ! Bien tenté\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 18 : Quel est le meilleur joueur de foot ?\n1) Lionel Messi\n2) CR7```")        
        score = score + 0

    if message.content == "président louis-napoléon bonaparte":
        await message.channel.send("Bonne Réponse !\nhttps://media.tenor.com/wbLdTEtMGwkAAAAM/fran%C3%A7ois-hollande-pr%C3%A9sident.gif")
        await message.channel.send("```Question 18 : Quel est le meilleur joueur de foot ?\n1) Lionel Messi\n2) CR7```")        
        score = score + 1

    if message.content == "lionel messi":
        await message.channel.send("Bonne Réponse !\nhttps://media.tenor.com/4tdgVCWep1IAAAAM/regele-fotbalului-regele.gif")
        await message.channel.send("```Vous venez de finir le mode quiz ! Si cette démo vous a plu n'hésitez pas à nous mettre une belle note pour que nous ayons la possibilité de développer de nouveaux modes ! N'hésitez pas aussi à le partager ça fait plaisir :)```")
        score = score + 1
    if message.content == "cr7":
        await message.channel.send("Mauvaise Réponse ! Bien tenté\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Vous venez de finir le mode quiz ! Si cette démo vous a plu n'hésitez pas à nous mettre une belle note pour que nous ayons la possibilité de développer de nouveaux modes ! N'hésitez pas aussi à le partager ça fait plaisir :)```")
        score = score + 0



      #ANGLAIS
        # NIVEAU 1

    if message.content.startswith("!game"):
        await message.channel.send("```Question 1 :\nI’m getting fat and I’m not gaining weight. Who am I?\n1) A Sunglass\n2) A Magnifying Glass\n3) An Eyeglass.```")
    if message.content == "a magnifying glass":
        await message.channel.send("Correct answer !\nhttps://media.tenor.com/juSKPTv4zXcAAAAC/will-smith-magnifying-glass.gif")
        await message.channel.send("```Question 2 :\nWhen you need me, you throw me out. When you don't, you bring me back.\n1) An Anchor\n2) An Ink\n3) An Anvil```")
        score = score + 1
    if message.content == "a sunglass":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 2 :\nWhen you need me, you throw me out. When you don't, you bring me back.\n1) An Anchor\n2) An Ink\n3) An Anvil```")
        score = score + 0
    if message.content == "an eyeglass":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 2 :\nWhen you need me, you throw me out. When you don't, you bring me back.\n1) An Anchor\n2) An Ink\n3) An Anvil```")
        score = score + 0
    if message.content == "an anchor":
        await message.channel.send("Correct answer !\nhttps://media.tenor.com/TSFcZns60VUAAAAd/dropping-anchor-ship.gif")
        await message.channel.send("```Question 3 :\nWhat is the sharpest letter?\n1) F\n2) T\n3) H```")
        score = score + 1
    if message.content == "an ink":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 3 :\nWhat is the sharpest letter?\n1) F\n2) T\n3) H```")
        score = score + 0
    if message.content == "an anvil":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 3 :\nWhat is the sharpest letter?\n1) F\n2) T\n3) H```")
        score = score + 0
    if message.content == "h":
        await message.channel.send("Correct answer !\nhttps://media.tenor.com/ThHQFQoLB64AAAAj/lewa-toa.gif")
        await message.channel.send("```Question 4 :\nWhat can go through a window without ever breaking it?\n1) The Sunrays\n2) Light\n3) The Heat ```")
        score = score + 1
    if message.content == "f":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 4 :\nWhat can go through a window without ever breaking it?\n1) The Sunrays\n2) Light\n3) The Heat ```")
        score = score + 0
    if message.content == "t":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 4 :\nWhat can go through a window without ever breaking it?\n1) The Sunrays\n2) Light\n3) The Heat ```")
        score = score + 0
    if message.content == "the sunrays":
        await message.channel.send("Correct answer !\nhttps://media.tenor.com/KN65IEw0TqMAAAAd/parhelie-soleil.gif")
        await message.channel.send("```Question 5 :\nWhat is bigger than the Eiffel Tower, but has no weight ?\n1) His Shadow\n2) itself\n3) Her perception ```")
        score = score + 1
    if message.content == "light":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 5 :\nWhat is bigger than the Eiffel Tower, but has no weight ?\n1) His Shadow\n2) Itself\n3) Her perception ```")
        score = score + 0
    if message.content == "the heat":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 5 :\nWhat is bigger than the Eiffel Tower, but has no weight ?\n1) His Shadow\n2) Itself\n3) Her perception ```")
        score = score + 0
    if message.content == "his shadow":
        await message.channel.send("Correct answer !\nhttps://media.tenor.com/GPfZynG5fZIAAAAC/shadow.gif")
        await message.channel.send("```Question 6 : I can scare the children but chocolate they love me not to finish... who am I ?\n1) A Storm\n2) Lightning\n3) The Rain```")
        score = score + 1
    if message.content == "her perception":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 6 : I can scare the children but chocolate they love me not to finish... who am I ?\n1) A Storm\n2) Lightning\n3) The Rain```")
        score = score + 0
    if message.content == "itself":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 6 : I can scare the children but chocolate they love me not to finish... who am I ?\n1) A Storm\n2) Lightning\n3) The Rain```")
        score = score + 0
    if message.content == "lightning":
        await message.channel.send("Correct answer !\nhttps://media.tenor.com/SL2dB-FCP3QAAAAM/the-flash-flash-running.gif")
        await message.channel.send("```You have finished level 1! You can restart using the !restart command or continue to level 2 using !level2.```")
        score = score + 1
    if message.content == "a storm":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```You have finished level 1! You can restart using the !restart command or continue to level 2 using !level2.```")
        score = score + 0
    if message.content == "the rain":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```You have finished level 1! You can restart using the !restart command or continue to level 2 using !level2.```")
        score = score + 0




    # NIVEAU 2

    if message.content.startswith("!level2"):
        await message.channel.send("```There is the level 2 ! Just a bit harder than level 1. Good Luck ! :)```")
        await message.channel.send("```Question 7 : I’m something that belongs to you but that people use more than you, who am I?\n1) My Voice\n2) My Name\n3) My Age ```")

    if message.content.startswith("my name"):
        await message.channel.send("Correct answer !\nhttps://media.tenor.com/XpUiRdezqE8AAAAC/i-know-em-by-their-birth-name-kevin-gates.gif")
        await message.channel.send("```Question 8 : I grow up without being alive. I have no lung, but I need air to live. Water, even if I have no mouth, kill me, who am I?\n1) A Fish\n2) The Fire\n3) A Black Hole```")
        score = score + 1
    if message.content == "my voice":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 8 : I grow up without being alive. I have no lung, but I need air to live. Water, even if I have no mouth, kill me, who am I?\n1) A Fish\n2) The Fire\n3) A Black Hole```")
        score = score + 0
    if message.content == "my age":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 8 : I grow up without being alive. I have no lung, but I need air to live. Water, even if I have no mouth, kill me, who am I?\n1) A Fish\n2) The Fire\n3) A Black Hole```")
        score = score + 0
    if message.content.startswith("the fire"):
        await message.channel.send("Correct answer !\nhttps://media.tenor.com/vxFNoJHV3I4AAAAC/chiquichico.gif")
        await message.channel.send("````Question 9 : Being broken I’m more useful than when I’m not, who am I?\n1) Wood\n2) An Egg\n3) A Seashell ```")
        score = score + 1
    if message.content == "a fish":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("````Question 9 : Being broken I’m more useful than when I’m not, who am I?\n1) Wood\n2) An Egg\n3) A Seashell ```")
        score = score + 0
    if message.content == "a black hole":
        await message.channel.send("Wrong answer ! Nice try\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("````Question 9 : Being broken I’m more useful than when I’m not, who am I?\n1) Wood\n2) An Egg\n3) A Seashell ```")
        score = score + 0
    if message.content == "an egg":
        await message.channel.send("Correct answer !\nhttps://media.tenor.com/66Q2g0rug9IAAAAM/tim-micallef-tim.gif")
        await message.channel.send("```Question 10 : I’m a month where people sleep less, who am I?\n1) December\n2) February\n3) August```")
        score = score + 1
    if message.content == "wood":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 10 : I’m a month where people sleep less, who am I?\n1) December\n2) February\n3) August```")
        score = score + 0
    if message.content == "a seashell":
        await message.channel.send("Wrong answer ! Nice try\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 10 : I’m a month where people sleep less, who am I?\n1) december\n2) february\n3) august```")
        score = score + 0
    if message.content == "february":
        await message.channel.send("Correct answer !\nhttps://media.tenor.com/iW05S-arQ0cAAAAi/valentine-valentines.gif")
        await message.channel.send("```Question 11 : I am big when I am young and small when I am old. I radiate life and the wind is my greatest enemy. What am I?\n1) Sheet\n2) Candle\n3) A Human```")
        score = score + 1
    if message.content == "august":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 11 : I am big when I am young and small when I am old. I radiate life and the wind is my greatest enemy. What am I?\n1) Sheet\n2) Candle\n3) A Human```")
        score = score + 0
    if message.content == "december":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 11 : I am big when I am young and small when I am old. I radiate life and the wind is my greatest enemy. What am I?\n1) Sheet\n2) Candle\n3) A Human```")
        score = score + 0
    if message.content == "candle":
        await message.channel.send("Correct answer !\nhttps://media.tenor.com/Fira0s7iRWcAAAAC/frozen-candle.gif")
        await message.channel.send("````Question 12 : Mister and Madam Janin have 6 sons. They all have a sister, how many people are there in this family ?\n1) 8\n2) 7\n3) 9```")
        score = score + 1
    if message.content == "sheet":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 12 : Mister and Madam Janin have 6 sons. They all have a sister, how many people are there in this family ?\n1) 8\n2) 7\n3) 9```")
        score = score + 0
    if message.content == "a human":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 12 : Mister and Madam Janin have 6 sons. They all have a sister, how many people are there in this family ?\n1) 8\n2) 7\n3) 9```")
        score = score + 0
    if message.content == "9":
        await message.channel.send("Correct answer !\nhttps://media.tenor.com/lp1PwlO3UFsAAAAC/benzema-karim.gif")
        await message.channel.send("```You finished level 2! You can restart using the !restart command or pass to level 3 with !level3.```")
        score = score + 1
    if message.content == "8":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```You finished level 2! You can restart using the !restart command or continue to the final level with !level3.```")
        score = score + 0
    if message.content == "7":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```You finished level 2! You can restart using the !restart command or continue to the final level with !level3.```")
        score = score + 0





        # NIVEAU 3

    if message.content.startswith("!level3"):
        await message.channel.send("```Welcome to level 3 ! Much harder than the level 2. Good Luck !```")
        await message.channel.send("```Question 13 : Solve the following equation : 3x - 9 = 0\n1) -2\n2) 3/4\n3) 3```")

    if message.content == "3":
        await message.channel.send("Correct answer !\nhttps://media.tenor.com/StJOsOlTM48AAAAC/good-answer-hades.gif")
        await message.channel.send("```Question 14 : Determine the following limit: (2x - 1) / (x² + 5) with x tending to +infinity.\n1) +infinity\n2) 0\n3) 2```")
        score = score + 1
    if message.content == "3/4":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 14 : Determine the following limit: (2x - 1) / (x² + 5) with x tending to +infinity.\n1) +infinity\n2) 0\n3) 2```")
        score = score + 0
    if message.content == "-2":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 14 : Determine the following limit: (2x - 1) / (x² + 5) with x tending to +infinity.\n1) +infinity\n2) 0\n3) 2```")
        score = score + 0
    if message.content == "0":
        await message.channel.send("Correct answer !\nhttps://media.tenor.com/StJOsOlTM48AAAAC/good-answer-hades.gif")
        await message.channel.send("```Question 15 : Who made this artwork ? (Nature morte au pichet vert (1865))``` https://upload.wikimedia.org/wikipedia/commons/5/52/Cezanne_-_Stilleben_mit_gr%C3%BCnem_Gef%C3%A4%C3%9F_und_Zinnkanne.jpg\n```1) Paul Cézanne\n2) Van Gogh\n3) Paul Gauguin```")
        score = score + 1
    if message.content == "+infinity":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 15 : Who made this artwork ? (Nature morte au pichet vert (1865))``` https://upload.wikimedia.org/wikipedia/commons/5/52/Cezanne_-_Stilleben_mit_gr%C3%BCnem_Gef%C3%A4%C3%9F_und_Zinnkanne.jpg\n```1) Paul Cézanne\n2) Van Gogh\n3) Paul Gauguin```")
        score = score + 0
    if message.content == "2":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 15 : Who made this artwork ? (Nature morte au pichet vert (1865))``` https://upload.wikimedia.org/wikipedia/commons/5/52/Cezanne_-_Stilleben_mit_gr%C3%BCnem_Gef%C3%A4%C3%9F_und_Zinnkanne.jpg\n```1) Paul Cézanne\n2) Van Gogh\n3) Paul Gauguin```")
        score = score + 0
    if message.content == "paul cézanne":
        await message.channel.send("Correct answer !\nhttps://media.tenor.com/StJOsOlTM48AAAAC/good-answer-hades.gif")
        await message.channel.send("```Question 16 : Name the country between India and China .\n1) Taïwan\n2) Népal\n3) Sri lanka```")
        score = score + 1
    if message.content == "van gogh":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 16 : Name the country between India and China .\n1) Taïwan\n2) Népal\n3) Sri lanka```")
        score = score + 0
    if message.content == "paul gauguin":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 16: Name the country between India and China .\n1) Taïwan\n2) Népal\n3) Sri lanka```")
        score = score + 0
    if message.content == "népal":
        await message.channel.send("Correct answer !\nhttps://media.tenor.com/QwmIR-_m3WIAAAAC/nepal.gif")
        await message.channel.send("```Question 17 : Name the first French president .\n1) Napoléon II\n2) Adolphe Thiers\n3) Louis-Napoléon Bonaparte```")
        score = score + 1
    if message.content == "sri lanka":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 17 : Name the first French president .\n1) Napoléon II\n2) Adolphe Thiers\n3) Louis-Napoléon Bonaparte```")
        score = score + 0
    if message.content == "taïwan":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 17 : Name the first French president .\n1) Napoléon II\n2) Adolphe Thiers\n3) Louis-Napoléon Bonaparte```")
        score = score + 0
    if message.content == "louis-napoléon bonaparte":
        await message.channel.send("Correct answer !\nhttps://media.tenor.com/wbLdTEtMGwkAAAAM/fran%C3%A7ois-hollande-pr%C3%A9sident.gif")
        await message.channel.send("```Question 18 : Who is the best football player in the world ?\n1) Leo Messi\n2) Cristiano Ronaldo```")
        score = score + 1
    if message.content == "napoléon ii":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 18 : Who is the best football player in the world ?\n1) Leo Messi\n2) Cristiano Ronaldo```")
        score = score + 0
    if message.content == "adolphe thiers":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```Question 18 : Who is the best football player in the world ?\n1) Leo Messi\n2) Cristiano Ronaldo```")
        score = score + 0
    if message.content == "leo messi":
        await message.channel.send("Correct answer !\nhttps://media.tenor.com/4tdgVCWep1IAAAAM/regele-fotbalului-regele.gif")
        await message.channel.send("```You have finished level 3! You can restart using the !restart command or pass to level 3 with !level3 .```")
        score = score + 1
        await message.channel.send("```FINAL SCORE : " + str(score) + " PTS```")
    if message.content == "cristiano ronaldo":
        await message.channel.send("Wrong answer ! Nice try.\nhttps://media.tenor.com/Ha6D75HkFywAAAAC/simpsons-wrong-answer.gif")
        await message.channel.send("```You have finished level 3! Use !ranking to see your rank ! You can also restart using the !restart command .```")
        score = score + 0
        await message.channel.send("```FINAL SCORE : " + str(score) + " PTS```")


    # RECOMMENCER

    if message.content.startswith("!restart"):
        await message.channel.send("\nThe game has been successfully relaunched !\n```Question 1 :\nI’m getting fat and I’m not gaining weight. Who am I?\n1) A Sunglass\n2) A Magnifying Glass\n3) An Eyesglass.```")
        score = 0


    if message.content.startswith("!recommencer"):
        await message.channel.send("\nLe jeu a été relancer avec succès !\n```Question 1 :\nJe grossis et je ne prends pas de poids. Qui suis-je ?\n1) Une Loupe\n2) Des lunettes\n3) Un télescope```")
        score = 0

    # LES POINTS

    if message.content.startswith("!mypoints"):
        await message.channel.send("**YOUR CURRENT POINTS : **" + str(score) + " PTS")

    if message.content.startswith("!mespoints"):
        await message.channel.send("**VOS POINTS ACTUEL : **" + str(score) + " PTS")


    # CLASSEMENT

    if message.content.startswith("!ranking"):
        await message.channel.send("```RANKING :\n\n0-3 POINTS : NOOB\n4-7 POINTS : AMATEUR\n8-12 POINTS : ADVANCED-LEVEL\n13-15 POINTS : PRO\n16-18 POINTS : GOAT```")


    if message.content.startswith("!classement"):
        await message.channel.send("```CLASSEMENT :\n\n0-3 POINTS : DEBUTANT\n4-7 POINTS : AMATEUR\n8-12 POINTS : NIVEAU-AVANCE\n13-15 POINTS : PRO\n16-18 POINTS : LEGENDE```")

client.run("MTA0NDg5OTA5ODgxMTE3NDk2Mw.Ggp7p2.60A8HryHonm5VFZlkZRkLVKNjTGo2Kcq7UGOlA")