entero =[100,90,50,40,10,9,5,4,1]
romano=["C","XC","L","XL","X","IX","V","IV","I"]

while ( True ):
    x = int(input("\nINGRESE UN NUMERO "))
    
    if(x==0):
       break
        
    print str(x)+":"
     
    i =0
    while( x>0 ):    
	if( x >= entero[i]):
            print str(romano[i]),
            x = x - entero[i]
        else:
            i=i+1