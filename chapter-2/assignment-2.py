#1.Simple Message
message='Hello'
print(message)
#2.Simple Message
#2.1
message2='Good, morning'
print(message2)
#2.2
message2='It is a beautiful day'
print(message2)
#3.Personal Message
#3.1
person_name='Rehma'
#3.2
print(f'Hello {person_name}, would you like to learn something today?')
#4.Name Cases
#4.1
person_name2='rehma khan'
#4.2
print(person_name2.lower())
print(person_name2.upper())
print(person_name2.title())
#5.Famous Quote
#5.1
famous_person='Min Yoongi'
quote='You were born to be real, not yo be perfect'
#5.2
print(f'{famous_person} once said: {quote}')
#6.Famous Quote 2
#6.1
famous_person2='Jeon Jungkook'
#6.2
message3='Living without a passion, is like being dead'
#6.3
print(f'{famous_person2} said: {message3}')
#7.Stripping Names
#7.1
name='       Hello,Rehma      '
#7.2
name2='  Hello,\n\tFatima'
#7.3
print(name)
print(name2)
#7.4
print(name.rstrip())
print(name.lstrip())
print(name.strip())
#8.Variable Sum
x,y,z=5,10,15
sum=x+y+z
print(f'sum={sum}')
#9.Variable Swap
a,b=4,7
print(f'before swap:a={a},b={b}')
a,b=b,a
print(f'after swap:a={a},b={b}')
#10.Favorite Color
color='Purple'
print(f'My favorite color is {color}')
fav_color=color
print(f"My favorite color is {fav_color}")
#11.Changing Pet Name
pet_name='Cupcake'
pet_name='Hope'
print(pet_name)
#12.Observing Name Error
sunrise='Sunshine'
print(sunrise)
#13.Reassigning Score
score:int=100
print(f'The score is {score}')
score=200
print(f'The new score is {score}')
#14.City Name
city:str='Lahore'
print(f'I like {city}')
#15.Title Case Text
text='python programming'
print(text.title())
#16.Lowercase Conversion
text2:str='pytHON proGrAMMing'
print(text2.lower())
#17.Uppercase Conversion
text3:str='pytHON proGrAMMing'
print(text3.upper())
#18.Current Temperature
temp=25
print(f'The current temperature is {temp} degrees.')
#19.Printing a Poem
poem='''Hold fast to dreams
For if dreams die,
Life is a broken-winged bird
That cannot fly.
Hold fast to dreams
For when dreams go,
Life is a barren field
Frozen with snow.'''
print(poem)