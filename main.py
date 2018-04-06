from termcolor import colored
import time
q = 0
x = float(.25/2)
print (colored('                            ____________','cyan'))
time.sleep(x/2)
print (colored('                            \|M  A  I  N|\ ','cyan'))
time.sleep(x/2)
print (colored('                             \|-=-=-=-=-=|\ ','cyan'))
time.sleep(x/2)
print (colored('                              \|M  E  N  U|\ ','cyan'))
time.sleep(x/2)
print (colored('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|', 'cyan'))
time.sleep(x)
print (colored('|   AREA   |||||||| PERIMITER |||||||| SURFACE AREA  ||||||||    VOLUME   ||||||||', 'cyan'))
time.sleep(x)
print (colored('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|', 'cyan'))
time.sleep(x)
print (colored('|  SQUARE  | 1.01 |   SQUARE  | 2.01 |      CUBE     | 3.01 |     CUBE    | 4.01 |', 'cyan'))
time.sleep(x)
print (colored('|++++++++++|++++++|+++++++++++|++++++|+++++++++++++++|++++++|+++++++++++++|++++++|', 'cyan'))
time.sleep(x)
print (colored('| TRIANGLE | 1.02 |  TRIANGLE | 2.02 |  RECTANGULAR  | 3.02 | RECTANGULAR | 4.02 |', 'cyan'))
time.sleep(x)
print (colored('|          |      |           |      |     PRISM     |      |    PRISM    |      |', 'cyan'))
time.sleep(x)
print (colored('|++++++++++|++++++|+++++++++++|++++++|+++++++++++++++|++++++|+++++++++++++|++++++|', 'cyan'))
time.sleep(x)
print (colored('|  CIRCLE  | 1.03 |   CIRCLE  | 2.03 |   TRIANGULAR  | 3.03 |  TRIANGULAR | 4.03 |', 'cyan'))
time.sleep(x)
print (colored('|          |      |           |      |     PRISM     |      |    PRISM    |      |', 'cyan'))
time.sleep(x)
print (colored('|++++++++++|++++++|+++++++++++|++++++|+++++++++++++++|++++++|+++++++++++++|++++++|', 'cyan'))
time.sleep(x)
print (colored('|    TBA   | 1.04 |    TBA    | 2.04 |      CONE     | 3.04 |     CONE    | 4.04 |', 'cyan'))
time.sleep(x)
print (colored('|++++++++++|++++++|+++++++++++|++++++|+++++++++++++++|++++++|+++++++++++++|++++++|', 'cyan'))
time.sleep(x)
print (colored('|    TBA   | 1.05 |    TBA    | 2.05 |  RECTANGULAR  | 3.05 | RECTANGULAR | 4.05 |', 'cyan'))
time.sleep(x)
print (colored('|          |      |           |      |    PYRAMID    |      |  PYRAMID    |      |', 'cyan'))
time.sleep(x)
print (colored('|++++++++++|++++++|+++++++++++|++++++|+++++++++++++++|++++++|+++++++++++++|++++++|', 'cyan'))
time.sleep(x)
print (colored('|    TBA   | 1.06 |    TBA    | 2.06 |   TRIANGULAR  | 3.06 |  TRIANGULAR | 4.06 |', 'cyan'))
time.sleep(x)
print (colored('|          |      |           |      |    PYRAMID    |      |   PYRAMID   |      |', 'cyan'))
time.sleep(x)
print (colored('|++++++++++|++++++|+++++++++++|++++++|+++++++++++++++|++++++|+++++++++++++|++++++|', 'cyan'))
time.sleep(x)
print (colored('|    TBA   | 1.07 |    TBA    | 2.07 |     SPHERE    | 3.07 |    SPHERE   | 4.07 |', 'cyan'))
time.sleep(x)
print (colored('|-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=|', 'cyan'))
time.sleep(x)
print (colored('|      OTHER      ||||||||','cyan'))
time.sleep(x)
print (colored('|-=-=-=-=-=-=-=-=-=-=-=-=|','cyan'))
time.sleep(x)
print (colored('|     VARIBLES    | 0.01 |','cyan'))
time.sleep(x)
print (colored('|   TRANSLATION   |      |','cyan'))
time.sleep(x)
print (colored('|++++++++++++++++++++++++|','cyan'))
time.sleep(x)
print (colored('| EQUATIONS  USED | 0.02 |','cyan'))
time.sleep(x)
print (colored('|++++++++++++++++++++++++|','cyan'))
time.sleep(x)
print (colored('|      EXIT       | 0.03 |','cyan'))
time.sleep(x)
print (colored('|-=-=-=-=-=-=-=-=-=-=-=-=|','cyan'))
while q<1:
	pi = float(3.14159)
	x = float(x/2)
	a = float(input())
	x1 = float(1)
	
	#area of square
	if a == 1.01:
		print(colored('a = l * w', 'yellow'))
		l = float(input('l = '))
		w = float(input('w = '))
		a = float(l * w)
		a = str(a)
		print (colored('a = ' + a, 'green'))
		time.sleep(x1)
	
	#area of triangle
	elif a == 1.02:
		print(colored('a = (h * b)/2','yellow'))
		h = float(input('h = '))
		b = float(input('b = '))
		a = (h*b)/2
		a = str(a)
		print (colored('a = ' + a, 'green'))
		time.sleep(x1)
	
	#area of circle
	elif a == 1.03:
		print(colored('a = pi * r ^ 2','yellow'))
		r = float(input('h = '))
		a = pi * r **2
		a = str(a)
		print (colored('a = ' + a,'green'))
	
 #	------------------------------------------------
	
	#perimiter of squrae
	elif a == 2.01:
		print(colored('p = (2 * l) + (2 * w)', 'yellow'))
		l = float(input('l = '))
		w = float(input('w = '))
		p = float((2*l) + (2*w))
		p = str(p)
		print(colored('p = ' + p, 'green'))
		time.sleep(x1)
	
	#perimiter of triangle
	elif a == 2.02:
		print(colored(' p = 3*s','yellow'))
		s = float(input('s = '))
		p = s*3
		p = str(p)
		print(colored('p = ' + p, 'green'))
		time.sleep(x1)
	
	#perimiter of circle
	elif a == 2.03:
		print(colored('p = 2 * pi* r','yellow'))
		r = float(input('r = '))
		p = 2 * pi * r
		p = str(p)
		print('p = ' + p,'green')
		time.sleep(x1)
	
 #	------------------------------------------------
	
	#surface area of cube
	elif a == 3.01:
		print(colored('sa = 6 * s ^ 2','yellow'))
		s = float(input('s = '))
		sa = float(6*s**2)
		sa = str(sa)
		print(colored('sa = ' + sa, 'green'))
		time.sleep(x1)
	
	#surface area of rectangular prism
	elif a == 3.02:
		print(colored('sa = 2 * (w * l + h * l + h * w)  ','yellow'))
		w = float(input('w = '))
		l = float(input('l = '))
		h = float(input('h = '))
		sa = 2*(w*l+h*l+h*w)
		sa = str(a)
		print (colored('sa = ' + sa, 'green'))
		time.sleep(x1)
		
	#surface area of triangular prisim
	elif a == 3.03:
		print('wip')
		time.sleep(x1)
	
 #	------------------------------------------------
	
	#volume of cube
	elif a == 4.01:
		print(colored('v = l * w * h','yellow'))
		l = float(input('l = '))
		w = float(input('w = '))
		h = float(input('h = '))
		v = l*w*h
		v = str(v)
		print(colored('v = ' + v, 'green'))
		time.sleep(x1)
		
	#volume of rectangular prisim
	elif a == 4.02:
		print(colored('v = w * l * h','yellow'))
		w = float(input('w = '))
		l = float(input('l = '))
		h = float(input('h = '))
		v = w*l*h
		v = str(v)
		print(colored('v = ' + v, 'green'))
		time.sleep(x1)
		
	#volume of triangular prisim
	elif a == 4.03:
		print('wip')
		time.sleep(x1)
	
 #	------------------------------------------------
	
	#varible translation
	elif a == 0.01:
		print('wip')
		time.sleep(x1)
		
 #	------------------------------------------------
	
	#equations used
	elif a == 0.02:
		print(colored('v = l * w * h','yellow'))
		print(colored('a = l * w', 'yellow'))
		print(colored('a = l * w', 'yellow'))
		print(colored('sa = 6 * s ^ 2','yellow'))
		print(colored('p = (2 * l) + (2 * w)', 'yellow'))
		time.sleep(x1)
	
	elif a == 0.03:
		print(colored('shuting','red'))
		time.sleep(1)
		print(colored('down','red'))
		time.sleep(1)
		q = q + 1
	
 #	------------------------------------------------
 
	else:
		print (colored("that input is not listed or incorect. please try again.","red"))
		time.sleep(x1)
