
def getBondDuration(y, face, couponRate, m, ppy = 1):
    SumProduct = 0
    pvcfsum = 0

    if ppy == 1:
        cf = face * couponRate
        for i in range(1, m + 1):
            pvcf = cf * (1 + y) ** -i
            if i == m:
                pvcf = pvcf + (face * (1 + y) ** -m)
            pvcfsum = pvcfsum + pvcf
            SumProduct = SumProduct + i * pvcf
        duration = SumProduct / pvcfsum

    else:
        y = y / ppy
        couponRate = couponRate / ppy
        m = m * ppy
        cf = face * couponRate
        for i in range(1, m + 1):
            pvcf = cf * (1 + y) ** -i
            if i == m:
                pvcf = pvcf + (face * (1 + y) ** -m)
            pvcfsum = pvcfsum + pvcf
            SumProduct = SumProduct + i * pvcf
        duration = (SumProduct / pvcfsum) / ppy     

    return duration
