from djchoices import ChoiceItem, DjangoChoices

class BicycleCategory(DjangoChoices):
    Gents = ChoiceItem("gents")
    Ladies = ChoiceItem("ladies")
    Kids = ChoiceItem("kids")
    Electric = ChoiceItem("electric")
    Folding = ChoiceItem("folding")
    RangerPlain = ChoiceItem("rangerPlain")
    RangerSuspension = ChoiceItem("rangerSuspension")
    RangerGear = ChoiceItem("rangerGear")

class BicycleSize(DjangoChoices):
    S_16175 = ChoiceItem("16.175")
    S_20175 = ChoiceItem("20.175")
    S_24175 = ChoiceItem("24.175")
    S_26150 = ChoiceItem("26.150")
    S_26175 = ChoiceItem("26.175")
    S_26235 = ChoiceItem("26.235")
    S_26300 = ChoiceItem("26.300")
    S_26400 = ChoiceItem("26.400")
    S_28150 = ChoiceItem("28.150")
    S_27114 = ChoiceItem("27.114")
    S_Universal = ChoiceItem("universal")

class BicycleBrand(DjangoChoices):
    Atlas = ChoiceItem("atlas")
    Avon = ChoiceItem("avon")
    BSA = ChoiceItem("bsa")
    Hercules = ChoiceItem("hercules")
    Hero = ChoiceItem("hero")
    Kross = ChoiceItem("kross")
    SkBikes = ChoiceItem("skBikes")
    Tuvox = ChoiceItem("tuvox")
    Other = ChoiceItem("other")

class BicycleAccessoriesCategory(DjangoChoices):
    Locks = ChoiceItem("locks")
    Lights = ChoiceItem("lights")
    Helmets = ChoiceItem("helmets")
    Bells = ChoiceItem("bells")
    Horns = ChoiceItem("horns")
    Reflectors = ChoiceItem("reflectors")
    Mudguards = ChoiceItem("mudguards")
    Stands = ChoiceItem("stands")
    Carriers = ChoiceItem("carriers")
    Baskets = ChoiceItem("baskets")
    Tyre = ChoiceItem("tyre")
    Tube = ChoiceItem("tube")
    Rim = ChoiceItem("rim")
    Chain = ChoiceItem("chain")
    Freewheel = ChoiceItem("freewheel")
    ChainWheel = ChoiceItem("chainWheel")
    Spoke = ChoiceItem("spoke")
    HandleBar = ChoiceItem("handleBar")
    Saddle = ChoiceItem("saddle")
    Paddle = ChoiceItem("paddle")

class BicycleAccessoriesBrand(DjangoChoices):
    Bhogal = ChoiceItem("bhogal")
    Masco = ChoiceItem("masco")
    Ramous = ChoiceItem("ramous")
    Trax = ChoiceItem("trax")
    BM = ChoiceItem("bm")
    KW = ChoiceItem("kw")
    Nelco = ChoiceItem("nelco")
    Other = ChoiceItem("other")