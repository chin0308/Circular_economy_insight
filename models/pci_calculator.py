def calculate_pci(events):
    reuse = events.count('Resold')
    refurb = events.count('Refurbished')
    recycle = events.count('Recycled')
    total = len(events)
    if total == 0:
        return 0
    pci = (reuse + refurb + recycle) / total
    return round(pci, 3)
