

def getBondPrice(y, face, couponRate, m, ppy=1):
    pvcfsum = 0
    if ppy == 1:
        cf = face * couponRate
        for i in range(1, m + 1):
            pvcf = cf * (1 + y) ** -i
            if i == m:
                pvcf = pvcf + face * (1 + y) ** -i
            pvcfsum = pvcfsum + pvcf 
    else:
        y = y / ppy
        couponRate = couponRate / ppy
        m = m * ppy
        cf = face * couponRate
        for i in range(1, m + 1):
            pvcf = cf * (1 + y) ** -i
            if i == m:
                pvcf = pvcf + face * (1 + y) ** -i
            pvcfsum = pvcfsum + pvcf        

    return pvcfsum


