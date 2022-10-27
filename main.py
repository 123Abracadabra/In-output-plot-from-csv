from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
from scipy.interpolate import make_interp_spline
from statistics import mean

# take data from csv file
style.use("ggplot")
# zmieniaj sobie tylko nazwe pliku
a_file = open("NewFile3.csv", "r")


string_without_line_breaks = ""
dane = ""
help=0
for line in a_file:
  stripped_line = line.rstrip()
  if help>1:
    string_without_line_breaks += stripped_line
  else: # take 2 first lanes
    dane+=stripped_line
  help += 1
a_file.close()

text,dane = string_without_line_breaks.split(',') ,dane.split(',')
start,step = float(dane[6]),float(dane[7])
# take vales to []
ch1=[float(text[i]) for i in range(len(text)-1) if i%2 ]
ch2=[float(text[i]) for i in range(len(text)-1) if not(i%2) ]
# take last elements to see stabilizacjon
help = ch1[-200:]
avrage=mean(help)
avrage= round(avrage,3)


time= [(start+(i)*(step)) for i in range (len(ch1))]

ch11=[]
ch22=[]
time11=[]

for i in range(len(time)):
  if time[i]>-0.0002:
    time11.append(time[i])
    ch11.append(ch1[i])
    ch22.append(ch2[i])

avr = [avrage for i in range(len(time11))]
ch1_ar,ch2_ar,time_ar,avr_ar = np.array(ch11),np.array(ch22),np.array(time11),np.array((avr))

Av_Time = make_interp_spline(time_ar,avr_ar)
Ch1_Time_Spline = make_interp_spline(time_ar,ch1_ar)
Ch2_Time_Spline = make_interp_spline(time_ar,ch2_ar)

X_ = np.linspace(time_ar.min(), time_ar.max(), 20)
Y_ = Ch1_Time_Spline(X_)
plt.plot(X_, Y_)
Y_ = Ch2_Time_Spline(X_)
plt.plot(X_, Y_)
Y_ = Av_Time(X_)
plt.plot(X_, Y_)

plt.title("Wykres")
plt.ylabel("h(t)[v]")
plt.xlabel("t[s]")

plt.savefig("zdjecie.png")
plt.show()