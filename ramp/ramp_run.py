# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 14:35:00 2019
This is the code for the open-source stochastic model for the generation of
multi-energy load profiles in off-grid areas, called RAMP, v.0.2.1-pre.
@authors:
- Francesco Lombardi, Politecnico di Milano
- Sergio Balderrama, Université de Liège
- Sylvain Quoilin, KU Leuven
- Emanuela Colombo, Politecnico di Milano
Copyright 2019 RAMP, contributors listed above.
Licensed under the European Union Public Licence (EUPL), Version 1.1;
you may not use this file except in compliance with the License.
Unless required by applicable law or agreed to in writing,
software distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and limitations
under the License.
"""

# %% Import required modules

from core.stochastic_process import Stochastic_Process
from post_process.post_process import *

#Set the year and the month number you want to simulate
year = 2022
month = 1
full_month = True
# Calls the stochastic process and saves the result in a list of stochastic profiles
# In this default example, the model runs for 2 input files ("input_file_1", "input_file_2"),
# but single or multiple files can be run restricting or enlarging the iteration range
# and naming further input files with progressive numbering
input_files_to_run = [month]

for j in input_files_to_run:
    Profiles_list = Stochastic_Process(full_month, year,month,j)

    # Post-processes the results and generates plots
    Profiles_avg, Profiles_list_kW, Profiles_series = Profile_formatting(Profiles_list)
    Profile_series_plot(Profiles_series)  # by default, profiles are plotted as a series

    #Time_adj_profiles = Profile_dataframe(Profiles_series, year)

    #Time_adj_profiles.resample('H').sum().to_csv('results/%s.csv' % j)
    export_series(Profiles_series,year,month,full_month)

    if len(Profiles_list) > 1:  # if more than one daily profile is generated, also cloud plots are shown
        Profile_cloud_plot(Profiles_list, Profiles_avg,month)