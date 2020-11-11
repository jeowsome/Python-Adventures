# create the planets.txt
file_name = open('planets.txt', 'w', encoding='utf-8')
planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter',
           'Saturn', 'Uranus', 'Neptune']

for planet in planets:
    file_name.write(planet + '\n')

file_name.close()
