Hanna=input('Jön Hanna ma kosarazni(igen/nem)? ' )
Henrik=input('Jön Henrik ma kosarazni(igen/nem)? ' )

if Hanna == 'igen' and Henrik == 'igen':
    print('Mind a ketten jönnek kosarazni.')
    
elif Hanna == 'igen' and Henrik == 'nem':
    print('Csak az egyikük jön kosarazni.')
    
elif Hanna == 'nem' and Henrik == 'igen':
    print('Csak az egyikük jön kosarazni.')
    
else:
    print('Egyikük sem jön kosarazni.')