def not_empty(s):
    return s and s.strip()

print(' hello   '.strip())
print(''.__eq__(''.strip()))
print('A' and 'A'.strip())
print('' and ''.strip())
print('A' and 'B')

print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' '])))

