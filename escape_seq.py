#    #==================+=================================================================#
#    |	Escape		|	Whatit does						  |
#    #==================+=================================================================#
#    |	\\    		|	backslash						  |
#    |	\'    		|	single-quote						  |
#    |	\"    		|	double-quote						  |
#    |	\a    		|	ASCIi bell (BEL)					  |
#    |	\b    		|	ASCII backspace						  |
#    |	\f    		|	ASCII formfeed(FF)					  |
#    |	\n    		|	ASCII linefeed(LF)					  |
#    |	\N{name}	|       character named name in the unicode database(Unicode only)|
#    |	\r    		|	ASCII carriage return(CR)				  |
#    |	\t    		|	ASCII horizontal tab		  			  |
#    |	\uxxx		|	character with 16-bit hex value xxxx (Unicode only)	  |
#    |	\Uxxxxxxxx	|	Character with 32-bit hex value xxxxxxxx (Unicode only)	  |
#    |	\v		|	ASCII vertical tab (VT)					  |
#    ######################################################################################


tabby = "\tI'm tabbed in. "
new_line = "hello \n world"
backslash = "this is \\ a \\ cat"

unorder_list = """
unorder list :
\t* Apple
\t* Mango
\t* Banana \n \t* etc..
"""
print(tabby)
print(new_line)
print(backslash)
print(unorder_list)
