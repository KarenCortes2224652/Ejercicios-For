m9 = 0
m7 = 0
for i in range(1000,5000):
    if i % 7 == 0:
        m7 = m7 + 1
    if i % 9 == 0:
        m9 = m9 + 1
print(m7)
print(m9)