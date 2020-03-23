'''
Quick kivy COVID19 stat plotter
Data pulled from Johns Hopkins
plotted in matplotlib
'''


import requests
import csv
import matplotlib.pyplot as plt

# kivy imports
from kivy.garden.matplotlib.backend_kivyagg import FigureCanvasKivyAgg
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout



def get_data(url):
    with requests.Session() as s:
        download = s.get(url)
        decoded_content = download.content.decode('utf-8')
        cr = csv.reader(decoded_content.splitlines(), delimiter=',')  # csv reader object
        my_list = list(cr)
        header = my_list.pop(0)
    return header, my_list


confirmed_headers, confirmed = get_data("https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_19-covid-Confirmed.csv&filename=time_series_2019-ncov-Confirmed.csv")

death_headers, deaths = get_data("https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_19-covid-Deaths.csv&filename=time_series_2019-ncov-Deaths.csv")

recovered_headers, recovered = get_data("https://data.humdata.org/hxlproxy/api/data-preview.csv?url=https%3A%2F%2Fraw.githubusercontent.com%2FCSSEGISandData%2FCOVID-19%2Fmaster%2Fcsse_covid_19_data%2Fcsse_covid_19_time_series%2Ftime_series_19-covid-Recovered.csv&filename=time_series_2019-ncov-Recovered.csv")





# alternate way to grab CSV locally

# with open("time_series_2019-ncov-Confirmed.csv") as f:
#     reader = csv.reader(f)
#     confirmed = list(reader)
#
# with open("time_series_2019-ncov-Deaths.csv") as f:
#     reader = csv.reader(f)
#     deaths = list(reader)
#
# with open("time_series_2019-ncov-Recovered.csv") as f:
#     reader = csv.reader(f)
#     recovered = list(reader)


# plt.show()
class CovidApp(App):
    def build(self):
        self.layout = CovidLayout()
        self.canvas = FigureCanvasKivyAgg(plt.gcf())
        self.layout.plot_canvas = self.canvas
        self.layout.add_widget(self.canvas)
        self.layout.make_plot()
        return self.layout

class CovidLayout(BoxLayout):
    def __init__(self):
        self.confirmed = confirmed
        self.recovered = recovered
        self.deaths = deaths
        self.plot_deaths = True
        self.plot_confirmed = True
        self.plot_recovered = True
        self.use_country = False  # do you want to use country name.  Default is a US State
        self.country = "US"
        self.my_state = "Illinois"
        self.start_date = "3/1/20"
        self.width = 10
        self.height = 8
        self.my_name = self.my_state

        self.countries = [x[1] for x in self.confirmed]
        self.country_list = [x[1] for x in self.confirmed if x[0] == ""]
        self.country_list.sort()
        #print(self.country_list)
        self.states = [x[0] for x in self.confirmed]
        self.states_list = [x for x in self.states if x != ""]
        self.states_list.sort()
        self.dates = confirmed_headers[4:]
        self.date_index = 4
        self.date_index_end = len(confirmed_headers)
        self.fig = plt.figure("COVID Graph 1", figsize=(self.width, self.height), tight_layout=True)
        self.ax = self.fig.gca()
        self.ax.grid(color='lightgray')
        plt.xlabel("Date")
        plt.ylabel("Cases")
        super().__init__()

    def cases_toggle(self, check_state):
        if check_state:
            self.plot_confirmed = True
        else:
            self.plot_confirmed = False
        self.make_plot()

    def deaths_toggle(self, check_state):
        if check_state:
            self.plot_deaths = True
        else:
            self.plot_deaths = False
        self.make_plot()

    def recovered_toggle(self, check_state):
        if check_state:
            self.plot_recovered = True
        else:
            self.plot_recovered = False
        self.make_plot()

    def plot_country(self, country):
        print(country)
        self.use_country = True
        self.country = country
        self.make_plot()
        #self.state_spin.text = "Select State"

    def plot_state(self, state):
        print(state)
        self.use_country = False
        self.my_state = state
        self.make_plot()

    def start_change(self, start):
        self.start_date = start
        self.date_index = self.dates.index(start)
        if self.date_index >= self.date_index_end:
            self.date_index_end = len(self.dates) - 1
        self.make_plot()

    def end_change(self, end):
        self.end_date = end
        self.date_index_end = self.dates.index(end)
        self.make_plot()

    def make_plot(self):
        if self.date_index >= self.date_index_end:
            return
        print("Make plot")
        plt.clf()

        # # build the graph
        if self.use_country:
            self.my_name = self.country
        else:
            self.my_name = self.my_state

        print(self.my_name)

        # # find the index of the start date
        self.date_index = confirmed_headers.index(self.start_date)
        plt.title(self.my_name + " COVID19 ", color="blue", fontsize=20)


        # tease out confirmed cases in country/state
        self.confirmed_states = [x[0] for x in confirmed]
        self.confirmed_countries = [x[1] for x in confirmed]
        for i in range(len(self.confirmed_states)):
            print(self.confirmed_states[i], self.confirmed_countries[i])

        self.state_index = self.confirmed_states.index(self.my_state)
        self.country_index = self.confirmed_countries.index(self.country)
        x_numbers = [x for x in range(len(confirmed_headers[self.date_index:self.date_index_end + 1]))]

        if self.use_country:
            if confirmed[self.country_index][-1] == "":
                confirmed[self.country_index].pop(-1)
                recovered[self.country_index].pop(-1)
                deaths[self.country_index].pop(-1)
                x_numbers.pop(-1)
        else:
            if confirmed[self.state_index][-1] == "":
                confirmed[self.state_index].pop(-1)
                recovered[self.state_index].pop(-1)
                deaths[self.state_index].pop(-1)
                x_numbers.pop(-1)

        if self.plot_confirmed:
            if self.use_country:
                plt.plot(x_numbers, [int(x) for x in confirmed[self.country_index][self.date_index:self.date_index_end + 1]], label="Confirmed Cases",
                         marker=".")
            else:
                plt.plot(x_numbers, [int(x) for x in confirmed[self.state_index][self.date_index:self.date_index_end + 1]], label="Confirmed Cases",
                         marker=".")

        # deaths in state or country
        # death_headers = deaths.pop(0)
        print(death_headers)
        death_states = [x[0] for x in deaths]
        death_countries = [x[1] for x in confirmed]

        if self.plot_deaths:
            if self.use_country:
                plt.plot(x_numbers, [int(x) for x in deaths[self.country_index][self.date_index:self.date_index_end + 1]], label="Deaths", color='red',
                         marker=".")
            else:
                plt.plot(x_numbers, [int(x) for x in deaths[self.state_index][self.date_index:self.date_index_end + 1]], label="Deaths", color='red',
                         marker=".")

        # recovered
        if self.plot_recovered:
            if self.use_country:
                plt.plot(x_numbers, [int(x) for x in recovered[self.country_index][self.date_index:self.date_index_end + 1]], label="Recovered", color='green', marker=".")
            else:
                plt.plot(x_numbers, [int(x) for x in recovered[self.state_index][self.date_index:self.date_index_end + 1]], label="Recovered", color='green', marker=".")
        plt.xticks(x_numbers, confirmed_headers[self.date_index:self.date_index_end], rotation=90, fontsize=7)
        plt.legend(fontsize="large", shadow=True)
        self.plot_canvas.draw()



if __name__== "__main__":
    CovidApp().run()



