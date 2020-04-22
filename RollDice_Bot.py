import discord
from discord.ext import commands
import random
import json
import os
from os import listdir

TOKEN = ""
BOT_PREFIX = "/"

client = commands.Bot(command_prefix=BOT_PREFIX)


def check(author):
    def inner_check(message):
        if message.author != author:
            return False
        try:
            return True
        except ValueError:
            return False
    return inner_check




@client.command(name = "test")
async def Test(ctx, nickname):
    file = json.load(open(str(ctx.guild) + "/" + nickname + ".json", "r"))
    await ctx.send(file["Firstname"])
    file["Firstname"] = "Nicolas"
    await ctx.send(file["Firstname"])
    await ctx.send(listdir(str(ctx.guild)))


@client.command(name="humor",
                brief="Quel est l'humeur du PNJ d'en face ? Ex : /humor")
async def humor(ctx):
    Possible_Humor = ["Heureux", "Complice", "Pas content agrougrou", "Vicieux", "Triste", "Au calme frère"]
    await ctx.send("Le PNJ est : " + random.choice(Possible_Humor) + ".")




@client.command(name="showplayer",
                brief = "Montre la fiche de perso d'un joueur. Ex : /showplayer marethyu")
async def showplayer(ctx, name):
    file = json.load(open(str(ctx.guild) + "/" + name.lower() + ".json", "r"))
    await ctx.send("Créateur : " + file["Owner"])
    await ctx.send("Nom : " + file["Name"] + "    Prénom : " + file["Firstname"])
    await ctx.send("Nom de héro : " + file["Nickname"])
    await ctx.send("Sexe : " + file["Sex"] + "    Age : " + file["Age"] + " ans")
    await ctx.send("PV : " + file["HP"] + "    Mana / Energie : " + file["Mana"])
    await ctx.send("Taille : " + file["Height"] + " m" + "    Poids : " + file["Weight"] + " kg")
    await ctx.send("Race : " + file["Race"] + "    Classe : " + file["Class"])
    e = discord.Embed()
    e.set_image(url=file["Picture"])
    await ctx.send(embed=e)
    await ctx.send("Histoire : " + file["Lore"])
    await ctx.send("Force : " + file["Stats"][0] + "    Dext : " + file["Stats"][1] + "    Const : " + file["Stats"][2])
    await ctx.send("Int : " + file["Stats"][3] + "    Sag : " + file["Stats"][4] + "    Cha : " + file["Stats"][5])
    await ctx.send("Stat de chance : " + file["Stats"][6])
    await ctx.send("Argent : " + file["Money"] + " pésos")
    await ctx.send("Inventaire : " + file["Inventory"])
    await ctx.send("Compétences / sorts : " + file["Skills"])
    await ctx.send("Arme : " + file["Weapon"] + "    Armure : " + file["Armor"] + "    Bouclier : " + file["Shield"])



@client.command(name="luck",
                brief="Etes vous chanceux ? Découvrons le ! Ex /luck")
async def luck(ctx):
    luck = random.randint(1, 20)
    list = listdir(str(ctx.guild))
    for files in list:
        file = json.load(open(str(ctx.guild) + "/" + files, "r"))
        if file["Owner"] == str(ctx.author):
            if luck == 1:
                await ctx.send(str(ctx.author).upper() + " est extrèmement chanceux ! C'est une réussite critique !")
            elif luck == 20:
                await ctx.send(str(ctx.author).upper() + " a une très mauvaise chance ... Echec critique ...")
            elif luck > int(file["Stats"][6]):
                await ctx.send(str(ctx.author).upper() + " a une mauvaise chance ... C'est un échec ...")
            else:
                await ctx.send(str(ctx.author).upper() + " est chanceux ! C'est une réussite !")



@client.command(name = "playeradd",
               brief = "Ajoute un joueur. Exemple : /playeradd")
async def playeradd(ctx):
    await ctx.author.send("Nous allons continuer la création ici !")
    await ctx.author.send("Quel est le Prénom et Nom de votre personnage ? Ex : Durant Hector / Jean-Paul Belmondo")
    name = await client.wait_for('message', check=check(ctx.author))
    firstname = name.content.split(" ")[1]
    name = name.content.split(" ")[0]

    await ctx.author.send("Quel est votre nom de héro ? Ex : Marethyu")
    nickname = await client.wait_for('message', check=check(ctx.author))

    await ctx.author.send("Quel est votre sexe ? Ex : Femme")
    sex = await client.wait_for('message', check=check(ctx.author))

    await ctx.author.send("Quel est votre âge ?")
    age = await client.wait_for('message', check=check(ctx.author))

    await ctx.author.send("Quel est votre taille ? Ex : 1.75")
    height = await client.wait_for('message', check=check(ctx.author))

    await ctx.author.send("Quel est votre poids ? Ex : 70")
    weight = await client.wait_for('message', check=check(ctx.author))

    await ctx.author.send("Combien de PV avez vous ? Ex : 10")
    hp = await client.wait_for('message', check=check(ctx.author))

    await ctx.author.send("Combien de mana / énergie avez vous ? Ex : 15")
    mana = await client.wait_for('message', check=check(ctx.author))

    await ctx.author.send("A quoi ressemble votre personnage ? Ex : https://ULR.com")
    picture = await client.wait_for('message', check=check(ctx.author))

    await ctx.author.send("Quel est votre race ? Ex : Humain")
    race = await client.wait_for('message', check=check(ctx.author))

    await ctx.author.send("Quel est votre classe ? Ex : Mage")
    classe = await client.wait_for('message', check=check(ctx.author))

    await ctx.author.send("Expliquer rapidement votre personnage.")
    lore = await client.wait_for('message', check=check(ctx.author))

    await ctx.author.send("Combien avez vous d'argent ? ( Demandez au MJ )")
    money = await client.wait_for('message', check=check(ctx.author))

    await ctx.author.send("Quels sont vos stats ? ( Demandez au MJ ) Ex : FORCE DEXT CONST INT SAG CHA")
    stats = await client.wait_for('message', check=check(ctx.author))
    force = stats.content.split(" ")[0]
    dext = stats.content.split(" ")[1]
    const = stats.content.split(" ")[2]
    int = stats.content.split(" ")[3]
    sag = stats.content.split(" ")[4]
    cha = stats.content.split(" ")[5]
    chance = str(random.randint(2, 19))

    await ctx.author.send("Quel est votre arme ? ( Demandez au MJ ) Ex : Epée longue 2D4")
    weapon = await client.wait_for('message', check=check(ctx.author))

    await ctx.author.send("Quelle est votre armure ? ( Demandez au MJ ) Ex : Plastron en cuir 2def")
    armor = await client.wait_for('message', check=check(ctx.author))

    await ctx.author.send("Quelle est votre bouclier ? ( Demandez au MJ ) Ex : Bouclier 4def")
    shield = await client.wait_for('message', check=check(ctx.author))

    await ctx.author.send("Quels compétences / sorts avez vous ? ( Demandez au MJ ) Ex : boule de feu 1D6 3mana, agrandissement 2mana")
    skills = await client.wait_for('message', check=check(ctx.author))

    await ctx.author.send("Quels objets avez vous ? ( Demandez au MJ ) Ex : 5 torches, 2 rations, pierre bleue")
    inventory = await client.wait_for('message', check=check(ctx.author))

    os.system("mkdir -p " + str(ctx.guild))
    file = open(str(ctx.guild) + "/" + nickname.content.lower() + ".json", "w")
    file.write('{ "Owner": "' + str(ctx.author) + '", \n')
    file.write('"Name": "' + name + '", \n')
    file.write('"Firstname": "' + firstname + '", \n')
    file.write('"Nickname": "' + nickname.content.replace(" ", "_") + '", \n')
    file.write('"Sex": "' + sex.content + '", \n')
    file.write('"Age": "' + age.content + '", \n')
    file.write('"HP": "' + hp.content + '", \n')
    file.write('"HPMax": "' + hp.content + '", \n')
    file.write('"Mana": "' + mana.content + '", \n')
    file.write('"XP": "' + "0" + '", \n')
    file.write('"Level": "' + "1" + '", \n')
    file.write('"ManaMax": "' + mana.content + '", \n')
    file.write('"Height": "' + height.content + '", \n')
    file.write('"Weight": "' + weight.content + '", \n')
    file.write('"Race": "' + race.content + '", \n')
    file.write('"Class": "' + classe.content + '", \n')
    file.write('"Picture": "' + picture.content + '", \n')
    file.write('"Lore": "' + lore.content + '", \n')
    file.write('"Stats": ["' + force + '", "' + dext + '", "' + const + '", "' + int + '", "' + sag + '", "' + cha + '", "' + chance + '"], \n')
    file.write('"Money": "' + money.content + '", \n')
    file.write('"Skills": "' + skills.content + '", \n')
    file.write('"Inventory": "' + inventory.content + '", \n')
    file.write('"Weapon": "' + weapon.content + '", \n')
    file.write('"Armor": "' + armor.content + '", \n')
    file.write('"Shield": "' + shield.content + '" }')
    file.close()

    await showplayer(ctx, nickname.content)




@client.command(name = "playerdel",
                brief = "Supprime un joueur. Exemple : /playerdel nom_du_joueur",
                aliases = ["delete", "disparition"])
async def playerdel(ctx, name):
    os.system("rm " + str(ctx.guild) + "/" + name.lower() + ".json")
    await ctx.send("La main de Dieu est tombée ! Le joueur : " + str(name.upper()) + " a disparu.")




@client.command(name = "drink", 
                brief = "BATTLE DE BOISSONS !!!!! /drink Joueur1 Stat Joueur2 Stat")
async def Drink(ctx, player1, stat1, player2, stat2):
    Drink1 = 0
    Drink2 = 0
    stat1 = int(stat1)
    stat2 = int(stat2)
    while (Drink1 < 3 and Drink2 < 3):
        Dice1 = random.randint(1, 20)
        Dice2 = random.randint(1, 20)
        if Dice1 == 1 and Dice2 == 1:
            Drink1 = 50
            Drink2 = 50
            await ctx.send("Double échec critique ! C'est du jamais vu !")
        elif Dice1 == 1 and Dice2 >= stat2:
            Drink1 = 50
            Drink2 += 1
            await ctx.send(player1 + " a fait un échec critique !")
        elif Dice1 == 1 and Dice2 < stat2:
            Drink1 = 50
            await ctx.send(player1 + " a fait un échec critique !")
        elif Dice1 == 1 and Dice2 == 20:
            Drink1 = 50
            Drink2 -= 1
            await ctx.send(player2 + " a fait une réussite critique. Il attend la difficulté ...")
            await ctx.send(player1 + " a fait un échec critique !")

        elif Dice1 >= stat1 and Dice2 == 1:
            Drink1 += 1
            Drink2 = 50
            await ctx.send(player2 + " a fait un échec critique !")
        elif Dice1 >= stat1 and Dice2 >= stat2:
            Drink1 += 1
            Drink2 += 1
        elif Dice1 >= stat1 and Dice2 < stat2:
            Drink1 += 1
        elif Dice1 >= stat1 and Dice2 == 20:
            Drink1 += 1
            Drink2 -= 1
            await ctx.send(player2 + " a fait une réussite critique. Il attend la difficulté ...")

        elif Dice1 < stat1 and Dice2 == 1:
            Drink2 = 50
            await ctx.send(player2 + " a fait un échec critique !")
        elif Dice1 < stat1 and Dice2 >= stat2:
            Drink2 += 1
        elif Dice1 < stat1 and Dice2 == 20:
            Drink2 -= 1
            await ctx.send(player2 + " a fait une réussite critique. Il attend la difficulté ...")

        elif Dice1 == 20 and Dice2 == 1:
            Drink1 -= 1
            Drink2 = 50
            await ctx.send(player1 + " a fait une réussite critique. Il attend la difficulté ...")
            await ctx.send(player2 + " a fait un échec critique !")
        elif Dice1 == 20 and Dice2 >= stat2:
            Drink1 -= 1
            Drink2 += 1
            await ctx.send(player1 + " a fait une réussite critique. Il attend la difficulté ...")
        elif Dice1 == 20 and Dice2 < stat2:
            Drink1 -= 1
            await ctx.send(player1 + " a fait une réussite critique. Il attend la difficulté ...")
        elif Dice1 == 20 and Dice2 == 20:
            Drink1 -= 1
            Drink2 -= 1
            await ctx.send("Double réussite critique ! Serveur ! Remenez du vrai alcool !")

        if Drink1 >= 3 and Drink2 >= 3:
            await ctx.send("Les 2 participants sont entrain de rouler ... Egalité !")
        elif Drink1 >= 3:
            await ctx.send(player1 + " vient de s'effondrer ... " + player2 + " a gagné !")
        elif Drink2 >= 3:
            await ctx.send(player2 + " vient de s'effondrer ... " + player1 + " a gagné !")





@client.command(name = "hit", 
                brief = "Choisi au hasard la partie du corps touchée. Exemple : /hit")
async def BodyHit(ctx):
    Touch = random.randint(1, 17)
    if Touch <= 5:
        await ctx.send("Vous avez touché le torse !")
    elif Touch <=7:
        await ctx.send("Vous avez touché le bras droit !")
    elif Touch <=9:
        await ctx.send("Vous avez touché le bras gauche !")
    elif Touch <=11:
        await ctx.send("Vous avez touché la jambe droite !")
    elif Touch <=13:
        await ctx.send("Vous avez touché la jambe gauche !")
    elif Touch <= 15:
        await ctx.send("Vous avez touché la tête !")
    else:
        await ctx.send("Vous avez touché l'entre jambe !")






@client.command(name = "rd",
                brief = "Lancé de dés random. Exemple : /rd D10 ou /rd 2D20")
async def rolldice(ctx, dice):
    dice = dice.upper()
    dice = dice.split("D")
    if dice[0] == None or dice[0] == "" or dice[0] == " " or dice[0] == "1":
        result = random.randint(1, int(dice[1]))
        await ctx.send("Les dés ne mentent pas ! C'est un : " + str(result))
    else:
        answer = ""
        total = 0
        for i in range(int(dice[0])):
            result = random.randint(1, int(dice[1]))
            total += result
            if i == int(dice[0])-1:
                answer += str(result)
            else:
                answer += str(result) + " + "
        await ctx.send("Les dés ne mentent pas ! Ce sont des : ")
        await ctx.send(answer + " = " + str(total))




#@client.event
#async def on_command_error(ctx, error):
#    await ctx.send(type(error))
#    if isinstance(error, commands.MissingRequiredArgument):
#        await ctx.send("Il manque des paramètres à votre commande !")

@client.command(name = "w",
                brief = "Choisi aléatoirement le temps actuel. Exemple : /w")
async def weather(ctx):
    possible_weather = ["Grand soleil", "Nuageux", "Pluvieux"]
    await ctx.send("Le temps actuel est : " + random.choice(possible_weather) + ".")
    vent = random.randint(1, 2)
    if vent == 1:
        await ctx.send("Il y a du vent.")
    else:
        await ctx.send("Il n'y a pas de vent.")




@client.command(name = "chp",
                brief = "Montre les PV actuel des joueurs. Exemple : /chp")
async def chp(ctx):
    list = listdir(str(ctx.guild))
    await ctx.send("Les joueurs ont :")
    for files in list:
        file = json.load(open(str(ctx.guild) + "/" + files, "r"))
        await ctx.send(file["Nickname"] + " a " + file["HP"] + " PV sur " + file["HPMax"] + " PV max.")


@client.command(name = "cmoney",
                brief = "Affiche la thune de tout les joueurs. Exemple : /cmoney")
async def current_money(ctx):
    list = listdir(str(ctx.guild))
    await ctx.send("Les joueurs ont :")
    for files in list:
        file = json.load(open(str(ctx.guild) + "/" + files, "r"))
        await ctx.send(file["Nickname"] + " a " + file["Money"] + " Pésos.")



@client.command(name = "cmana",
                brief = "Affiche la mana/énergie actuelle des joueurs. Exemple : /cmana")
async def show_mana(ctx):
    list = listdir(str(ctx.guild))
    await ctx.send("Les joueurs ont :")
    for files in list:
        file = json.load(open(str(ctx.guild) + "/" + files, "r"))
        await ctx.send(file["Nickname"] + " a " + file["Mana"] + " Mana/Energie sur " + file["ManaMax"] + " Mana/Energie max.")


@client.command(name = "cxp",
                brief = "Affiche l'xp et le niv. Exemple : /cxp")
async def current_xp(ctx):
    list = listdir(str(ctx.guild))
    await ctx.send("Les joueurs ont :")
    for files in list:
        file = json.load(open(str(ctx.guild) + "/" + files, "r"))
        await ctx.send(file["Nickname"] + " est level " + file["Level"] + " et a " + file["XP"] + " points d'XP.")



@client.command(name = "cstats",
                brief = "Affiche ses stats. Exemple : /cstats")
async def show_stats(ctx):
    list = listdir(str(ctx.guild))
    await ctx.send("Les joueurs ont :")
    for files in list:
        file = json.load(open(str(ctx.guild) + "/" + files, "r"))
        await ctx.send(file["Nickname"] + " a : " + file["Stats"][0] + " force, " + file["Stats"][1] + " dext, " + file["Stats"][2] + " const, " + file["Stats"][3] + " int, " + file["Stats"][4] + " sag, " + file["Stats"][5] + " cha.")
        await ctx.send("Stat de chance : " + file["Stats"][6])






@client.command(name = "hp",
                brief = "Ajoute ou enlève des PV à un joueur. Exemple : /hp nom +/-PV")
async def players(ctx, player, hp):
    jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "r")
    file = json.load(jsonfile)
    HPMax = file["HPMax"]
    if hp[0] == "-":
        hp = hp.replace("-", "")
        file["HP"] = str(int(file["HP"])-int(hp))
        if int(file["HP"]) <= 0:
            file["HP"] = 0
            await ctx.send(player.upper() + " est mort !")
        else:
            await ctx.send(player.upper() + " a actuellement " + file["HP"] + " PV.")
    elif hp[0] == "+":
        hp = hp.replace("+", "")
        file["HP"] = str(int(file["HP"])+int(hp))
        if int(file["HP"]) >= int(file["HPMax"]):
            file["HP"] = file["HPMax"]
            await ctx.send(player.upper() + " est full vie !")
        else:
            await ctx.send(player.upper() + " a actuellement " + file["HP"] + " PV.")
    jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "w")
    json.dump(file, jsonfile)




@client.command(name = "hpmax",
                brief = "Modifie les PV max d'un joueur. Ex : /hpmax nom_du_joueur +/-PV",
                aliases = ["pvmax"])
async def hpmax(ctx, player, hp):
    jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "r")
    file = json.load(jsonfile)
    if hp[0] == "+":
        hp = hp.replace("+", "")
        file["HPMax"] = str(int(file["HPMax"])+int(hp))
        file["HP"] = str(int(file["HP"])+int(hp))
    elif hp[0] == "-":
        hp = hp.replace("-", "")
        file["HPMax"] = str(int(file["HPMax"])-int(hp))
        file["HP"] = str(int(file["HP"])-int(hp))
    await ctx.send("Les PV max de " + str(player.upper()) + " sont au max de " + file["HPMax"])
    jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "w")
    json.dump(file, jsonfile)




@client.command(name = "heal",
                brief = "Heal au maxi tout les joueurs ou un seul. Exemple : /heal nom/all")
async def heal(ctx, player):
    if player.lower() == "all":
        list = listdir(str(ctx.guild))
        for files in list:
            jsonfile = open(str(ctx.guild) + "/" + files, "r")
            file = json.load(jsonfile)
            file["HP"] = file["HPMax"]
            file["Mana"] = file["ManaMax"]
            jsonfile = open(str(ctx.guild) + "/" + files, "w")
            json.dump(file, jsonfile)
        await ctx.send("Tout les joueurs sont full vie et mana !")
    else:
        jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "r")
        file = json.load(jsonfile)
        file["HP"] = file["HPMax"]
        file["Mana"] = file["ManaMax"]
        jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "w")
        json.dump(file, jsonfile)
        await ctx.send("Le joueur " + player.upper() + " est bien full vie et mana !")





@client.command(name = "money",
                brief = "Modifie le solde d'un compte. Exemple : /money Joueur +/-Nombre")
async def add_or_remove_money(ctx, player, money):
    jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "r")
    file = json.load(jsonfile)
    if money[0] == "+":
        money = money.replace("+", "")
        file["Money"] = str(int(file["Money"])+int(money))
        await ctx.send("Le joueur " + player.upper() + " a " + file["Money"] + " pésos.")
    elif money[0] == "-":
        money = money.replace("-", "")
        if int(file["Money"])-int(money) < 0:
            await ctx.send(player.upper() + " n'as pas assez d'argent !")
        else:
            file["Money"] = str(int(file["Money"])-int(money))
            await ctx.send("Le joueur " + player.upper() + " a " + file["Money"] + " pésos.")
    jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "w")
    json.dump(file, jsonfile)





@client.command(name = "mana",
                brief = "Modifie la mana/énergie d'un joueur. Exemple : /mana nom +/-Mana")
async def mana(ctx, player, mana):
    jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "r")
    file = json.load(jsonfile)
    if mana[0] == "+":
        mana = mana.replace("+", "")
        file["Mana"] = str(int(file["Mana"])+int(mana))
        if int(file["Mana"]) > int(file["ManaMax"]):
            file["Mana"] = file["ManaMax"]
        await ctx.send("Le joueur " + player.upper() + " a " + file["Mana"] + " mana/énergie sur " + file["ManaMax"] + " mana/énergie max.")
    elif mana[0] == "-":
        mana = mana.replace("-", "")
        if int(file["Mana"]) < 0:
            await ctx.send("Le joueur " + player.upper() + " n'as pas assez de mana/énergie !")
        else:
            file["Mana"] = str(int(file["Mana"])-int(mana))
            await ctx.send("Le joueur " + player.upper() + " a " + file["Mana"] + " mana/énergie sur " + file["ManaMax"] + " mana/énergie max.")
    jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "w")
    json.dump(file, jsonfile)





@client.command(name = "manamax",
                brief = "Ajoute de la mana max a un joueur. Exemple : /manamax nom Mana")
async def manamax(ctx, player, mana):
    jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "r")
    file = json.load(jsonfile)
    file["ManaMax"] = str(int(file["ManaMax"])+int(mana))
    file["Mana"] = str(int(file["Mana"])+int(mana))
    jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "w")
    await ctx.send(player.upper() + " a un maximum de " + file["ManaMax"] + " mana.")
    json.dump(file, jsonfile)





@client.command(name = "xp",
                brief = "Ajoute de l'xp. Exemple : /xp nom/all xp")
async def xp(ctx, player, xp):
    if player.lower() == "all":
        list = listdir(str(ctx.guild))
        for files in list:
            jsonfile = open(str(ctx.guild) + "/" + files, "r")
            file = json.load(jsonfile)
            XP = int(file["XP"])
            if XP + int(xp) >= 100:
                XP += int(xp) - 100
                file["XP"] = str(XP)
                file["Level"] = str(int(file["Level"]) + 1)
            else:
                file["XP"] = str(int(file["XP"]) + int(xp))
        jsonfile = open(str(ctx.guild) + "/" + files, "w")
        json.dump(file, jsonfile)
        await ctx.send(file["Nickname"].upper() + " est niveau " + file["Level"] + " et a " + file["XP"] + " XP.")
    else:
        jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "r")
        file = json.load(jsonfile)
        XP = int(file["XP"])
        if XP + int(xp) >= 100:
            XP += int(xp) - 100
            file["XP"] = str(XP)
            file["Level"] = str(int(file["Level"]) + 1)
        else:
            file["XP"] = str(int(file["XP"]) + int(xp))
        jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "w")
        json.dump(file, jsonfile)
        await ctx.send(player.upper() + " est niveau " + file["Level"] + " et a " + file["XP"] + " XP.")





@client.command(name = "setstats",
                brief = "Set les stats. Ex : /setstats joueur force dext const int sag cha")
async def set_stats(ctx, player, force, dext, const, int, sag, cha):
    jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "r")
    file = json.load(jsonfile)
    file["Stats"][0] = force
    file["Stats"][1] = dext
    file["Stats"][2] = const
    file["Stats"][3] = int
    file["Stats"][4] = sag
    file["Stats"][5] = cha
    jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "w")
    json.dump(file, jsonfile)
    await ctx.send("Force : " + file["Stats"][0] + "    Dext : " + file["Stats"][1] + "    Const : " + file["Stats"][2])
    await ctx.send("Int : " + file["Stats"][3] + "    Sag : " + file["Stats"][4] + "    Cha : " + file["Stats"][5])




@client.command(name="chweapon",
                brief="Vous permet de changer d'arme. Ex: /chweapon joueur \"arme\"")
async def change_weapon(ctx, player, weapon):
    jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "r")
    file = json.load(jsonfile)
    file["Weapon"] = weapon
    jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "w")
    json.dump(file, jsonfile)
    await ctx.send(player.upper() + " a changé d'arme pour : " + file["Weapon"])


@client.command(name="charmor",
                brief="Vous permet de changer d'arme. Ex: /charmor joueur \"armure\"")
async def change_armor(ctx, player, armor):
    jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "r")
    file = json.load(jsonfile)
    file["Armor"] = armor
    jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "w")
    json.dump(file, jsonfile)
    await ctx.send(player.upper() + " a changé d'armure pour : " + file["Armor"])


@client.command(name="chshield",
                brief="Vous permet de changer d'arme. Ex: /chshield joueur \"bouclier\"")
async def change_shield(ctx, player, shield):
    jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "r")
    file = json.load(jsonfile)
    file["Shield"] = shield
    jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "w")
    json.dump(file, jsonfile)
    await ctx.send(player.upper() + " a changé de bouclier pour : " + file["Shield"])



@client.command(name="cinventory",
                brief="Affiche l'inventaire d'un joueur. Ex : /cinventory joueur")
async def current_inventory(ctx, player):
    jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "r")
    file = json.load(jsonfile)
    Inventory = file["Inventory"].split(",")
    await ctx.send(player.upper() + " a dans son inventaire :")
    for i in range (0, len(Inventory)):
        await ctx.send(str(i+1) + "    :    " + Inventory[i])
    await ctx.send(str(len(Inventory)+1) + "    :    None")





@client.command(name="inventory",
                brief="Modifie l'inventaire d'un joueur. Ex : /inventory joueur")
async def modify_inventory(ctx, player):
    await current_inventory(ctx, player)
    jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "r")
    file = json.load(jsonfile)
    Inventory = file["Inventory"].split(",")
    InventoryStr = ""
    await ctx.send("Voulez vous ajouter, modifier ou supprimer une ligne ? ajouter | modifier | supprimer")
    choice = await client.wait_for('message', check=check(ctx.author))
    if choice.content.lower() == "ajouter":
        await ctx.send("Que voulez vous ajouter ? Ex : 2 rations | None")
        object = await client.wait_for('message', check=check(ctx.author))
        if object.content.lower() == "none":
            await ctx.send("Rien n'a été modifié.")
        else:
            Inventory.append(object.content)
            await ctx.send("La ligne a été ajoutée.")
    elif choice.content.lower() == "modifier":
        await ctx.send("Quelle ligne voulez vous modifier ? Ex : 2")
        line = await client.wait_for('message', check=check(ctx.author))
        if int(line.content) == len(Inventory) + 1:
            await ctx.send("Rien n'a été modifié.")
        else:
            await ctx.send("Comment voulez vous le modifier ? Ex : 5 torches")
            object = await client.wait_for('message', check=check(ctx.author))
            Inventory[int(line.content)-1] = object.content
            await ctx.send("La ligne a bien été modifiée.")
    elif choice.content.lower() == "supprimer":
        await ctx.send("Quelle ligne voulez vous supprimer ? Ex : 2")
        line = await client.wait_for('message', check=check(ctx.author))
        if int(line.content) == len(Inventory) + 1:
            await ctx.send("Rien n'a été modifié.")
        else:
            Inventory.pop(int(line.content)-1)
            await ctx.send("La ligne a bien été supprimée.")
    else:
        await ctx.send("Vous avez fait une erreur dans la réponse. Merci de relancer la commande.")
    for Obj in Inventory:
        if Obj == Inventory[-1]:
            InventoryStr += Obj
        else:
            InventoryStr += Obj + ","
    file["Inventory"] = InventoryStr
    jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "w")
    json.dump(file, jsonfile)




@client.command(name="cskill",
                brief="Affiche les compétences / sorts d'un joueur. Ex : /cskill joueur")
async def current_inventory(ctx, player):
    jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "r")
    file = json.load(jsonfile)
    Skills = file["Skills"].split(",")
    await ctx.send(player.upper() + " a comme compétences / sorts :")
    for i in range (0, len(Skills)):
        await ctx.send(str(i+1) + "    :    " + Skills[i])
    await ctx.send(str(len(Skills)+1) + "    :    None")




@client.command(name="skill",
                brief="Modifie les compétences / sorts d'un joueur. Ex : /skill joueur")
async def modify_inventory(ctx, player):
    await current_inventory(ctx, player)
    jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "r")
    file = json.load(jsonfile)
    Skills = file["Skills"].split(",")
    SkillsStr = ""
    await ctx.send("Voulez vous ajouter, modifier ou supprimer une ligne ? ajouter | modifier | supprimer")
    choice = await client.wait_for('message', check=check(ctx.author))
    if choice.content.lower() == "ajouter":
        await ctx.send("Que voulez vous ajouter ? Ex : tir des arcanes 1D6 2mana | None")
        skill = await client.wait_for('message', check=check(ctx.author))
        if skill.content.lower() == "none":
            await ctx.send("Rien n'a été modifié.")
        else:
            Skills.append(skill.content)
            await ctx.send("La ligne a été ajoutée.")
    elif choice.content.lower() == "modifier":
        await ctx.send("Quelle ligne voulez vous modifier ? Ex : 2")
        line = await client.wait_for('message', check=check(ctx.author))
        if int(line.content) == len(Skills) + 1:
            await ctx.send("Rien n'a été modifié.")
        else:
            await ctx.send("Comment voulez vous le modifier ? Ex : tir des arcanes 1D6 2mana")
            skill = await client.wait_for('message', check=check(ctx.author))
            Skills[int(line.content)-1] = skill.content
            await ctx.send("La ligne a bien été modifiée.")
    elif choice.content.lower() == "supprimer":
        await ctx.send("Quelle ligne voulez vous supprimer ? Ex : 2")
        line = await client.wait_for('message', check=check(ctx.author))
        if int(line.content) == len(Skills) + 1:
            await ctx.send("Rien n'a été modifié.")
        else:
            Skills.pop(int(line.content)-1)
            await ctx.send("La ligne a bien été supprimée.")
    else:
        await ctx.send("Vous avez fait une erreur dans la réponse. Merci de relancer la commande.")
    for Obj in Skills:
        if Obj == Skills[-1]:
            SkillsStr += Obj
        else:
            SkillsStr += Obj + ","
    file["Skills"] = SkillsStr
    jsonfile = open(str(ctx.guild) + "/" + player.lower() + ".json", "w")
    json.dump(file, jsonfile)



client.run(TOKEN)
