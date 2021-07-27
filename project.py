import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd


df = pd.read_csv("Sp.csv")

mathscore = df['mathscore'].tolist()

readingscore = df['readingscore'].tolist()

mathscoremean = statistics.mean(mathscore)

readingscoremean = statistics.mean(readingscore)

mathscoremedian = statistics.median(mathscore)

readingscoremedian = statistics.median(readingscore)

mathscoremode = statistics.mode(mathscore)

readingscoremode = statistics.mode(readingscore)


print('Mean,Median,Mode of the mathscore is {}, {} and {} respectively'.format(mathscoremean,mathscoremedian,mathscoremode))

print('Mean,Median,Mode of the readingscore is {}, {} and {} respectively'.format(readingscoremean,readingscoremedian,readingscoremode))


#standard deviation

mathscorestd = statistics.stdev(mathscore)
readingscorestd = statistics.stdev(readingscore)

mathscore1SDstart,mathscore1SDend = mathscoremean-mathscorestd,mathscoremean+mathscorestd
mathscore2SDstart,mathscore2SDend = mathscoremean-(2*mathscorestd),mathscoremean+(2*mathscorestd)
mathscore3SDstart,mathscore3SDend = mathscoremean-(3*mathscorestd),mathscoremean+(3*mathscorestd)

readingscore1SDstart,readingscore1SDend = readingscoremean-readingscorestd,readingscoremean+readingscorestd
readingscore2SDstart,readingscore2SDend = readingscoremean-(2*readingscorestd),readingscoremean+(2*readingscorestd)
readingscore3SDstart,readingscore3SDend = readingscoremean-(3*readingscorestd),readingscoremean+(3*readingscorestd)

# Calculating percentage

mathscoredata_1SD = [result for result in mathscore if result>mathscore1SDstart and result<mathscore1SDend]
mathscoredata_2SD = [result for result in mathscore if result>mathscore2SDstart and result<mathscore2SDend]  
mathscoredata_3SD = [result for result in mathscore if result>mathscore3SDstart and result<mathscore3SDend] 

readingscoredata_1SD = [result for result in readingscore if result>readingscore1SDstart and result<readingscore1SDend]
readingscoredata_2SD = [result for result in readingscore if result>readingscore2SDstart and result<readingscore2SDend]  
readingscoredata_3SD = [result for result in readingscore if result>readingscore3SDstart and result<readingscore3SDend] 

print('{} % of mathscoredata lies in 1STD'.format(len(mathscoredata_1SD)*100/len(mathscore)))
print("{} % of mathscoredata lies in 2STD".format(len(mathscoredata_2SD)*100/len(mathscore)))
print('{} % of mathscoredata lies in 3STD'.format(len(mathscoredata_3SD)*100/len(mathscore)))

print('{} % of readingscoredata lies in 1STD'.format(len(readingscoredata_1SD)*100/len(readingscore)))
print('{} % of readingscoredata lies in 2STD'.format(len(readingscoredata_2SD)*100/len(readingscore)))
print('{} % of readingscoredata lies in 3STD'.format(len(readingscoredata_3SD)*100/len(readingscore)))