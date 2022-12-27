#STRING METODLARI - strip()

gel_yaz = "  gelecegi_yazanlar  "

print(gel_yaz.strip())

gel_yaz = "*gelecegi_yazanlar*"
print(gel_yaz.strip("*"))

gel_yaz = "Cgelecegi_yazanlarC"
print(gel_yaz.strip("C"))