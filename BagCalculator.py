print ("enter information...")

batches = int(input("batch count: "))

def addMat(batches):
    material = list()

    while True:
        matVendor = input("vendor: ")
        matType = input("material type: ")
        matSize = input("material size: ")
        bagWeight = int(input("bag weight: "))
        mix1 = int(input("mix 1: "))
        mix2 = int(input("mix 2: "))
        mix3 = int(input("mix 3: "))
        mix4 = int(input("mix 4: "))
        mixBatch = mix1 + mix2 + mix3 + mix4
        mixTotal = mixBatch * batches
        bagCount = mixTotal / bagWeight
        bagWeightStr = str(bagWeight)
        mixBatchStr = str(mixBatch)
        mixTotalStr = str(mixTotal)
        bagCountStr = str(bagCount)

        materialInfo = [matVendor, matType, matSize, bagWeightStr, mixBatchStr, mixTotalStr, bagCountStr]
        material.append(materialInfo)

        if input("repeat? y/n: ") != "y":
            break

    for i in range(len(material)):
        print(f"Material {i+1}: {materialInfo[6]} bags | {materialInfo[0]} | {materialInfo[1]} | {materialInfo[2]} | {materialInfo[3]}kg | {materialInfo[4]}kg/batch | Total: {materialInfo[5]}")



addMat(batches)

                

        

