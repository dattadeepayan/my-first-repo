mon = 12
day = 31
week =  1
year =  1899
year_counter = 3

while ( 1 ):
        if  mon in [ 1 , 3 , 5 , 7 ,8 , 10 , 12 ]:
                day = ( day + 28 )  - 31
                if day > 0:
                        mon+=1
                        if ( mon > 12):
                                mon = 1
                                year+=1
                                year_counter+=1
                                if year_counter > 4:
                                		year_counter = 1
                                if year > 2000:
                                		break

                        if ( day % 7 == 1 ):
                        		print ( str (year ) + "." + str( mon ) + "." + str("1") )
                else:
                        day = ( 31 - abs (day ) ) +  28 -  31
                        mon+=1
                        if ( mon > 12 ) :
                                mon = 1
                                year+=1
                                if year_counter > 4:
                                		year_counter = 1
                                if year > 2000:
                                		break
                        
                        if (day % 7 == 1 ):
                        		print ( str (year ) + "." + str( mon ) + "." + str("1") )




        if mon in [ 4, 6 , 9 , 11 ]:
        		day = day + 28 - 30
        		if day > 0:
        				mon+=1
        				if ( day % 7 == 1):
        						print ( str (year ) + "." + str( mon ) + "." + str("1") )
        		else:
        				day = ( 30 - abs (day) ) + 28 - 30
        				mon+=1
        				if( day %7 == 1):
        						print ( str (year ) + "." + str( mon ) + "." + str("1") )

       	if ( mon == 2):
       			if (year_counter != 4 ):
       					day = day + 28 - 28
       					if day > 0:
        						mon+=1
        						if ( day %7== 1):
        								print ( str (year ) + "." + str( mon ) + "." + str("1") )
        				else:
        						day = ( 28 - abs (day) ) + 28 - 28
        						mon+=1
        						if( day % 7 == 1):
        								print ( str (year ) + "." + str( mon ) + "." + str("1") )
       			else:
       					day = day + 28 - 29
       					if day > 0:
        						mon+=1
        						if ( day % 7 == 1):
        								print ( str (year ) + "." + str( mon ) + "." + str("1") )
        				else:
        						day = ( 29 - abs (day) ) + 28 - 29
        						mon+=1
        						if( day %7 == 1):
        								print ( str (year ) + "." + str( mon ) + "." + str("1") )
