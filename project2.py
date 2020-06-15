import time
import pandas as pd
import numpy as np
# Change 1
# Change 2
# Change 3

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
    cities = ['chicago', 'new york city', 'washington']
    city = input("Enter city to be explored (chicago, new york city or washington):").lower()
    while city not in cities:
        try:  
            print ("Invalid input, not in range. Try again.")
            city = input("Enter city to be explored (chicago, new york city or washington):").lower()
        except:
            print ("Invalid input, not in range. Try again.")

    # TO DO: get user input for month (all, january, february, ... , june)
    months = ['all','january', 'february', 'march', 'april', 'may', 'june']
    month = input("Enter month to be explored (Jan-Jun) or all for no filter:").lower()
    while month not in months:
        try:  
            print ("Invalid input, not in range. Try again.")
            month = input("Enter month to be explored (Jan-Jun) or all for no filter:").lower()
        except:
            print ("Invalid input, not in range. Try again.")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter weekday to be explored or all for no filter:").lower()
    days = ['all','monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while day not in days:
        try:   
            print ("Invalid input, not in range. Try again.")
            days = input("Enter weekday to be explored or all for no filter:").lower()
        except:
            print ("Invalid input, not in range. Try again.")

    print('-'*40)
    return city, month, day


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

        # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    common_month = int(common_month - 1)
    common_month = months[common_month]
    print('Most Common month:', common_month)
        
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most Common Weekday:', common_day)
        
    # TO DO: display the most common start hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Start Hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_start = df['Start Station'].mode()[0]
    print('Most Common Start Station:', common_start)

    # TO DO: display most commonly used end station
    common_end = df['End Station'].mode()[0]
    print('Most Common End Station:', common_end)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combi = (df['Start Station'] + df['End Station']).mode()[0]
    print('Most Frequent Combination:', frequent_combi)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel = df['Trip Duration'].sum()
    travel_days = total_travel//86400
    travel_hour = total_travel//3600 - (travel_days*24)
    travel_minute = total_travel//60 - (travel_days*1440)-(travel_hour*60)
    travel_seconds = total_travel - (travel_days*86400)-(travel_minute * 60) - (travel_hour*3600)
    print('Total travel time:',travel_days, 'days', travel_hour, 'hours', travel_minute, 'minutes and', travel_seconds, 'seconds')

    # TO DO: display mean travel time
    mean_travel = df['Trip Duration'].mean()
    mean_minute = int(mean_travel//60)
    mean_seconds = int(mean_travel - (mean_minute * 60))
    print('Mean travel time (rounded to seconds):', mean_minute, 'minutes and', mean_seconds, 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_count = df['User Type'].value_counts()
    print('User Type Counts:\n', user_type_count)

    # TO DO: Display counts of gender
    if city != 'washington':
        gender_count = df['Gender'].value_counts()
        print('\n','Gender Counts:\n', gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
        common_year = int(df['Birth Year'].mode()[0])
        recent_year = int(df['Birth Year'].max())
        earliest_year = int(df['Birth Year'].min())
        print('\n','Most Common Birth Year:', common_year,'\n', 'Most Recent Birth Year:', recent_year, '\n', 'Earliest Birth Year:', earliest_year)
    else:
        print('No gender and year available')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Displays rwa data upon request."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    
    # TO DO: Display raw data if required
    raw = input("Do you want to see raw data? (yes or no)\n").lower()
    raws = ['yes' , 'no']
    while raw not in raws:
            try:
                print ("Invalid input, not in range. Try again.")
                raw = input("Do you want to see raw data? (yes or no)\n").lower()
                
            except:
                print ("Invalid input, not in range. Try again.")
    i = 0
    while raw == 'yes':
                   print(df.iloc[i:i+5]) # first five rows of dataframe
                   i = i+5
                   raw = input("Do you want to see more raw data? (yes or no)\n").lower()
                    
                   if raw != 'yes':
                      break
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40) 
    
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
