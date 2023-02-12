color = {'colors':'red', 'visible':'Light'}
print(color['visible'])
print(color['colors'])

#Accessing values in Dictionaries
alien = {'color': 'green', 'point': '5'}
new_point= alien['point']
print(' You just earned '+ str(new_point)+ ' points ')

alien = {'color': 'green', 'points': '5'}
print(alien)
alien['x_position'] = 0
alien['y_position'] = 25
print(alien) 

alien = {}
alien['color'] = 'green'
alien['points'] = '5'
print(alien)

alien = {'color': 'green'}
print("The alien color is now "+ alien['color']+ ".")
alien = {'color': ' yellow '}
print("Now alien is " + alien['color'] + 'color.')

alien =  {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position:" + str(alien['x_position']))

if alien['speed'] == 'slow':
    x_increment = 1
elif alien['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
alien['x_position'] = alien['x_position'] + x_increment
print("new x-position:" + str(alien['x_position']))   

favorite_language = {
    'jen' : 'python',
    'sara' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}
print("Sara's favourite language is "+ favorite_language['sara'].title()+'.')
print("jen's favourite langauge is " + favorite_language['jen'].title()+'.')

user_0 = {
    'username': 'efermi',
    'first_name': 'enrico',
    'last': 'fermi',
    }
for key, value in user_0.items():
    print("\nkey: " + key)
    print("value: " + value)


favorite_language = {
    'jen' : 'python',
    'sara' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}
for name,language in favorite_language.items():
    print(name.title() + "'s favorite language is " + language.title()+".")


favorite_language = {
    'jen' : 'python',
    'sara' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}
for name in favorite_language.keys():
    print(name.title())    


favorite_language = {
    'jen' : 'python',
    'sara' : 'c',
    'edward' : 'ruby',
    'phil' : 'python'
}
friends = ['phil', 'sara']
for name in favorite_language.keys():
    print(name.title)

    if name in friends:
        print(" Hi " + name.title() +", I see your favourite language is "+ favorite_language[name].title() + "!")


#Nesting
for aliens_number in range(30):
    new_aliens = {'color': 'green', 'points': 5, 'speed': 'slow'}
    alien.append(new_aliens)

for aliens in alien[:5]:
    print(alien)
print(".....")

print("Total number of alien: " + str(len(alien)))


