number = int
def convert(number):
  divided_by_2 = number % 2 == 0
    divided_by_3 = number % 3 == 0
            divided_by_5 = number % 5 == 0
            divided_by_7 = number% 7 == 0
            
        # Making conditional statement for 3, 5, 7 
        # Cuz we have 3 numbers,so we have 3! ways for if statement which will be 3! = 3*2*1 ways(regardless Else)

            
            if divided_by_3 and divided_by_5 and divided_by_7:
                return("PlingPlangPlong")
            
            elif divided_by_3 and divided_by_5:
                return("PlingPlang")
                
            elif divided_by_3 and divided_by_7:
                return("PlingPlong")
            
            elif divided_by_2:
                return(f"{given_number}")
            
            elif divided_by_3:
                return("Pling")
                
            elif divided_by_5:
                return("Plang")
                
            elif divided_by_7:
                return("Plong")
            
            else:
                return given_number
    except ValueError:
        return "You have to enter a number! "
        
    
    