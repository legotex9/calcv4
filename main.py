from termcolor import colored
import time
import replit
q = 0
while q<1:
	x = float(.25/2)
	pi = int(3.14159)
	print (colored("                            ____________","cyan"))
	time.sleep(x/2)
	print (colored("                            \|M  A  I  N|\ ","cyan"))
	time.sleep(x/2)
	print (colored("                             \|-=-=-=-=-=|\ ","cyan"))
	time.sleep(x/2)
	print (colored("                              \|M  E  N  U|\ ","cyan"))
	time.sleep(x/2)
	print (colored("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|", "cyan"))
	time.sleep(x)
	print (colored("|   AREA   |||||| PERIMITER |||||| SURFACE AREA  ||||||    VOLUME   ||||||", "cyan"))
	time.sleep(x)
	print (colored("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|", "cyan"))
	time.sleep(x)
	print (colored("|  SQUARE  | 01 |   SQUARE  | 02 |      CUBE     | 03 |     CUBE    | 04 |", "cyan"))
	time.sleep(x)
	print (colored("|++++++++++|++++|+++++++++++|++++|+++++++++++++++|++++|+++++++++++++|++++|", "cyan"))
	time.sleep(x)
	print (colored("| TRIANGLE | 05 |  TRIANGLE | 06 |  RECTANGULAR  | 07 | RECTANGULAR | 08 |", "cyan"))
	time.sleep(x)
	print (colored("|          |    |           |    |     PRISM     |    |    PRISM    |    |", "cyan"))
	time.sleep(x)
	print (colored("|++++++++++|++++|+++++++++++|++++|+++++++++++++++|++++|+++++++++++++|++++|", "cyan"))
	time.sleep(x)
	print (colored("|  CIRCLE  | 09 |   CIRCLE  | 10 |   TRIANGULAR  | 11 |  TRIANGULAR | 12 |", "cyan"))
	time.sleep(x)
	print (colored("|          |    |           |    |     PRISM     |    |    PRISM    |    |", "cyan"))
	time.sleep(x)
	print (colored("|++++++++++|++++|+++++++++++|++++|+++++++++++++++|++++|+++++++++++++|++++|", "cyan"))
	time.sleep(x)
	print (colored("|    TBA   | 13 |    TBA    | 14 |      CONE     | 15 |     CONE    | 16 |", "cyan"))
	time.sleep(x)
	print (colored("|++++++++++|++++|+++++++++++|++++|+++++++++++++++|++++|+++++++++++++|++++|", "cyan"))
	time.sleep(x)
	print (colored("|    TBA   | 17 |    TBA    | 18 |  RECTANGULAR  | 19 | RECTANGULAR | 20 |", "cyan"))
	time.sleep(x)
	print (colored("|          |    |           |    |    PYRAMID    |    |  PYRAMID    |    |", "cyan"))
	time.sleep(x)
	print (colored("|++++++++++|++++|+++++++++++|++++|+++++++++++++++|++++|+++++++++++++|++++|", "cyan"))
	time.sleep(x)
	print (colored("|    TBA   | 21 |    TBA    | 22 |   TRIANGULAR  | 23 |  TRIANGULAR | 24 |", "cyan"))
	time.sleep(x)
	print (colored("|          |    |           |    |    PYRAMID    |    |   PYRAMID   |    |", "cyan"))
	time.sleep(x)
	print (colored("|++++++++++|++++|+++++++++++|++++|+++++++++++++++|++++|+++++++++++++|++++|", "cyan"))
	time.sleep(x)
	print (colored("|    TBA   | 25 |    TBA    | 26 |     SPHERE    | 27 |    SPHERE   | 28 |", "cyan"))
	time.sleep(x)
	print (colored("|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|", "cyan"))
	time.sleep(x)
	x = float(x/2)
	print (colored("|      OTHER      ||||||","cyan"))
	time.sleep(x)
	print (colored("|-=-=-=-=-=-=-=-=-=-=-=|","cyan"))
	time.sleep(x)
	print (colored("|     VARIBLES    | VT |","cyan"))
	time.sleep(x)
	print (colored("|   TRANSLATION   |    |","cyan"))
	time.sleep(x)
	print (colored("|++++++++++++++++++++++|","cyan"))
	time.sleep(x)
	print (colored("| EQUATIONS  USED | EQ |","cyan"))
	time.sleep(x)
	print (colored("|      EXIT       |EXIT|","cyan"))
    time.sleep(x)
    print (colored("|++++++++++++++++++++++|","cyan"))
	time.sleep(x)
	print (colored("|-=-=-=-=-=-=-=-=-=-=-=|","cyan"))
	a = input()
	x1 = float(1)
	#area of square
	if a == "1" or a == "01":
		print(colored("a = l * w", "yellow"))
		l = float(input("l = "))
		w = float(input("w = "))
		a = float(l * w)
		a = str(a)
		print (colored("a = " + a, "green"))
		time.sleep(x1)
	#perimiter of squrae
	elif a == "2" or a == "02":
		print(colored("p = (2 * l) + (2 * w)", "yellow"))
		l = float(input("l = "))
		w = float(input("w = "))
		p = float((2*l) + (2*w))
		p = str(p)
		print(colored("p = " + p, "green"))
		time.sleep(x1)
	#surface area of cube
	elif a == "3" or a == "03":
		print(colored("sa = 6 * s ^ 2","yellow"))
		s = float(input("s = "))
		sa = float(6*s**2)
		sa = str(sa)
		print(colored("sa = " + sa, "green"))
		time.sleep(x1)
	#volume of cube
	elif a == "4" or a == "04":
		print(colored("v = l * w * h","yellow"))
		l = float(input("l = "))
		w = float(input("w = "))
		h = float(input("h = "))
		v = l*w*h
		v = str(v)
		print(colored("v = " + v, "green"))
		time.sleep(x1)
	#area of triangle
	elif a == "5" or a == "05":
		print(colored("a = (h * b)/2","yellow"))
		h = float(input("h = "))
		b = float(input("b = "))
		a = (h*b)/2
		a = str(a)
		print (colored("a = " + a, "green"))
		time.sleep(x1)
	#perimiter of triangle
	elif a == "6" or a == "06":
		print(colored(" p = 3*s","yellow"))
		s = float(input("s = "))
		p = s*3
		p = str(p)
		print(colored("p = " + p, "green"))
		time.sleep(x1)
	#surface area of rectangular prism
	elif a == "7" or a == "07":
		print(colored("sa = 2 * (w * l + h * l + h * w)  ","yellow"))
		w = float(input("w = "))
		l = float(input("l = "))
		h = float(input("h = "))
		sa = 2*(w*l+h*l+h*w)
		sa = str(a)
		print (colored("sa = " + sa, "green"))
	#volume of rectangular prisim
	elif a == "8" or a == "08":
		print("v = w * l * h","yellow")
		w = float(input("w = "))
		l = float(input("l = "))
		h = float(input("h = "))
		v = w*l*h
		v = str(v)
		print(colored("v = " + v, "green"))
	#area of circle
	elif a == "9" or a == "09":
		print("wip")
	#perimiter of circle
	elif a == "10":
		print("wip")
	#surface area of triangular prisim
	elif a == "11":
		print("wip")
	#volume of triangular prisim
	elif a == "12":
		print("wip")
	#tba
	elif a == "13":
		print("tba")
	#tba
	elif a == "14":
		print("tba")
	#surface area of cone
	elif a == "15":
		print("wip")
	#volume of cone
	elif a == "16":
		print("wip")
	#tba
	elif a == "17":
		print("tba")
	#tba
	elif a == "18":
		print("tba")
	#surface area of rectangular pyramid
	elif a == "19":
		print("wip")
	#volume of rectangular pyramid
	elif a == "20":
		print("wip")
	#tba
	elif a == "21":
		print("tba")
	#tba
	elif a == "22":
		print("tba")
	#surface area of triangular pyramid
	elif a == "23":
		print("wip")
	#volume of triangular pyramid
	elif a == "24":
		print("wip")
	#tba
	elif a == "25":
		print("tba")
	#tba
	elif a == "26":
		print("tba")
	#surface area of sphere
	elif a == "27":
		print("wip")
	#volume of sphere
	elif a == "28":
		print("wip")
	#varible translation
	elif a == "VT" or a == "vt":
		print("wip")
	#equations used
	elif a == "EQ" or a == "eq":
		print(colored("v = l * w * h","yellow"))
		print(colored("a = l * w", "yellow"))
		print(colored("a = l * w", "yellow"))
		print(colored("sa = 6 * s ^ 2","yellow"))
		print(colored("p = (2 * l) + (2 * w)", "yellow"))
	elif a == "exit" or a == "EXIT":
		print(colored("shuting","red"))
		time.sleep(1)
		print(colored("down","red"))
		q = q + 1
	elif a > "28" or 1 or a != "EQ" or a != "eq" or a != "VT" or a != "vt" or a != "EXIT" or a != "exit":
		print (colored(" what you enterd that is not listed. \n please try again", "red"))
		time.sleep(2)
		replit.clear()
