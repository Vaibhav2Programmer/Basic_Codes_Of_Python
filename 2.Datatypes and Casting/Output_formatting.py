# Sometimes formatting is done to make output attractive
# we use str.format() method/function. This method/function is visible to any string object.

x=5;y=10
print('The value of x is {} and y is {}'.format(x,y))
print('The value of x is {} and y is {}'.format(y,x))  # Order of x and y is changed

print('Hello {name},{greeting}'.format(greeting='Good Night',name='Vaibhav'))

print('I Love {1} which is a {0}'.format('sport','cricket')) # Here at 0 index we have sport and at 1 we have cricket

input = 'a'
print("First Input is {input}")