# -*- coding: utf-8 -*-

# %% Initialisation of a model instance

from ramp.core.core import np, pd
import importlib
import datetime
import calendar
#import pytz

# Import holidays package
#import holidays

def month_day_number(year, j):
    if calendar.isleap(year):
        year_len = 366
    else:
        year_len = 365

    if j == 1:
        return (31)
    if j == 2:
        return (28) if year_len == 365 else (29)
    if j == 3:
        return (31)
    if j == 4:
        return (30)
    if j == 5:
        return (31)
    if j == 6:
        return (30)
    if j == 7:
        return (31)
    if j == 8:
        return (31)
    if j == 9:
        return (30)
    if j == 10:
        return (31)
    if j == 11:
        return (30)
    if j == 12:
        return (31)


def yearly_pattern(year,month):
    '''
    Definition of a yearly pattern of weekends and weekdays, in case some appliances have specific wd/we behaviour
    '''

    # Yearly behaviour pattern
    first_day = datetime.date(year, month, 1).strftime("%A")
    month_len = month_day_number(year,month)

    if month == 1:
        holidays_list = [datetime.datetime(year, 1, 1)]
    elif month == 2:
        holidays_list = [datetime.datetime(year, 2, 12)]
    elif month == 3:
        holidays_list = [datetime.datetime(year, 3, 11),datetime.datetime(year, 3, 14),
                      datetime.datetime(year, 3, 20),datetime.datetime(year, 3, 29)]
    elif month == 4:
        holidays_list = [datetime.datetime(year, 4, 2), datetime.datetime(year, 4, 4)]
    elif month == 5:
        holidays_list = [datetime.datetime(year, 5, 1), datetime.datetime(year, 5, 13),
                      datetime.datetime(year, 5, 14),datetime.datetime(year, 5, 26)]
    elif month == 6:
        holidays_list = [datetime.datetime(year, 6, 1), datetime.datetime(year, 6, 21)]
    elif month == 7:
        holidays_list = [datetime.datetime(year, 7, 20)]
    elif month == 8:
        holidays_list = [datetime.datetime(year, 8, 10), datetime.datetime(year, 8, 17),
                      datetime.datetime(year, 8, 22), datetime.datetime(year, 8, 30)]
    elif month == 9:
        holidays_list = [datetime.datetime(year, 9, 10), datetime.datetime(year, 9, 23)]
    elif month == 10:
        holidays_list= [datetime.datetime(year, 10, 7), datetime.datetime(year, 10, 15),
                      datetime.datetime(year, 10, 19)]
    elif month == 11:
        holidays_list= [datetime.datetime(year, 11, 4)]
    else:
        holidays_list= [datetime.datetime(year, 12, 21), datetime.datetime(year, 12, 24),
                      datetime.datetime(year, 12, 25),datetime.datetime(year, 12, 31)]


    Year_behaviour = np.ones(month_len)

    dict_year = {'Monday': [5, 6],
                 'Tuesday': [4, 5],
                 'Wednesday': [3, 4],
                 'Thursday': [2, 3],
                 'Friday': [1, 2],
                 'Saturday': [0, 1],
                 'Sunday': [6, 0]}

    for d in dict_year.keys():
        if first_day == d:
            Year_behaviour[dict_year[d][0]:month_len:7] = 2
            Year_behaviour[dict_year[d][1]:month_len:7] = 2

    for i in range(len(holidays_list)):
        day_of_month = holidays_list[i].timetuple().tm_mday
        Year_behaviour[day_of_month - 1] = 2

    #hourly_year_behaviour = pd.DataFrame([int(y) for x in Year_behaviour for y in (x,)*24])

    return (Year_behaviour)


def user_defined_inputs(j):
    '''
    Imports an input file and returns a processed User_list
    '''

    file_module = importlib.import_module(f'input_files.input_file_{j}')

    User_list = file_module.User_list

    return (User_list)


def Initialise_model(full_month, year, month):
    '''
    The model is ready to be initialised
    '''

    Profile = []  # creates an empty list to store the results of each code run, i.e. each stochastically generated profile
    # Simulating n days before and after the wished number of profiles
    if full_month:
        num_profiles_user = month_day_number(year, month)
    else:
        num_profiles_user = int(input(
            "Please indicate the number of profiles (days) to be generated: "))  # asks the user how many profiles (i.e. code runs) they want

    assert 1 <= num_profiles_user <= 31, '[CRITICAL] Incorrect number of profiles, please provide a number higher than 0, up to 366'
    print('Please wait...')
    num_profiles = num_profiles_user

    return (Profile, num_profiles)


def Initialise_inputs(year,month,j):
    Year_behaviour = yearly_pattern(year,month)
    user_list = user_defined_inputs(j)

    # Calibration parameters
    '''
    Calibration parameters. These can be changed in case the user has some real data against which the model can be calibrated
    They regulate the probabilities defining the largeness of the peak window and the probability of coincident switch-on within the peak window
    '''
    peak_enlarg = 0.15  # percentage random enlargement or reduction of peak time range length
    mu_peak = 0.5  # median value of gaussian distribution [0,1] by which the number of coincident switch_ons is randomly selected
    s_peak = 0.5  # standard deviation (as percentage of the median value) of the gaussian distribution [0,1] above mentioned
    op_factor = 0.5

    return (peak_enlarg, mu_peak, s_peak,op_factor, Year_behaviour, user_list)