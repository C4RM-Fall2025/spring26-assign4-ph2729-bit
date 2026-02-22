

def getBondPrice_Z(face, couponRate, times, yc):
    pvcfsum = 0
    cf = face * couponRate
    for i, y in zip(times, yc):
        pvcf = cf * (1 + y) ** -i
        if i == times[-1]:
            pvcf = pvcf + face * (1 + y) ** -i
        pvcfsum = pvcfsum + pvcf

    return(pvcfsum)    

