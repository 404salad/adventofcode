import json

def convert_to_json(data):
    json_data = {}
    for i, row in enumerate(data, start=1):
        key = str(i)
        values = [entry.strip() for entry in row.split(';')]
        json_data[key] = values

    return json.dumps(json_data, indent=2)

data = [
"1: 13 green, 3 red; 4 red, 9 green, 4 blue; 9 green, 10 red, 2 blue",
"2: 3 red, 8 green, 1 blue; 4 green, 11 blue, 2 red; 3 blue, 2 red, 6 green; 5 green, 15 blue, 1 red; 2 blue, 2 red, 5 green; 12 blue, 7 green, 2 red",
"3: 1 red, 9 green, 3 blue; 8 green, 4 red, 11 blue; 6 red, 10 blue; 6 green, 6 red, 12 blue; 2 blue, 11 green, 7 red; 12 blue, 9 green, 8 red",
"4: 7 red, 2 green, 1 blue; 12 green; 12 green",
"5: 15 red, 3 green, 1 blue; 6 red, 2 blue, 2 green; 3 green, 3 red, 1 blue; 2 blue, 13 red, 5 green; 2 green, 15 red, 2 blue",
"6: 3 blue, 15 red, 1 green; 8 green, 5 red, 6 blue; 9 green, 5 blue, 6 red; 9 green, 3 blue, 9 red; 10 green, 14 red, 2 blue",
"7: 6 green, 1 red, 11 blue; 6 green, 1 red, 3 blue; 4 green, 20 blue; 2 red, 5 blue, 4 green; 10 green, 17 blue",
"8: 10 blue, 9 green, 10 red; 9 green, 1 red; 8 red, 9 green, 9 blue; 5 green, 3 red, 7 blue",
"9: 7 blue, 1 red; 5 red, 4 green; 4 green, 6 red, 5 blue; 2 green, 4 blue; 3 green, 6 blue, 4 red; 1 green, 3 red, 3 blue",
"10: 2 red, 2 green, 2 blue; 10 blue, 2 red, 1 green; 2 green, 9 blue, 3 red",
"11: 8 red, 4 blue, 1 green; 3 red; 1 green; 2 green, 3 blue",
"12: 10 red, 2 green, 4 blue; 4 red, 2 green; 1 blue, 1 red, 1 green; 10 red, 1 green, 5 blue",
"13: 20 blue, 9 green, 7 red; 13 red, 13 blue, 16 green; 17 blue, 6 red, 6 green; 1 red, 1 blue, 9 green; 9 blue, 18 green, 7 red",
"14: 6 blue, 14 red; 9 red, 8 blue; 2 red, 1 green, 8 blue; 3 blue, 1 green, 9 red; 8 blue, 2 green, 1 red",
"15: 3 red, 1 blue, 5 green; 2 red, 3 green; 5 red, 5 green, 1 blue; 2 green, 6 red; 4 red, 1 blue; 6 red, 1 blue, 1 green",
"16: 5 blue, 7 red, 2 green; 7 red, 12 blue; 10 blue, 11 green, 5 red; 11 red, 11 blue, 10 green",
"17: 3 red, 7 blue; 1 blue, 14 green, 4 red; 11 blue, 4 red, 11 green; 18 blue, 5 red, 11 green; 18 blue, 1 red, 8 green",
"18: 8 green, 2 red, 6 blue; 8 blue, 11 green; 2 red, 11 blue, 9 green",
"19: 11 red, 9 green, 3 blue; 19 green, 9 red, 2 blue; 19 green, 4 blue, 4 red; 1 green, 11 red; 10 red, 2 green, 4 blue",
"20: 2 blue, 3 red, 1 green; 1 red, 3 green; 7 blue, 1 green, 4 red; 1 red, 8 blue, 7 green; 6 blue, 3 red; 5 red, 3 blue, 7 green",
"21: 1 green, 1 blue, 10 red; 1 green, 5 red, 8 blue; 11 red, 4 blue; 6 blue, 6 red",
"22: 6 blue, 6 green; 8 green, 15 blue; 8 green, 3 blue, 1 red; 11 blue, 2 red, 7 green",
"23: 1 green, 3 blue, 7 red; 4 red, 1 green, 2 blue; 3 red, 2 blue, 2 green",
"24: 4 green, 8 blue, 4 red; 2 green, 9 blue; 4 green, 1 red; 2 green, 5 blue, 1 red; 2 blue, 3 red, 3 green; 6 blue",
"25: 7 blue; 15 blue, 5 red; 6 blue, 12 red; 1 green, 17 red; 13 blue, 5 red; 17 red",
"26: 1 blue, 3 green, 7 red; 9 red, 4 green, 1 blue; 1 red, 2 green, 1 blue; 11 red, 3 green; 10 red, 4 green, 2 blue; 6 red, 4 green",
"27: 4 blue, 6 red; 2 blue, 8 red, 1 green; 3 blue, 3 red; 2 red, 1 blue; 1 green, 3 blue, 6 red",
"28: 1 red, 7 blue, 7 green; 2 green, 1 red, 4 blue; 8 green, 2 red; 2 red, 7 blue, 5 green; 12 green, 5 blue, 2 red; 1 red, 1 green, 2 blue",
"29: 10 green, 3 red, 6 blue; 9 green, 6 blue, 4 red; 3 red, 2 blue, 17 green",
"30: 8 blue; 15 blue, 1 red; 10 green, 2 red, 13 blue",
"31: 10 green, 2 blue, 7 red; 2 green, 1 blue; 1 blue, 15 green, 2 red; 7 green, 2 blue; 3 blue, 6 green, 8 red; 6 red, 1 blue",
"32: 2 blue, 2 red, 11 green; 10 green, 2 red, 1 blue; 1 green, 2 blue; 2 red, 9 green, 2 blue; 2 blue, 1 green; 5 green, 1 blue, 2 red",
"33: 8 red, 6 blue; 2 green, 3 red, 2 blue; 1 green, 13 red, 18 blue",
"34: 7 blue, 5 green; 5 green, 8 blue; 13 blue, 15 red, 2 green",
"35: 1 blue, 2 green; 9 green; 4 red, 14 green; 1 red, 1 blue, 17 green",
"36: 2 red, 14 green, 4 blue; 13 green, 3 blue; 1 blue, 7 green, 2 red; 4 blue, 9 green; 1 green, 3 blue, 1 red; 2 red, 4 blue, 10 green",
"37: 2 blue, 7 green, 5 red; 5 green, 2 blue; 6 blue, 11 red",
"38: 6 green, 6 red; 9 red, 10 green; 2 blue, 8 green, 8 red",
"39: 10 red, 3 blue; 5 green, 3 red; 5 red, 7 green",
"40: 5 red, 14 green, 2 blue; 5 red, 7 blue, 12 green; 2 green, 4 red; 1 red, 16 green, 3 blue; 16 green, 4 red, 7 blue; 9 green, 2 red",
"41: 4 red, 3 green, 2 blue; 13 green, 6 blue; 2 red, 14 green, 1 blue; 7 blue, 2 red, 14 green",
"42: 4 red; 1 blue, 5 red; 1 green, 6 red; 1 red, 1 blue; 3 blue, 8 red",
"43: 7 blue, 16 red, 1 green; 2 red, 6 green, 1 blue; 5 green, 3 red; 5 green, 9 blue, 2 red; 3 red, 9 blue, 4 green; 7 red, 9 blue",
"44: 2 red, 2 green; 5 red, 1 blue, 8 green; 7 green, 3 blue, 5 red",
"45: 8 blue, 16 red; 8 blue; 4 blue, 1 green, 8 red",
"46: 11 green, 9 blue, 1 red; 8 green, 7 blue; 10 blue, 1 red, 1 green; 12 green, 10 blue",
"47: 3 green, 6 red, 1 blue; 2 blue, 2 green, 12 red; 3 red, 2 green, 1 blue",
"48: 3 red, 3 green, 3 blue; 3 red, 4 green, 2 blue; 2 green, 7 red, 1 blue; 2 red, 3 blue, 5 green",
"49: 5 red, 7 blue, 5 green; 10 red, 4 green, 7 blue; 9 red, 17 green; 6 green, 1 red, 2 blue; 7 green, 8 blue, 5 red",
"50: 2 red, 4 green, 16 blue; 4 blue, 3 red, 8 green; 4 blue, 2 red, 6 green",
"51: 16 green, 10 red, 14 blue; 8 red, 4 blue, 12 green; 14 green, 7 blue; 6 red, 20 green, 3 blue",
"52: 1 red, 1 blue, 1 green; 9 green, 9 red; 4 green, 13 red; 7 red, 11 green; 4 red, 1 blue; 8 green, 3 red, 1 blue",
"53: 4 green, 11 blue; 9 green, 2 red; 6 red, 18 green, 13 blue; 6 red, 2 blue, 14 green",
"54: 1 green, 1 red, 1 blue; 2 green, 4 blue; 4 blue, 5 green; 3 blue, 1 red, 10 green",
"55: 8 blue, 2 red, 3 green; 9 red, 11 blue; 1 green, 12 blue, 4 red; 3 green, 17 red; 3 red, 3 green, 15 blue; 7 blue, 7 red, 2 green",
"56: 3 blue, 13 green; 9 green, 2 blue; 1 red, 2 blue, 16 green",
"57: 6 blue, 4 red; 3 green, 6 red; 2 red, 3 blue, 3 green; 8 red, 5 blue",
"58: 4 red, 15 green, 5 blue; 1 red, 16 blue, 14 green; 2 green, 17 blue, 6 red; 20 blue, 3 red, 7 green; 17 green, 1 red, 12 blue",
"59: 3 blue, 14 red; 5 green, 10 red, 2 blue; 2 blue, 5 red, 6 green",
"60: 4 red, 1 blue, 1 green; 15 blue; 8 green, 14 blue, 4 red; 9 blue, 3 green, 4 red; 4 green, 2 red, 11 blue; 4 blue, 7 green",
"61: 5 green, 9 blue, 16 red; 4 blue, 12 green, 4 red; 17 red, 7 green, 5 blue; 19 blue, 12 red, 17 green; 8 green, 13 red",
"62: 13 green, 1 red, 7 blue; 9 blue, 1 red, 4 green; 14 green, 2 red, 2 blue; 3 green",
"63: 6 green; 7 red, 3 blue, 8 green; 5 blue, 1 green, 6 red; 6 green, 6 red, 2 blue; 8 green, 2 blue",
"64: 16 blue, 1 red, 2 green; 4 green, 1 blue, 6 red; 6 green, 2 blue, 2 red; 17 blue; 1 red; 13 blue, 6 green, 1 red",
"65: 8 red, 3 green, 7 blue; 6 blue, 8 red, 2 green; 2 blue, 3 green, 17 red",
"66: 2 blue, 3 green, 3 red; 3 red, 2 blue; 5 red, 4 green, 3 blue; 1 blue, 3 green; 2 red, 1 green, 1 blue; 2 blue, 4 green",
"67: 2 red, 3 blue, 15 green; 2 blue, 2 red, 17 green; 4 blue, 3 red, 2 green; 6 red; 3 red, 8 green",
"68: 7 red, 1 blue, 12 green; 17 red, 1 green; 10 red, 8 green; 16 red, 5 green, 2 blue; 4 red, 1 blue, 8 green; 8 green, 7 red, 2 blue",
"69: 17 green, 9 red, 2 blue; 1 blue, 14 green, 3 red; 9 red, 12 green, 2 blue; 11 green, 2 blue, 7 red",
"70: 1 green, 8 blue, 2 red; 2 red, 10 green, 1 blue; 1 red, 12 green, 6 blue; 9 green, 4 blue, 4 red; 2 red, 6 green; 3 red, 8 green, 6 blue",
"71: 1 red, 5 blue; 12 blue, 3 red; 3 red, 2 green, 4 blue; 5 blue, 3 green, 1 red",
"72: 11 red, 6 blue; 1 red, 1 blue, 1 green; 2 blue, 7 red; 18 blue, 3 red; 1 green, 1 blue, 12 red",
"73: 4 red, 2 blue, 1 green; 3 red; 5 red, 1 blue; 4 blue, 6 red",
"74: 2 red; 2 red, 5 green; 4 green, 1 red, 1 blue; 1 blue, 5 green, 5 red; 7 red, 1 blue, 3 green; 8 red, 1 blue, 6 green",
"75: 13 blue, 2 red, 2 green; 2 red, 9 blue; 2 red, 9 blue, 5 green",
"76: 2 red, 3 green, 18 blue; 2 red, 11 green, 5 blue; 6 green, 8 blue, 2 red; 4 blue; 7 green, 14 blue",
"77: 5 blue, 8 red, 1 green; 2 blue, 5 green, 12 red; 3 red, 4 blue",
"78: 1 blue, 2 green, 16 red; 2 red, 3 green; 1 red, 4 green, 2 blue; 11 red; 2 green, 12 red, 2 blue; 11 red, 5 green, 3 blue",
"79: 10 green, 3 blue, 2 red; 8 red, 3 blue, 8 green; 5 green, 3 red, 11 blue; 9 green, 16 blue",
"80: 1 red, 4 blue; 6 green, 1 red; 6 green, 3 blue, 1 red; 6 green, 2 red; 7 green, 1 blue; 2 red, 2 blue, 2 green",
"81: 10 blue, 4 red, 4 green; 5 green, 1 red, 7 blue; 11 blue, 8 green, 2 red; 8 green, 2 red",
"82: 12 green, 1 red, 3 blue; 6 red, 1 blue; 16 green, 3 red, 4 blue; 8 blue; 7 blue, 7 green, 2 red; 4 red, 19 green",
"83: 4 red, 4 blue, 3 green; 8 blue, 4 green, 6 red; 6 green, 7 blue, 6 red; 11 red, 6 green, 7 blue",
"84: 11 red, 2 green, 2 blue; 20 green, 2 blue, 13 red; 15 red, 6 green, 3 blue; 17 green, 7 red",
"85: 3 blue, 5 green, 2 red; 12 green, 2 blue, 1 red; 7 blue, 6 green, 5 red; 11 red, 2 blue, 17 green; 11 blue, 11 red, 17 green; 18 green, 9 red, 13 blue",
"86: 1 blue, 14 red; 4 green, 1 blue, 3 red; 2 green, 1 blue, 13 red; 1 green, 1 blue, 10 red",
"87: 2 red, 5 green, 4 blue; 3 blue, 9 red, 6 green; 7 blue, 9 red, 11 green; 10 green, 11 red, 9 blue; 7 green, 12 red, 4 blue; 5 blue, 1 red, 7 green",
"88: 11 red, 1 green; 9 blue, 4 green, 7 red; 10 red, 4 green, 1 blue; 4 green, 1 red, 1 blue; 10 blue, 1 red, 3 green; 2 green, 12 blue, 11 red",
"89: 3 green, 3 blue; 1 red, 7 green, 9 blue; 8 red, 11 blue, 11 green; 2 green, 6 blue, 5 red; 5 blue, 9 green",
"90: 3 blue, 10 red, 2 green; 2 blue; 8 red",
"91: 2 red, 10 green, 2 blue; 9 blue; 8 green, 5 red, 10 blue; 7 green, 6 blue, 5 red; 1 green, 6 red, 12 blue; 1 red, 4 green, 3 blue",
"92: 12 blue, 5 red, 2 green; 4 blue, 1 red, 3 green; 6 red, 6 blue; 1 blue, 8 red, 6 green; 6 blue, 3 red, 2 green; 7 green, 4 red, 1 blue",
"93: 3 blue; 8 blue; 3 blue, 2 red; 2 red, 1 green",
"94: 5 red, 7 blue, 6 green; 15 red, 7 blue, 4 green; 6 blue, 1 red, 2 green; 7 green, 4 blue, 17 red; 12 red, 5 green, 1 blue",
"95: 7 blue, 11 red, 9 green; 10 red, 6 blue, 7 green; 6 blue, 6 red, 7 green",
"96: 2 red, 1 green, 3 blue; 3 blue, 1 green; 1 green, 1 blue; 1 red, 1 blue; 1 green, 1 red, 4 blue",
"97: 6 red, 1 blue, 7 green; 2 blue, 5 red, 7 green; 8 red, 3 blue, 6 green; 6 green, 1 red, 3 blue; 5 red, 2 blue, 14 green; 3 green, 6 red, 6 blue",
"98: 9 red, 14 blue; 19 red, 4 blue; 11 red, 17 blue; 14 blue, 1 green, 18 red",
"99: 1 green, 1 red, 12 blue; 2 green, 4 red, 14 blue; 4 blue, 6 red; 10 red, 2 green, 1 blue",
"100: 5 red, 9 green, 2 blue; 9 blue, 6 green, 1 red; 8 blue, 7 green, 3 red"
]

json_result = convert_to_json(data)
print(json_result)

