T = int(raw_input())

for i in range(0, T):
	string = raw_input()
	number = 0
	string1 = "WWBWW"
	number += string.count(string1)*4
	string = string.replace(string1, "XXXXX")

	string2, string3 = "WWBW", "WBWW"
	number += string.count(string2)*3
	string = string.replace(string2, "XXXX")
	number += string.count(string3)*3
	string = string.replace(string3, "XXXX")

	string4, string5, string6 = "WBW", "WWB", "BWW"
	number += string.count(string4)*2
	string = string.replace(string4, "XXX")
	number += string.count(string5)*2
	string = string.replace(string5, "XXX")
	number += string.count(string6)*2
	string = string.replace(string6, "XXX")

	string7, string8 = "WB", "BW"
	number += string.count(string7)
	string = string.replace(string7, "XX")
	number += string.count(string8)
	string = string.replace(string8, "XX")

	print number