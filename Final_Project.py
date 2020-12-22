'''
Joseph Williams
Final Project 
This project is user interaction project that reads data from an online data source and displays the data to the user in data frames.
'''

# pandas is a python module that is used in data science project
import pandas as pd

# An input created to take the user input 
# the user will be prompted to input a particular country from several selections and the the population of the
# country will be displayed alongside the full table of countries.

#Ask for input from the user
def ask_for_input():
    '''
    This is a fuction for prompting user input with options and verifying if the input is in the right format.
    If the format is wrong the user is promted to enter the input again 
    The user can also quit.
    '''
    loop =True
    while loop == True:
        print("choose option\n 1:Filter data\n 2:Quit\n")
        try:
            option = int(input())
            if option == 1:
                life_expentancy = int(input("\ninput a minimum life expectancy value of your choice:\t"))
                loop =False
                return life_expentancy
            elif option ==2:
                loop = False
            else:
                print("invalid option\n please try again") 
                loop = True
            
        except:
            print("your choice must be an integer\n please try again")
            loop =True

#Check if user wants to re-process data
def repeat_process():
    '''
    This is a fuction for prompting user input to check if they are satisfied with previous analysis 
    verifying if the option selected is in the right format.
    If the format is wrong the user is promted to enter the input again 
    The user can also quit.
    '''
    loop = True
    while loop ==True:
        print("\n\n*****************************************************************\nDo you want to process data again? \n 1:Yes\n 2:No\n ")
        try:
            option = int(input())
            if option ==1:
                loop = False
                return True
            if option ==2:
                loop = False
                return False
            else:
                print("invalid option\n Try again\n ")
                
        except:
            print("Please choose an integer\n ")

#intializing a list to store the filtered life expectancy value 
processed_life_list = []
#while loop to repeat the data analysis process
loop = True
while loop == True:
    processed_life_list = []
    #created a variable to store the data set 
    data_store = 'http://bit.ly/2cLzoxH'

    #this is another variable that denotes the read_csv methos from the pandas module
    #it takes one parameter which is the data that will be read
    pandas_dataframe = pd.read_csv(data_store)

    # the below print statements forst one prints the string and the second prints the filtered data in a dataframe
    print("\nThe full list of the countries is printed below:\n")
    print(pandas_dataframe)

    #request for input
    life_expentancy = ask_for_input()

    #this variable will filters all the rows with a life expectancy higher than the input 
    more_life_expectancy = pandas_dataframe[pandas_dataframe['lifeExp']
                                            > life_expentancy]
    #for loop to loop through the records and the filtered more life expectancy
    for life_exp in more_life_expectancy['lifeExp']:
        #the results are appended to the list
        processed_life_list.append(life_exp)
    # the below print statements will output the data frames after condition is satisfied
    print("\n\n*****************************************************************\nfull list of countries with a life expextancy greater than " +
        str(life_expentancy) + "\n")
    print(more_life_expectancy)
    #print(processed_life_list)
    print('---------- Processing done successifully---------- \n',len(processed_life_list), ' processed records')
    
    #check for repeat request
    check_repeat = repeat_process()
    if check_repeat == False:
        loop = False


