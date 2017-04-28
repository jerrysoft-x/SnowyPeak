from io import StringIO
f = StringIO('Hello!\nHi!\nGoodbye!')
# while True:
#     s = f.readline()
#     if s == '':
#         break
#     print(s.strip())
for s in f.readlines():
    print(s.strip())
