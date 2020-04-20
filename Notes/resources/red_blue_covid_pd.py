'''
Quick kivy COVID19 stat plotter
Data pulled from Johns Hopkins
plotted in matplotlib
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


data = pd.read_csv("http://covidtracking.com/api/states/daily.csv")
trend_days = 14
print(data.head())

dates = data["date"]
print(type(dates))
#dates.drop_duplicates(keep="last")

print(dates.head())



#
#
# red = ["AL", "AK", "AZ", "AR", "FL", "GA", "ID", "IN", "IA", "KS", "KY", "LA", "MI", "MS", "MO", "MT", "NE", "NC", "ND", "OH", "OK", "PA", "SC", "SD", "TN", "TX", "UT", "WV", "WI", "WY"]
# blue = ["CA", "CO", "CT", "DC", "DE", "HI", "IL", "ME", "MD", "MA", "MN", "NV", "NH", "NJ", "NM", "NY", "OR", "RI", "VT", "VA", "WA"]
#
# # states won by 10 or more
# red10 = ["AL", "AK", "AR", "ID", "IN", "KS", "KY", "LA", "MS", "MO", "MT", "NE", "ND", "OK", "SC", "SD", "TN", "UT", "WV", "WY"]
# blue10 = ["CA", "CT", "DC", "DE", "HI", "IL", "MD", "MA", "NJ", "NY", "OR", "RI", "VT", "WA"]
# blue10 = ["CA"]
#
# # make my plot
# dummy_dates = np.array([x for x in range(len(blue_positives_bydate))])
# blue_positives_bydate = np.asanyarray(blue_positives_bydate)
# red_positives_bydate = np.asanyarray(red_positives_bydate)
# blue10_bydate = np.asanyarray(blue_positives_bydate)
# red10_bydate = np.asanyarray(red_positives_bydate)
#
# fig = plt.figure(1, tight_layout=True, figsize=(10,8))
# ax = fig.add_subplot(111)
#
# ax.plot(dummy_dates, blue_positives_bydate, color="blue", marker=".", label="Clinton States")
# ax.plot(dummy_dates, red_positives_bydate, color="red", marker=".", label="Trump States")
#
# #plt.plot(dummy_dates, blue_positives_bydate, color="blue", marker=".", label="Clinton States")
# #plt.plot(dummy_dates, red_positives_bydate, color="red", marker=".", label="Trump States")
#
# ax.legend()
#
# ax.set_ylabel("positive tests (log)")
#
# date_labels = [str(x) for x in all_dates]
# date_labels = [x[4:6] + "/" + x[6:8] for x in date_labels]
#
# plt.title("Red/Blue Covid Trend")
# ax.set_yscale("log")
# plt.xticks(dummy_dates, date_labels, rotation=90)
#
#
# # best fits
# # blue state fit
# p = np.polyfit(dummy_dates[-trend_days:], np.log(blue_positives_bydate[-trend_days:]), 1)
# ax.semilogy([dummy_dates[-trend_days], dummy_dates[-1]], np.exp([p[0] * dummy_dates[-trend_days] + p[1], p[0] * dummy_dates[-1] + p[1]]), alpha=0.5, linestyle="--", color="black")
# mid = len(dummy_dates) // 2
# ax.annotate("Blue State Growth Rate {:.2f}".format(math.exp(p[0])), xy=(0, blue_positives_bydate[mid] * 1.5), color="darkblue", fontsize=10)
#
# # red state fit
# p = np.polyfit(dummy_dates[-trend_days:], np.log(red_positives_bydate[-trend_days:]), 1)
# ax.semilogy([dummy_dates[-trend_days], dummy_dates[-1]], np.exp([p[0] * dummy_dates[-trend_days] + p[1], p[0] * dummy_dates[-1] + p[1]]), alpha=0.5, linestyle="--", color="black")
#
# mid = len(dummy_dates) // 2
# ax.annotate("Red State Growth Rate {:.2f}".format(math.exp(p[0])), xy=(dummy_dates[mid] + 3, red_positives_bydate[mid]), color="darkred", fontsize=10)
#
# ax.grid(which="both", color="gray", alpha=0.5)
#
#
# # LANDSLIDE PLOT
# #
# # fig2 = plt.figure(2, tight_layout=True, figsize=(10,8))
# # ax2 = fig2.add_subplot(111)
# #
# #
# # ax2.set_ylabel("positive tests (log)")
# #
# # date_labels = [str(x) for x in all_dates]
# # date_labels = [x[4:6] + "/" + x[6:8] for x in date_labels]
# #
# # plt.title("Red/Blue Covid Trend in Landslide States")
# # ax2.set_yscale("log")
# # plt.xticks(dummy_dates, date_labels, rotation=90)
# #
# # ax2.plot(dummy_dates, blue10_bydate, color="blue", marker=".", label="Clinton by 10+% States")
# # ax2.plot(dummy_dates, red10_bydate, color="red", marker=".", label="Trump by 10+% States")
# #
# # # blue 10 fit
# # p = np.polyfit(dummy_dates[-trend_days:], np.log(blue10_bydate[-trend_days:]), 1)
# # ax2.semilogy([dummy_dates[-trend_days], dummy_dates[-1]],
# #              np.exp([p[0] * dummy_dates[-trend_days] + p[1], p[0] * dummy_dates[-1] + p[1]]), alpha=0.5, linestyle="--", color="black")
# # mid = len(dummy_dates) // 2
# # ax2.annotate("Blue 10 Growth Rate {:.2f}".format(math.exp(p[0])), xy=(0, blue10_bydate[mid] * 2), color="darkblue", fontsize=10)
# #
# # # red 10 fit
# # p = np.polyfit(dummy_dates[-trend_days:], np.log(red10_bydate[-trend_days:]), 1)
# # ax2.semilogy([dummy_dates[-trend_days], dummy_dates[-1]],
# #              np.exp([p[0] * dummy_dates[-trend_days] + p[1], p[0] * dummy_dates[-1] + p[1]]), alpha=0.5, linestyle="--", color="black")
# # mid = len(dummy_dates) // 2
# # ax2.annotate("Red 10 Growth Rate {:.2f}".format(math.exp(p[0])), xy=(dummy_dates[mid] + 3, red10_bydate[mid]), color="darkred", fontsize=10)
# #
# #
# # ax2.grid(which="both", color="gray", alpha=0.5)
# # ax2.legend()
#
# plt.show()
