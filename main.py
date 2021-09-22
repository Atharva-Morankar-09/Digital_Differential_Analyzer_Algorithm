
# Digital Differential Analyzer (DDA) Line Drawing Algorithm

import matplotlib.pyplot as plt
print("ENTER STARTING CO-ORDINATES")
x1, y1 = map(int, input().split())
print("ENTER ENDING CO-ORDINATES")
x2, y2 = map(int, input().split())

dx = x2 - x1
dy = y2 - y1

X_coordinates = [x1]
Y_coordinates = [y1]

# Set the higher difference as length
if dx >= dy:
    Length = dx
else:
    Length = dy

delta_x = dx/Length
delta_y = dy/Length


x = x1 + (0.5 * delta_x)
y = y1 + (0.5 * delta_y)

print(" i     |   Setpixel(x,y)   |     X      |     Y      | ")
print("       |    (%d,%d)        |     %.2f     |    %.2f      |" % (x1, y1, x, y))

for i in range(1, Length+1):
    x = x + delta_x
    y = y + delta_y
    print("  %d    |    (%d,%d)        |     %.2f     |    %.2f     |" % (i, x, y, x, y))
    i += 1
    X_coordinates.append(x)
    Y_coordinates.append(y)
    X = (X_coordinates[0], X_coordinates[-1])
    Y = (Y_coordinates[0], Y_coordinates[-1])

# Graphical Representation of the line
plt.title("Digital Differential Analyzer")
plt.ylabel("Y-AXIS")
plt.xlabel("X-AXIS")
plt.plot(X, Y, 'red', linewidth="1")
plt.scatter(X_coordinates, Y_coordinates, color='BLACK', s=25)
plt.show()