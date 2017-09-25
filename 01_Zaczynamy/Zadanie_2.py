'''Napisz program, który obliczy pole trójkąta, pod warunkiem że użytkownik poda wysokość i długość podstawy tego trójkąta.
Uwzględnij, że wysokość i długość podstawy mogą być liczbami niecałkowitymi. '''


height = float(input("Enter the height of the triangle:  ").strip())
base = float(input("Enter the base of the triangle:  ").strip())

triangle_area = 0.5 * height * base

print("The area of the triangle is {}".format(triangle_area))



