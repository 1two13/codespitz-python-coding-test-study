# 상자 수
# k 피규어 수 / 피규어들 높이
# 피규어 높이가 왼쪽에서 오른쪽으로 증가 or 동일한 높이 => return 'YES'

n = int(input())

def read_boxes(n): 
  boxes = []
  for i in range(n):
    box = input().split()
    box.pop(0) # 피규어 개수 제거
    for i in range(len(box)):
      box[i] = int(box[i])
    boxes.append(box)
  return boxes

boxes = read_boxes(n)

def box_ok(box):
  for i in range(len(boxes) - 1):
    if box[i] > box[i + 1]:
      return False
    return True

def all_boxes_ok(boxes):
  for box in boxes:
    if not box_ok(box):
      return False
    return True

def boxes_endpoints(boxes):
  endpoints = []
  for box in boxes:
    endpoints.append(box[0], box[-1])
  return endpoints

def all_endpoints_ok(endpoints):
  maximum = endpoints[0][1]
  for i in range(1, len(endpoints)):
    if endpoints[i][0] < maximum:
      return False
    maximum = endpoints[i][1]
  return True

if not all_boxes_ok(boxes):
  print('NO')
else:
  endpoints = boxes_endpoints(boxes)
  endpoints.sort()
  if all_endpoints_ok(endpoints):
    print('YES')
  else:
    print('NO')