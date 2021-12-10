import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_list = ['chicago', 'new york city', 'washington']
    input_city = str(input("Choose a city (Chicago, New York City, Washington): "))
    while input_city.lower() not in city_list: #check if the selected city is an option
        print("Please choose a city from the available options!")
        input_city = str(input("Choose a city (Chicago, New York City, Washington): "))
    print("You chose " + input_city.title() +".")
    
    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ['all','january', 'february', 'march', 'april', 'may', 'june']
    input_month_selection = str(input("Do you want to see any particular month data from January - June? (Y/N)")) #check if user want to check all months
    while input_month_selection.lower() != "n" and input_month_selection.lower() !="y": #get the correct yes/no from user
        print("Please type Y for yes and N for no.")
        input_month_selection = str(input("Do you want to see any particular month data from January - June? (Y/N)"))
        
    #get user month selection
    if input_month_selection.lower() == "n":
        input_month = 'all'
    elif input_month_selection.lower() == "y":
        input_month = str(input("Your selected month name: "))
        while input_month.lower() not in month_list:
            print("Please choose a month from January to June and type in the full name.")
            input_month = str(input("Your selected month name: "))        
        
    if input_month.lower() == 'all':
        print("You chose to see data for all months.")
    else:
        print("You chose to see data for " + input_month.title() + ".")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    input_day_selection = get_input_day()
        
    #get user month selection
    if input_day_selection.lower() == "n":
        input_day = 'all'
    elif input_day_selection.lower() == "y":
        input_day = str(input("Your selected day: "))
        while input_day.lower() not in day_list:
            print("Please type your day.")
            input_day = str(input("Your selected day: "))        
        
    if input_day.lower() == 'All':
        print("You chose to see data for all days.")
    else:
        print("You chose to see data for " + input_day.title() + "s.")

    print('-'*40)
    return input_city.lower(), input_month.title(), input_day.title()

def get_input_day():
    input_day_selection = str(input("Do you want to see any particular day? (Y/N)")) #check if user want to check any chosen day
    while input_day_selection.lower() != "n" and input_day_selection.lower() !="y": #get the correct yes/no from user
        print("Please type Y for yes and N for no.")
        input_day_selection = str(input("Do you want to see any particular day? (Y/N)"))
    return input_day_selection

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    filename = CITY_DATA[city]
    filedata = pd.read_csv(filename)
    get_time_details(filedata)
    if month != 'All':
        filtered_month = filedata.loc[filedata['Month']==month]
    else: filtered_month = filedata
    if day != 'All':
        filtered_table = filtered_month.loc[filtered_month['Day']==day]
    else: filtered_table = filtered_month
    
    return filtered_table

def get_time_details(filedata):
    filedata['Start Time'] = pd.to_datetime(filedata['Start Time'])
    filedata['Month'] = filedata['Start Time'].dt.month_name()
    filedata['Day'] = filedata['Start Time'].dt.day_name()
    filedata['Hour'] = filedata['Start Time'].dt.hour
    filedata['Trip details'] = filedata['Start Station'] + '-' + filedata['End Station']

# def popular_time(df):

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    if df['Month'].nunique() == 1 and df['Day'].nunique() == 1:
        print("Most popular time on " + df['Day'].values[0]+ "s in " + df['Month'].values[0] + " is: ")
    if df['Month'].nunique() == 1 and df['Day'].nunique() > 1:
        print("The most frequent travel times in " +df['Month'].values[0] + " is:")
        popular_day = df['Day'].mode()[0]
        print("Most popular day: " + popular_day)
    if df['Month'].nunique() > 1 and df['Day'].nunique() == 1:
        print(df[['Day']].values[0][0] + ' is most popular in the following month and hour:')
        popular_month = df['Month'].mode()[0]
        print("Most popular month: " + popular_month)
    if df['Month'].nunique() > 1 and df['Day'].nunique() > 1:
        popular_month = df['Month'].mode()[0]
        print("Most popular month: " + popular_month)
        popular_day = df['Day'].mode()[0]
        print("Most popular day: " + popular_day)
        

    # TO DO: display the most common start hour
    popular_hour = df['Hour'].mode()[0]
    print("Most popular hour: " + str(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_origin = df['Start Station'].mode()[0]
    print("Most popular origin: " + popular_origin +'.')

    # TO DO: display most commonly used end station
    popular_destination = df['End Station'].mode()[0]
    print("Most popular destination: " + popular_destination +'.')

    # TO DO: display most frequent combination of start station and end station trip
    popular_trip = df['Trip details'].mode()[0]
    print("Most popular trip: " + popular_trip+'.')

    print("\nThis took %s seconds." % (time.time() - start_time)) 
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_duration = df['Trip Duration'].sum()
    total_duration_hours = int(total_duration//3600)
    total_duration_minutes = int((total_duration%3600)//60)
    total_duration_seconds = int((total_duration%3600)%60)
    
    print('Total travel time is ' + str(total_duration_hours) + ' hours, ' + str(total_duration_minutes) + ' minutes, and ' + str(total_duration_seconds) + ' seconds.')
                         
    # TO DO: display mean travel time
    average_duration = df['Trip Duration'].mean()
    ave_duration_hours = int(average_duration//3600)
    ave_duration_minutes = int((average_duration%3600)//60)
    ave_duration_seconds = int((average_duration%3600)%60)
    print('Average travel time is ' + str(ave_duration_hours) + ' hours, ' + str(ave_duration_minutes) + ' minutes, and ' + str(ave_duration_seconds) + ' seconds.')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    
    # TO DO: Display counts of user types
    if 'User Type' in df.columns:
        print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print("Earlist birth year: " + str(int(df['Birth Year'].min())))
        print("Latest birth year: " + str(int(df['Birth Year'].max())))
        print("Most common birth year: " + str(int(df['Birth Year'].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        
        time_stats(df)
        input("Enter to continue.")
        station_stats(df)
        input("Enter to continue.")
        trip_duration_stats(df)
        input("Enter to continue.")
        user_stats(df)
        input("Enter to continue.")
        
        display_data = input('Do you want to see the raw data? (Y/N)')
        while display_data.lower() != 'y' and display_data.lower() != 'n':
            print("Please choose Y for yes and N for no.")
            display_data = input('Do you want to see the raw data? (Y/N)')
        
        start = 0
        while display_data.lower() == 'y':
            print(df.iloc[start:start+5,:])
            display_data = input('Do you want to see more raw data? (Y/N)')             
            start +=5
                          
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
