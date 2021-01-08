recipieName = input("enter recipie name: ")
thickness = input("Enter 20T or 30T: ")
batchCount = int(input("batch count: "))

def promptMaterial():
    addMat = input("add material? y/n: ")
    if addMat == "y":
        newMaterial()


def newMaterial():
    matVendor = input("material vendor: ")  
    matType = input("material type: ")
    matSize = input("material size: ")
    bagWeight = int(input("bag weight in kg: "))
    mix1 = int(input("mix1: "))
    mix2 = int(input("mix2: "))
    mix3 = int(input("mix3: "))
    mix4 = int(input("mix4: "))
    mixBatch = mix1 + mix2 + mix3 + mix4
    mixTotal = mixBatch * batchCount
    bagCount = mixTotal / bagWeight
    print(f"{bagCount} bags | {matVendor} {matType} {matSize} @ {bagWeight}kg | {mixBatch}kg/batch | Total:{mixTotal}kg")
    
    promptMaterial()

promptMaterial()



