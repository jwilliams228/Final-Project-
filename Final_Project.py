'''
Joseph Williams
Final Project 
This project is user interaction project that reads data from an online data source and displays the data to the user in data frames.
'''

# pandas is a python module that is used in data science project
import pandas as pd

#created a variable to store the data set 
data_store = 'http://bit.ly/2cLzoxH'

#this is another variable that denotes the read_csv methos from the pandas module
#it takes one parameter which is the data that will be read
pandas_dataframe = pd.read_csv(data_store)

# the below print statements forst one prints the string and the second prints the filtered data in a dataframe
print("\nThe full list of the countries is printed below:\n")
print(pandas_dataframe)


# An input created to take the user input 
# the user will be prompted to input a particular country from several selections and the the population of the
# country will be displayed alongside the full table of countries.
life_expentancy = int(input(
    "\ninput a minimum life expectancy value of your choice:\t"))

#this variable will filters all the rows with a life expectancy higher than the input 
more_life_expectancy = pandas_dataframe[pandas_dataframe['lifeExp']
                                        > life_expentancy]

# the below print statements will output the data frames after condition is satisfied
print("\n\nfull list of countries with a life expextancy greater than " +
      str(life_expentancy) + "\n")
print(more_life_expectancy)

######to be continue
