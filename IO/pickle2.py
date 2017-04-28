import pickle
with open('dump.txt', 'rb') as f:
    d = pickle.load(f)
    print(d)