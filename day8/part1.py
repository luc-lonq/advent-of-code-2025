from math import sqrt


networks = []

boxes = []

with open("input.txt", "r") as f:
  for l in f:
    if l == "\n":
      continue
    b = l.split(',')
    boxes.append({"x": int(b[0]), "y": int(b[1]), "z": int(b[2])})

threshold = 0
for i in range(1000): # test input => 10
  minimum_length = None
  box1 = None
  box2 = None
  print(f"--- Iteration {i} ---")
  print(f"threshold: {threshold}")
  for b1 in boxes:
    for b2 in boxes:
      d = sqrt((b2['x'] - b1['x'])**2 + (b2['y'] - b1['y'])**2 + (b2['z'] - b1['z'])**2)
      #print(f"Distance between box {b1} and box {b2}: {d}")
      if d > threshold and (minimum_length is None or d < minimum_length):
        minimum_length = d
        box1 = b1
        box2 = b2

  print(f"minimum_length: {minimum_length}")
  threshold = minimum_length


  print(f"Connecting box {box1} with box {box2} at distance {minimum_length}")
  box1_network = None
  box2_network = None
  for network in networks:
    if box1 in network:
      box1_network = network
    if box2 in network:
      box2_network = network
  if box1_network is None and box2_network is None:
    networks.append([box1, box2])
  elif box1_network is not None and box2_network is None:
    box1_network.append(box2)
  elif box1_network is None and box2_network is not None:
    box2_network.append(box1)
  elif box1_network != box2_network:
    box1_network.extend(box2_network)
    networks.remove(box2_network)

print(networks)

top_three_networks = sorted(networks, key=lambda n: len(n), reverse=True)[:3]
n = 1
for tn in top_three_networks:
  n *= len(tn)
  print(f"Top network size: {len(tn)}")

print(n)