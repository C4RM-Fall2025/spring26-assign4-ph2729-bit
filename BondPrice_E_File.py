

def getBondPrice_E(face, couponRate, yc):
    pvcfsum = 0
    cf = face * couponRate
    for i, y in enumerate(yc):
        pvcf = cf * (1 + y) ** -(i + 1)
        if (i + 1) == len(yc):
            pvcf = pvcf + face * (1 + y) ** -(i + 1)
        pvcfsum = pvcfsum + pvcf

    return(pvcfsum)

