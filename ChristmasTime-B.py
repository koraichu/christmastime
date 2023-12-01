import datetime
import time
import os

one = [
"   █   ",
"  ██   ",
" █ █   ",
"   █   ",
"   █   ",
"███████"
]

two = [
"██████ ",
"      █",
" █████ ",
"█      ",
"█      ",
"███████"
]

thr = [
"██████ ",
"      █",
"  ████ ",
"      █",
"      █",
"██████ "
]

fou = [
"█     █",
"█     █",
"███████",
"      █",
"      █",
"      █"
]

fiv = [
"███████",
"█      ",
"██████ ",
"      █",
"      █",
"██████ "
]

six = [
" █████ ",
"█      ",
"██████ ",
"█     █",
"█     █",
" █████ "
]

sev = [
"███████",
"      █",
"     █ ",
"    █  ",
"   █   ",
"  █    "
]

eig = [
" █████ ",
"█     █",
" █████ ",
"█     █",
"█     █",
" █████ "
]

nin = [
" █████ ",
"█     █",
" ██████",
"      █",
"█     █",
" █████ "
]

zro = [
" █████ ",
"█     █",
"█     █",
"█     █",
"█     █",
" █████ "
]

bnk = [
" █████ ",
"█     █",
"█     █",
"█     █",
"█     █",
" █████ "
]

def main():
    today = datetime.date.today()
    future = datetime.date(2023,12,25)
    diff = future-today
    diffstr = str(diff.days)

    a = (diffstr)[0]
    if a == '1':
        a = one
    if a == '2':
        a = two
    if a == '3':
        a = thr
    if a == '4':
        a = fou
    if a == '5':
        a = fiv
    if a == '6':
        a = six
    if a == '7':
        a = sev
    if a == '8':
        a = eig
    if a == '9':
        a = nin
    if a == '0':
        a = zro
    if a == '':
        a = bnk    

    b = (diffstr)[1]
    if b == '1':
        b = one
    if b == '2':
        b = two
    if b == '3':
        b = thr
    if b == '4':
        b = fou
    if b == '5':
        b = fiv
    if b == '6':
        b = six
    if b == '7':
        b = sev
    if b == '8':
        b = eig
    if b == '9':
        b = nin
    if b == '0':
        b = zro
    if b == '':
        b = bnk


    print("   There are")
    for line1, line2 in zip(a, b):
        print (line1, " ", line2)
    print("days to Christmas!")
    print("")
    input("Press [RETURN] to exit.")

main()
