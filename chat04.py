# 練習字串分割 (分割法如同清單)

with open('3.txt', 'r', encoding='utf-8') as f:
	lines =[]
	for line in f:
		lines.append(line.strip())

	for line in lines:
		s = line.split(' ')	
		time = s[0][:5]
		name = s[0][5:]
		print('時間', time, '名字', name, '說', s[1:])	