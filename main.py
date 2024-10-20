import pygame
import random
import math
from decimal import Decimal
from functions.MassiveNum import BigNumber
import math
import time
import pickle
import os

pygame.font.init()
pygame.init
StaticFont = "Segou UI"
originalDisplayHeight = 640
originalDisplayWidth = 640
win = pygame.display.set_mode((640, 640), pygame.RESIZABLE)
pygame.display.set_caption("Oidle")

customFont = 'bigblueterm437nerdfont'




def DisplayHunter():
    text = "These guys will run around getting food and miscallenous materials for you!"
    DrawText("Hunter", 320, 320, 40, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText(text, 320, 350, 12, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText("Job Priority", 280, 433, 15, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText(str(JobPriorities[0]) + "%", 280, 453, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText("Jobs Occupied", 100, 433, 15, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText(str(OidInJob[0]), 100, 453, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    sumjob = sum(JobPriorities)
    newval = Arrows(400, 450, 1, 10)
    if (newval + sumjob) > 100:
        newval = 100 - sumjob
    if (newval + JobPriorities[0]) < -100:
        JobPriorities[0] = -100
        return ()
    JobPriorities[0] = JobPriorities[0] + newval


def DisplayFarmer():
    text = "These little bros will go around harvesting elixir for you!"
    DrawText("Farmer", 320, 320, 40, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText(text, 320, 350, 12, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText("Job Priority", 280, 433, 15, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText(str(JobPriorities[1]) + "%", 280, 453, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText("Jobs Occupied", 100, 433, 15, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText(str(OidInJob[1]), 100, 453, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    sumjob = sum(JobPriorities)
    newval = Arrows(400, 450, 1, 10)
    if (newval + sumjob) > 100:
        newval = 100 - sumjob
    if (newval + JobPriorities[1]) < -100:
        JobPriorities[1] = -100
        return ()
    JobPriorities[1] = JobPriorities[1] + newval


def DisplayHealer():
    text = "Immortal Oids do sound fun."
    DrawText("Healer", 320, 320, 40, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText(text, 320, 350, 20, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText("Job Priority", 280, 433, 15, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText(str(JobPriorities[2]) + "%", 280, 453, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText("Jobs Occupied", 100, 433, 15, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText(str(OidInJob[2]), 100, 453, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    sumjob = sum(JobPriorities)
    newval = Arrows(400, 450, 1, 10)
    if (newval + sumjob) > 100:
        newval = 100 - sumjob
    if (newval + JobPriorities[2]) < -100:
        JobPriorities[2] = -100
        return ()
    JobPriorities[2] = JobPriorities[2] + newval


def DisplayWarrior():
    text = "Brave warriors that fight the darkness!"
    DrawText("Warrior", 320, 320, 40, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText(text, 320, 350, 20, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText("Job Priority", 280, 433, 15, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText(str(JobPriorities[4]) + "%", 280, 453, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText("Jobs Occupied", 100, 433, 15, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText(str(OidInJob[4]), 100, 453, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    sumjob = sum(JobPriorities)
    newval = Arrows(400, 450, 1, 10)
    if (newval + sumjob) > 100:
        newval = 100 - sumjob
    if (newval + JobPriorities[4]) < -100:
        JobPriorities[4] = -100
        return ()
    JobPriorities[4] = JobPriorities[4] + newval

def DisplayArcanist():
    text = "The weakest of the strongest."
    DrawText("Arcanist", 320, 320, 40, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText(text, 320, 350, 20, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText("Job Priority", 280, 433, 15, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText(str(JobPriorities[5]) + "%", 280, 453, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText("Jobs Occupied", 100, 433, 15, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText(str(OidInJob[5]), 100, 453, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    sumjob = sum(JobPriorities)
    newval = Arrows(400, 450, 1, 10)
    if (newval + sumjob) > 100:
        newval = 100 - sumjob
    if (newval + JobPriorities[5]) < -100:
        JobPriorities[5] = -100
        return ()
    JobPriorities[5] = JobPriorities[5] + newval

def DisplayBuilder():
    text = "Can we fix it??"
    DrawText("Builder", 320, 320, 40, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText(text, 320, 350, 20, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText("Job Priority", 280, 433, 15, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText(str(JobPriorities[3]) + "%", 280, 453, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText("Jobs Occupied", 100, 433, 15, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText(str(OidInJob[3]), 100, 453, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    sumjob = sum(JobPriorities)
    newval = Arrows(400, 450, 1, 10)
    if (newval + sumjob) > 100:
        newval = 100 - sumjob
    if (newval + JobPriorities[3]) < -100:
        JobPriorities[3] = -100
        return ()
    JobPriorities[3] = JobPriorities[3] + newval

def UpgradesTab():

    Icon(32,  96, 17, 12, "Oib.png", "Oids: ", Oids)
    Icon(152, 96, 17, 12, "elixir.png", "Elixir: ", elixir)
    Icon(298, 96, 17, 12, "Ouire.png", "Ouire: ", Ouire)

    DisplayUpgrades()


def BuildingsTab():

    Icon(32,  96, 17, 12, "Oib.png", "Oids: ", Oids)
    Icon(152, 96, 17, 12, "elixir.png", "Elixir: ", elixir)
    Icon(318, 96, 17, 12, "Ouire.png", "Ouire: ", Ouire)

    DrawImage(320, 220, "building.png", 0)
    Icon(32, 320, 20, 16, "Oib.png", "Builders: ", OidInJob[3])
    Icon(32, 360, 25, 16, "Oib.png", "Total Employed Oids: ", specSum(OidInJob))
    Icon(32, 400, 25, 16, "Oib.png", "Buildings: ", Buildings)


JobPngsList = ["hunter.png", "farmer.png", "healer.png", "builder.png", "warrior.png", "arcanist.png"]
ChangeJobsList = [ChangeToHunter, ChangeToFarmer, ChangeToHealer, ChangeToBuilder, ChangeToWarrior, ChangeToArcanist]

def JobsTab():
    canShow = [True, upgrades[0].bought, upgrades[2].bought, upgrades[1].bought, False, False]

    Icon(32,  96, 17, 12, "Oib.png", "Oids: ", Oids)
    Icon(152, 96, 17, 12, "elixir.png", "Elixir: ", elixir)
    Icon(298, 96, 17, 12, "Ouire.png", "Ouire: ", Ouire)

    JobButton(64,  200, 0, canShow[JobsList[0]])
    JobButton(192, 200, 1, canShow[JobsList[1]])
    JobButton(320, 200, 2, canShow[JobsList[2]])
    JobButton(448, 200, 3, canShow[JobsList[3]])
    JobButton(576, 200, 4, canShow[JobsList[4]])

    func = JobTabs[displayJobPointer]
    func()
    Button(50, 288, 128, 128, "arrowleft.png", False, False, CycleLeft)
    Button(590, 288, 128, 128, "arrowright.png", False, False, CycleRight)

def JobButton(x, y, i, canShow):
    if canShow == True:
        Button(
            x,
            y,
            64,
            64,
            JobPngsList[JobsList[i]],
            False,
            False,
            ChangeJobsList[JobsList[i]],
        )
    else:
        DrawImage(x, y, JobPngsList[JobsList[i]], 0)
        DrawImage(x, y, "LOCKED.png", 0)


def ChangeToJobs(ignore, clicked):
    if clicked == True:
        global tabpointer
        tabpointer = 0


def ChangeToBuilding(ignore, clicked):
    if clicked == True:
        global tabpointer
        tabpointer = 1


def ChangeToUpgrades(ignore, clicked):
    if clicked == True:
        global tabpointer
        tabpointer = 2


def EnterJob(i, unemployed):

    priority = BigNumber(JobPriorities[i]/100)
    if BigNumber.overZero(priority):
        OidInJob[i] = OidInJob[i] + (unemployed * priority)
    elif BigNumber.underZero(priority):
            if priority != 0:
                minus = priority+1
                OidInJob[i] = OidInJob[i]*minus
    if OidInJob[i] > Oids:
        OidInJob[i] == BigNumber(0, 0)


def OidChangeJobs():
    global Oids
    Oidsinjob = specSum(OidInJob)
    unemployed = Oids - Oidsinjob
    
    EnterJob(0, unemployed)
    EnterJob(1, unemployed)
    EnterJob(2, unemployed)
    EnterJob(3, unemployed)


def OidDoJobs():
    global JobEfficiency
    l = OidInJob[0] + 1
    t = specSum(OidInJob) + l
    JobEfficiency = BigNumber.logxy(Buildings+1,13)+1
    HunterJobDo()
    FarmerJobDo()
    HealerJobDo()
    BuilderJobDo()

def elixirAdd(elixirPlus):
    global elixir
    elixir = elixir + elixirPlus*elxMultiplier

def ouireAdd(ouirePlus):
    global Ouire
    Ouire = Ouire + ouirePlus*ouireMultiplier

def HunterJobDo():
    SCALINGDEBUFF = (BigNumber.logxy(OidInJob[0],16)**BigNumber(0.9))+1
    elixirPlus = (OidInJob[0] / 200)/SCALINGDEBUFF
    elixirAdd(elixirPlus)
    OuirePlus = (OidInJob[0] / 600)/SCALINGDEBUFF
    ouireAdd(OuirePlus)


def FarmerJobDo():
    SCALINGDEBUFF = (BigNumber.logxy(OidInJob[0],10)**BigNumber(2.5))+1
    elixirPlus = (OidInJob[1]) * JobEfficiency / 70 / SCALINGDEBUFF
    elixirAdd(elixirPlus)

def BuilderJobDo():
    global Buildings
    global Ouire    
    BuildingsPlus = OidInJob[3] / 1000 * JobEfficiency*Ouire
    BuildingsPlus = BigNumber.logxy(BuildingsPlus,4)
    if Ouire*10 > BuildingsPlus:
        Ouire -= BigNumber.logxy(BuildingsPlus,4)*10
        Buildings += BigNumber.logxy(BuildingsPlus,4)


def HealerJobDo():
    SCALINGDEBUFF = (BigNumber.logxy(OidInJob[0],16)**BigNumber(3.5))+1
    global health
    health = BigNumber.logxy(OidInJob[2],100)/SCALINGDEBUFF
    if health < 1:
        health = 1


def OidsDie():
    global elixir
    global Oids
    if elixir >= Oids / 10:
        elixir -= Oids / 10
    else:
        OidsDie = round(Oids - (elixir * 10))
        ratio = Oids / OidsDie
        if ratio > 0.75:
            OidsDie = round(OidsDie * 0.75)
        Oids -= OidsDie
        if Oids < 0:
            Oids = BigNumber(0, 0)

def NewOids():
    global elixir
    global Oids
    if Oids != 0:
        oldelixir = elixir
        oldOids = Oids
        if elixir >= Oids / 2:
            elixir = elixir - round(oldOids)
            OidPlus = ((oldelixir) / 2)*health
            div = ((BigNumber.logxy(OidPlus, 100))**1.15)
            OidPlus = OidPlus/div
            Oids = Oids+OidPlus


class Upgrade:
    def __init__(self, x, y, picture, function, level = BigNumber(0,0)):
        self.png = picture
        self.x = x
        self.y = y
        self.func = function
        self.bought = False
        self.lvl = level

    def DoUpgrade(self):
        if self.bought == False:
            on, click = Button(
                self.x,
                self.y,
                16,
                16,
                self.png,
                "blankUpgrade.png",
                "blankUpgradeHover.png",
                ReturnVal,
            )
        else:
            on, click = Button(
                self.x,
                self.y,
                16,
                16,
                self.png,
                "boughtUpgrade.png",
                "boughtUpgrade.png",
                ReturnVal,
            )
        self.func(on, click)


def void(n, a):
    return 0


def UpgradesCreate(amount, startX, startY, ywidth, xIncrement, yIncrement):
    global void
    global upgrades
    for i in range(0, amount):
        x = startX + xIncrement * (i % ywidth)
        y = startY + yIncrement * (math.floor(i / ywidth))
        upgradeButton = Upgrade(x, y, "notexture.png", void)
        upgrades.append(upgradeButton)


def TryBuy(item, cost):
    boolean = True
    for i in range(0, len(item)):
        if cost[i] > item[i]:
            boolean = False
    return boolean

# farmerUpgrade
def upgradeI(onIt, click):
    if onIt:
        text = "Unlock farmers.. duh."
        DrawText("Farmer Upgrade(I)", 320, 320, 40, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        DrawText(text, 320, 350, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        DrawText("Cost:", 120, 390, 15, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        if upgrades[0].bought == True:
            DrawText("Bought!", 120, 430, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        else:
            DrawText("100 Elixir", 120, 430, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
            if click:
                global elixir
                CanBuy = TryBuy([elixir], [100])
                if CanBuy:
                    elixir -= 100
                    upgrades[0].bought = True


# builderUpgrade
def upgradeII(onIt, click):
    if onIt:
        text = "Unlock Builders duh."
        DrawText("Builders Upgrade(II)", 320, 320, 40, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        DrawText(text, 320, 350, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        DrawText("Cost:", 120, 390, 15, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        if upgrades[1].bought == True:
            DrawText("Bought!", 120, 430, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        else:
            DrawText("100 Ouire", 120, 430, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
            if click:
                global Ouire
                CanBuy = TryBuy([Ouire], [100])
                if CanBuy:
                    Ouire -= 100
                    upgrades[1].bought = True


# healerUpgrade
def upgradeIII(onIt, click):
    if onIt:
        text = "Unlock Healers."
        DrawText("Healer Upgrade(III)", 320, 320, 40, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        DrawText(text, 320, 350, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        DrawText("Cost:", 120, 390, 15, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        if upgrades[2].bought == True:
            DrawText("Bought!", 120, 430, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        else:
            DrawText("10000 Ouire", 120, 430, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
            if click:
                global Ouire
                CanBuy = TryBuy([Ouire], [10000])
                if CanBuy:
                    Ouire -= 10000
                    upgrades[2].bought = True

def UpgradeBaseEl(click, text, text2, text3, i, cost, maxlvl):
    DrawText(text3, 320, 320, 40, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText(text, 320, 350, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText("Cost:", 120, 390, 15, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText(text2, 320, 380, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText(str(cost) + " Elixir", 120, 430, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText("Lvl " + str(upgrades[i].lvl) , 480, 430, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    if click:
        global elixir
        CanBuy = TryBuy([elixir], [cost]) and (upgrades[i].lvl < maxlvl)
        if CanBuy:
            elixir -= cost
            upgrades[i].bought = True
            upgrades[i].lvl +=1
    if not (upgrades[i].lvl < maxlvl):
        DrawText("Maxed!" , 480, 470, 10, 'bigblueterm437nerdfont', 200, 200, 200, 1)

def UpgradeBaseOu(click, text, text2, text3, i, cost, maxlvl):
    DrawText(text3, 320, 320, 40, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText(text, 320, 350, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText("Cost:", 120, 390, 15, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText(text2, 320, 380, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText(str(cost) + " Ouire", 120, 430, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    DrawText("Lvl " + str(upgrades[i].lvl) , 480, 430, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
    if click:
        global Ouire
        CanBuy = TryBuy([Ouire], [cost]) and (upgrades[i].lvl < maxlvl)
        if CanBuy:
            Ouire -= cost
            upgrades[i].bought = True
            upgrades[i].lvl +=1
    if not (upgrades[i].lvl < maxlvl):
        DrawText("Maxed!" , 480, 470, 10, 'bigblueterm437nerdfont', 200, 200, 200, 1)





# OidElixirUpgrade
def upgradeIV(onIt, click):
    if onIt:
        cost = BigNumber(1,2)*BigNumber(1,1)**(upgrades[3].lvl+1)
        text = "More elixir.!"
        text2 = "Elixir 1.5x"
        text3 = "Elixir Upgrade 1(IV)"
        UpgradeBaseEl(click, text, text2, text3, 3, cost, 10)
    
# OidElixirUpgrade
def upgradeV(onIt, click):
    if onIt:
        cost = BigNumber(1,10)*BigNumber(1,3)**(upgrades[4].lvl+1)
        text = "Even more elixir!"
        text2 = "Elixir 2x"
        text3 = "Elixir Upgrade 2(V)"
        UpgradeBaseEl(click, text, text2, text3, 4, cost, 5)

# OidElixirUpgrade
def upgradeVI(onIt, click):
    if onIt:
        cost = BigNumber(1,20)*(upgrades[5].lvl+1)
        text = "Even more elixir..!"
        text2 = "Elixir 2.5x"
        text3 = "Elixir Upgrade 2(VI)"
        UpgradeBaseEl(click, text, text2, text3, 5, cost, 5)
                
# OuireUpgrade
def upgradeVII(onIt, click):
    if onIt:
        text = "more Ouire!"
        text2 = "Ouire 10x"
        DrawText("Ouire Upgrade 1(VII)", 320, 320, 40, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        DrawText(text, 320, 350, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        DrawText("Cost:", 120, 390, 15, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        DrawText(text2, 320, 380, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        if upgrades[6].bought == True:
            DrawText("Bought!", 120, 430, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        else:
            DrawText("1e50 Elixir", 120, 430, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
            if click:
                global elixir
                CanBuy = TryBuy([elixir], [BigNumber(1,50)])
                if CanBuy:
                    elixir -= BigNumber(1,50)
                    upgrades[6].bought = True

# OuireUpgrade
def upgradeVIII(onIt, click):
    if onIt:
        text = "even more Ouire!"
        text2 = "Ouire 10x"
        DrawText("Ouire Upgrade 2(VIII)", 320, 320, 40, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        DrawText(text, 320, 350, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        DrawText("Cost:", 120, 390, 15, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        DrawText(text2, 320, 380, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        if upgrades[7].bought == True:
            DrawText("Bought!", 120, 430, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        else:
            DrawText("1e100 Elixir", 120, 430, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
            if click:
                global elixir
                CanBuy = TryBuy([elixir], [BigNumber(1,100)])
                if CanBuy:
                    elixir -= BigNumber(1,100)
                    upgrades[7].bought = True

# OuireUpgrade
def upgradeIX(onIt, click):
    if onIt:
        text = "MOREEEEE Ouire!"
        text2 = "Ouire 10x"
        DrawText("Ouire Upgrade 1(IX)", 320, 320, 40, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        DrawText(text, 320, 350, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        DrawText("Cost:", 120, 390, 15, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        DrawText(text2, 320, 380, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        if upgrades[8].bought == True:
            DrawText("Bought!", 120, 430, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        else:
            DrawText("1e150 Elixir", 120, 430, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
            if click:
                global elixir
                CanBuy = TryBuy([elixir], [BigNumber(1,150)])
                if CanBuy:
                    elixir -= BigNumber(1,150)
                    upgrades[8].bought = True

# OuireUpgrade
def upgradeX(onIt, click):
    if onIt:
        text = "Sounds like cheating."
        text2 = "Oibs 3x"
        DrawText("Elixir Efficiency(X)", 320, 320, 40, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        DrawText(text, 320, 350, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        DrawText("Cost:", 120, 390, 15, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        DrawText(text2, 320, 380, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        if upgrades[9].bought == True:
            DrawText("Bought!", 120, 430, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        else:
            DrawText("1e250 Ouire", 120, 430, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
            if click:
                global Ouire
                CanBuy = TryBuy([Ouire], [BigNumber(1,250)])
                if CanBuy:
                    Ouire -= BigNumber(1,250)
                    upgrades[9].bought = True

# OuireUpgrade
def upgradeXX(onIt, click):
    if onIt:
        text = "I hope you dont regret this."
        text2 = "Unlock Arcanists.. and.. ??"
        DrawText("Arcanist Upgrade(XX)", 320, 320, 40, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        DrawText(text, 320, 350, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        DrawText("Cost:", 120, 390, 15, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        DrawText(text2, 320, 380, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        if upgrades[19].bought == True:
            DrawText("Bought!", 120, 430, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
        else:
            DrawText("1e250 Ouire", 120, 430, 13, 'bigblueterm437nerdfont', 200, 200, 200, 1)
            if click:
                global Ouire
                CanBuy = TryBuy([Ouire], [BigNumber(1,250)])
                if CanBuy:
                    Ouire -= BigNumber(1,50)
                    upgrades[19].bought = True

def CalculateElixirMultiplier():
    elx = BigNumber(1,0)
    if upgrades[3].bought == True:
        elx *= BigNumber(1.5,0)**(upgrades[3].lvl)
    if upgrades[4].bought == True:
        elx *= BigNumber(2,0)**(upgrades[4].lvl)
    if upgrades[5].bought == True:
        elx *= BigNumber(2.5,0)**(upgrades[5].lvl)
    global elxMultiplier
    elxMultiplier = elx

def CalculateOuireMultiplier():
    oir = BigNumber(1,0)
    if upgrades[6].bought == True:
        oir *= 2
    if upgrades[7].bought == True:
        oir *= 4
    if upgrades[8].bought == True:
        oir *= 10
    global ouireMultiplier
    ouireMultiplier = oir

def CalculateOibMultiplier():
    oibx = BigNumber(1,0)
    if upgrades[9].bought == True:
        oibx *= 2

    global oibMultiplier
    oibMultiplier = oibx
    


upgradePngs = [
    "farmerUpgrade.png",
    "builderUpgrade.png",
    "healerUpgrade.png",
    "elixirUpgradeI.png",
    "elixirUpgradeII.png",
    "elixirUpgradeIII.png",
    "OuireUpgradeI.png",
    "OuireUpgradeII.png",
    "OuireUpgradeIII.png",
    "elixirEfficiencyI.png"
]

upgradeFunctions = [
    upgradeI, upgradeII, 
    upgradeIII, upgradeIV,
    upgradeV, upgradeVI,
    upgradeVII, upgradeVIII,
    upgradeIX, upgradeX
    ]


def UpgradesInitialize():
    for i in range(0, len(upgradePngs)):
        upgrades[i].png = upgradePngs[i]
        upgrades[i].func = upgradeFunctions[i]


def DisplayUpgrades():
    for i in range(0, len(upgrades)):
        upgrade = upgrades[i]
        upgrade.DoUpgrade()


tabs = [JobsTab, BuildingsTab, UpgradesTab]
# Job Stuff
JobTabs = [DisplayHunter, DisplayFarmer, DisplayHealer, DisplayBuilder, DisplayWarrior, DisplayWarrior]
JobPriorities = [10, 0, 0, 0]
OidInJob = [BigNumber(0, 0), BigNumber(0, 0), BigNumber(0, 0), BigNumber(0, 0)]
displayJobPointer = 0
tabpointer = 0
JobsList = [0, 1, 2, 3, 4, 5]
# upgrade tab stuff
upgrades = []
# Resources
Oids = BigNumber(1,2)
elixir = BigNumber(0)
health = BigNumber(0)
Ouire = BigNumber(0)
tick = 0
Land = BigNumber(0)
JobEfficiency = BigNumber(0)
Buildings = BigNumber(0)
tickset = [10]
run = True
## multipliers
elxMultiplier = 1
oibMultiplier = 1
ouireMultiplier = 1
# initialize
LoadSave()
clicked = False
if tick == 0:
    UpgradesCreate(10, 176, 200, 10, 32, 32)
    UpgradesInitialize()

while run:
    timer = time.perf_counter()
    clicked = False
    for events in pygame.event.get():
        if events.type == pygame.MOUSEBUTTONDOWN:
            clicked = True
        if events.type == pygame.QUIT:
            run = False
    CalculateElixirMultiplier()
    CalculateOuireMultiplier()
    CalculateOibMultiplier()
    win.fill((25, 20, 25))
    DrawImage(320, 32, "upperTab.png", 0)
    Button(
        32, 32, 64, 64, "buildings.png", "button.png", "buttonHighlighted.png", ChangeToBuilding
    )
    Button(96, 32, 64, 64, "job.png", "button.png", "buttonHighlighted.png", ChangeToJobs)
    Button(
        160, 32, 64, 64, "upgrades.png", "button.png", "buttonHighlighted.png", ChangeToUpgrades
    )
    Tab = tabs[tabpointer]
    NewOids()
    OidChangeJobs()
    OidDoJobs()
    
    Tab()
    tick += 1
    pygame.display.update()


    tsmin = 0.05 - (time.perf_counter() - timer)
    if tsmin >= 0:
        time.sleep(tsmin)
Save()
pygame.quit()
