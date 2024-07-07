import scheduler
import numpy as np
import pandas as pd

nteams = 4
nfields = 3
bestfields = 1

teams = ['Team ' + str(z+1) for z in range(nteams)]
games = scheduler.get_best_schedule(teams, nfields, bestfields)

# Field distribution quality

field_distribution_quality = scheduler.get_aggregate_data(games)
print(field_distribution_quality)
# Schedule quality
schedule_quality = np.array(scheduler.get_gap_info(games))   # gaps between games (rows are teams)
print(schedule_quality)
# Save the schedule to csv

schedule = scheduler.pivot_schedule(games)
print(schedule)
# schedule.to_csv('schedule.csv')