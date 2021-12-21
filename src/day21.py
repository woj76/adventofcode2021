#!/snap/bin/pypy3

player1_init = 1
player2_init = 5

dice_position = 0

turn = 0
dice_rolls = 0

scores = [0, 0]

players = [player1_init - 1, player2_init - 1]

while True:
	dice = 0
	for _ in range(3):
		dice += dice_position + 1
		dice_position = (dice_position + 1) % 100
		dice_rolls += 1
	players[turn] = (players[turn] + dice) % 10
	scores[turn] += players[turn] + 1
	if scores[turn] >= 1000:
		break
	turn = (turn + 1) % 2

print(f"Part 1: {scores[(turn + 1) % 2]*dice_rolls}")

# 3 rolls_can give the possible outcomes of:
# 3: 1+1+1
# 4: 1+1+2, 1+2+1, 2+1+1
# 5: 1+2+2, 2+1+2, 2+2+1, 1+1+3, 1+3+1, 3+1+1
# 6: 1+2+3, 3+2+1, 1+3+2, 3+1+2, 2+1+3, 2+3+1, 2+2+2
# 7: 1+3+3, 3+1+3, 3+3+1, 2+2+3, 2+3+2, 3+2+2
# 8: 3+3+2, 3+2+3, 2+3+3
# 9: 3+3+3

cnts = { 3: 1, 4: 3, 5: 6, 6:7, 7:6, 8:3, 9:1}

wins1 = wins2 = 0

def check_win(player1, player2, score1, score2, paths, turn):
	global wins1
	global wins2
	for dice in cnts.keys():
		new_player1 = player1
		new_player2 = player2
		new_score1 = score1
		new_score2 = score2
		if turn == 0:
			new_player1 = (new_player1 + dice) % 10
			new_score1 += (new_player1 + 1)
			if new_score1 >= 21:
				wins1 += paths*cnts[dice]
				continue
		else:
			new_player2 = (new_player2 + dice) % 10
			new_score2 += (new_player2 + 1)
			if new_score2 >= 21:
				wins2 += paths*cnts[dice]
				continue
		check_win(new_player1, new_player2, new_score1, new_score2, cnts[dice]*paths, 1 if turn == 0 else 0)

check_win(player1_init-1, player2_init-1, 0, 0, 1, 0)

print(f"Part 2: {max(wins1, wins2)}")
