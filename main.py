def palindrom_sonlar(ro'yxat):
    return [son for son in ro'yxat if str(son) == str(son)[::-1]]

print(palindrom_sonlar([121, 344, 123, 454]))  # [121, 454]
