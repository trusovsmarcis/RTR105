#!/usr/bin/python
# -*- coding: utf-8 -*-

a = input("Cien. lietotāj, lūdzu, ievadi skaitli: ")
# 3. pythonā visi input rezultāti ir ar str datu tipu
# tapēc ievadītā lieluma datu tips vēlāk ie jāparveido
a = int(a)
print("Liet., Tu esi ievadījis skaitli: ")
aa = a * a
print("Tavs skaitlis kvadrātā ir: %d"%(aa))
