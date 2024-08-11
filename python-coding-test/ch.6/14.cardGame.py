# 1점: 잭, 1장 이상, 다음 1장 중 잭 퀸 킹 에이스 X
# 2점: 퀸, 2장 이상, 다음 2장 중 잭 퀸 킹 에이스 X
# 3점: 킹, 3장 이상, 다음 3장 중 잭 퀸 킹 에이스 X
# 4점: 에이스, 4장 이상, 다음 4장 중 잭 퀸 킹 에이스 X

NUM_CARDS = 52

deck = []
aScore = 0
bScore = 0
player = 'A'

# 다음 카드 중 잭, 퀸, 킹, 에이스가 없음을 보장하는 함수
def no_high(lst): 
  if 'jack' in lst:
    return False
  if 'queen' in lst:
    return False
  if 'king' in lst:
    return False
  if 'ace' in lst:
    return False
  return True

for i in range(NUM_CARDS):
  deck.append(input())

for i in range(NUM_CARDS):
  card = deck[i]
  points = 0
  remaining = NUM_CARDS - i - 1
  if card == 'jack' and remaining >= 1 and no_high(deck[i+1:i+2]):
    points = 1
  elif card == 'queen' and remaining >= 2 and no_high(deck[i+1:i+3]):
    points = 2
  elif card == 'king' and remaining >= 3 and no_high(deck[i+1:i+4]):
    points = 3
  elif card == 'ace' and remaining >= 4 and no_high(deck[i+1:i+5]):
    points = 4

  if points > 0:
    print(f'Player {player} scores {points} point(s).')
  
  if player == 'A':
    aScore = aScore + points
    player = 'B' # 다음 플레이어 차례로 넘기기
  else:
    bScore = bScore + points
    player = 'A'

print(f'Player A: {aScore} point(s).')
print(f'Player B: {bScore} point(s).')