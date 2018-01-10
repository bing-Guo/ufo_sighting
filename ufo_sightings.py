# Filename: ufo_sightings.py
# Date:     2018/01/07
# Author:   Bing

# coding: utf-8
import pandas as pd
from datetime import datetime
import re
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
import numpy as np

# load data
ufo = pd.read_table('data/ufo_awesome.tsv', sep='\t', header=None, error_bad_lines=False)

# cleaning data
# rename columns name of dataframe 
ufo.columns = ['DateOccurred', 'DateReported','Location','ShortDescription','Duration','LongDescription']

# check data construction
ufo.head()
ufo.tail()
ufo.dtypes
ufo.describe()

# clean DATE
## DateOccurred and DateReported transform int into string
ufo['DateOccurred'] = ufo['DateOccurred'].apply(str)  
ufo['DateReported'] = ufo['DateReported'].apply(str)

## some part of length of DateOccurred is 0
ufo = ufo.loc[ufo['DateOccurred'].str.len() == 8]

## let DateOccurred divide into year and month
ufo['DateOccurred_Y'] = [i[:4] for i in ufo['DateOccurred']]
ufo['DateOccurred_M'] = [i[4:6] for i in ufo['DateOccurred']]

# clean LOCATION
## location split into city and state
def getLocation(l):
    try:
        regexLocation = re.sub(r'[(]{1}[\S\s]*[)]{1}', '', l)
        splitLocation = regexLocation.split(',')
        cleanLocation = list(map(str.strip, splitLocation))
        if len(cleanLocation) <= 2:
            return cleanLocation
        else:
            return['','']
    except:
        return ['','']
    
cityState = [getLocation(i) for i in ufo['Location']]
df_cityState = pd.DataFrame(cityState, columns=['USCity','USState'])

## join ufo and cityState
ufo = pd.concat([ufo, df_cityState], axis=1)

## convert to lower case
ufo['USCity'] = ufo['USCity'].str.lower()
ufo['USState'] = ufo['USState'].str.lower()

## limit range in USA state
usstates = ['ak','al','ar','az','ca','co','ct','de','fl','ga','hi','ia','id','il','in','ks','ky','la','ma','md','me','mi','mn','mo','ms','mt','nc','nd','ne','nh','nj','nm','nv','ny','oh','ok','or','pa','ri','sc','sd','tn','tx','ut','va','vt','wa','wi','wv','wy']
usufo = ufo[ufo['USState'].isin(usstates)]

# UFO Sighting Distribution
## count ufo occurred date each year
date_occurred_count_forYear = usufo.groupby(['DateOccurred_Y']).size().reset_index(name='counts')

## draw Bar chart
plt.figure(num=1, figsize=(10,5))

x = date_occurred_count_forYear['DateOccurred_Y'].apply(int)
y = date_occurred_count_forYear['counts']
plt.bar(x,y,width=3,color="#91AAB4")

plt.xticks(np.arange(min(x), max(x), 50.0), rotation=35)

plt.xlabel('year')
plt.ylabel('counts')
plt.title('UFO Sighting')
plt.show()
# fig.savefig('ufo1.png')

## draw Bar chart 1990 - 2010
plt.figure(num=2, figsize=(10,5))

x = date_occurred_count_forYear['DateOccurred_Y'].apply(int)
y = date_occurred_count_forYear['counts']
plt.bar(x,y,color="#91AAB4")

minYear = 1990
maxYear = 2010
plt.xlim(minYear,maxYear)

plt.xticks(np.arange(minYear, maxYear+1, 5), rotation=35)

plt.xlabel('year')
plt.ylabel('counts')
plt.title('UFO Sighting(1990-2010)')
plt.show()
# fig.savefig('ufo2.png')

# time distribution of ufo sighting for every state between 1990 and 2010
## filter out greater than 1990

usufo = usufo.loc[usufo['DateOccurred_Y'] >= '1990']
usufo['YearMonth'] = usufo['DateOccurred_Y'].apply(str)+usufo['DateOccurred_M'].apply(str)
sightings = usufo[['YearMonth','USState']]
sightings.columns = ['yearMonth','state']

## count number of sighting
sightings = sightings.groupby(['yearMonth','state']).size().reset_index(name='sighting')

# we must to fill the date that don't exist in sighting data.
## create all combinations for state and date 
minMonth = '1990'
maxMonth = '2011'
date_series = [datetime.strftime(x,'%Y%m') for x in list(pd.date_range(start=minMonth, end=maxMonth, freq = 'M'))]
state_sighting_series = pd.DataFrame(columns=['state','yearMonth'])
for s in usstates:
    df = pd.DataFrame(date_series,columns=['yearMonth'])
    df['state'] = s
    state_sighting_series = pd.concat([state_sighting_series,df])

## left join
allSightings = pd.merge(state_sighting_series, sightings, on=['state','yearMonth'], how='left')

## cleaning DATE
allSightings['yearMonth'] = pd.to_datetime(allSightings['yearMonth'], format='%Y%m')
allSightings = allSightings.fillna(0)

# draw date plots for each state
fig, ax = plt.subplots(figsize=(20, 20))

for i in range(len(usstates)):
    state = usstates[i]
    plt.subplot(10,5,i+1)
    df = allSightings.loc[allSightings['state'] == state]
    x = df['yearMonth']
    y = df['sighting']
    ax.xaxis.set_major_formatter(DateFormatter('%Y'))
    plt.title(state)
    plt.tight_layout()
    plt.plot(x,y,color="darkblue")
    plt.grid(True)
    plt.ylim(0,80)

plt.show()
# fig.savefig('ufo3.png')

