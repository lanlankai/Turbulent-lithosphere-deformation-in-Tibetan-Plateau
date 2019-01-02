# python file to plot MATLAB figure in Fig11.py
# Created on 18-Oct-2016

import matplotlib as mpl
from matplotlib.colors import LightSource, Normalize
# from colorspacious import cspace_converter
# from colormaps import cmaps
# import matplotlib.patches as mpatches
# from matplotlib.collections import PatchCollection
from matplotlib.patches import Arc

from matplotlib import rc
# rc('font',**{'family':'sans-serif','sans-serif':['Helvetica']})
import numpy as np
from pylab import *
import matplotlib.mlab as mlab
import scipy.io
import os
rc('text', usetex=True)
mpl.rcParams['text.latex.preamble'] = [
r'\usepackage{siunitx}',   # i need upright \micro symbols, but you need...
r'\sisetup{detect-all}',   # ...this to force siunitx to actually use your fonts
r'\usepackage{helvet}',    # set the normal font here
r'\usepackage{sansmath}',  # load up the sansmath so that math -> helvet
r'\usepackage{wasysym}', #
#r'\sansmath',#               # <- tricky! -- gotta actually tell tex to use!
]

f=scipy.io.loadmat("Fig01.mat");
fig = figure(figsize=(8.000000,6.000000))

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# prepare the plot
ax1 = fig.add_axes([0.115955, 0.110000, 0.691272, 0.815000],aspect='equal')
# set 1th plot -- surface
x1 = f["x1"]
x1 = squeeze(np.array(x1))
y1 = f["y1"]
y1 = squeeze(np.array(y1))
z1 = f["z1"]
z1 = squeeze(np.array(z1))
cmap = plt.cm.terrain
ls = LightSource(315, 45)

rgb = ls.shade(z1, cmap)
imshow(rgb, # topology
       interpolation='bilinear',
	    origin='lower',
		vmin=z1.min(),
		vmax=z1.max(),
		cmap=cm.viridis,
		extent=(x1.min(), x1.max(),y1.min(), y1.max()),
		alpha=0.8,
		)
# level1=np.arange(z1.min()-0.1,z1.max()+0.1,0.1)
# cs=ax1.contourf(x1,y1,z1,level#                                 origin='lower',
#                                 cmap=cm.jet,
#                                 linewidths=1,
#                                 alpha=1)

x = f["x"]
x = squeeze(np.array(x))
y = f["y"]
y = squeeze(np.array(y))
u = f["u"]
u = squeeze(np.array(u))
v = f["v"]
v = squeeze(np.array(v))
Q=u*u+v*v;
Q=sqrt(Q)
colors = np.random.rand(553)
# GPS velocity 
ax1.scatter(x, y,s=Q*5e1,c=colors,alpha=0.8,lw=1,edgecolors='none',cmap=cm.jet)

u1=u/Q
v1=v/Q


ax1.quiver(x,y,u1,v1,#Q,
 # linewidths=0.5,
 units='x',
 # pivot='tip',
 width=0.1,
 scale=1,
 )


# set 1th axis property
title(r'')
xlabel(r'Longitude',fontsize=14)
ylabel(r'Latitude',fontsize=14)
xtick = [70.000000, 75.000000, 80.000000, 85.000000, 90.000000, 95.000000, 100.000000, 105.000000, 110.000000]
xticklabel = [r'$70 $', r'$75 $', r'$80 $', r'$85 $', r'$90 $', r'$95 $', r'$100$', r'$105$', r'$110$']
ytick = [25.000000, 30.000000, 35.000000, 40.000000, 45.000000]
yticklabel = [r'$25$', r'$30$', r'$35$', r'$40$']
ax1.set_xscale('linear')
ax1.set_yscale('linear')
ax1.xaxis.set_ticks_position('both')
ax1.yaxis.set_ticks_position('both')

# ax1.grid(True)
xlim=(74.350000, 108.716667)
ylim=(22.716667, 41.950000)
setp(ax1, xticklabels=xticklabel, yticks=ytick, yticklabels=yticklabel, xticks=xtick, xlim=xlim, ylim=ylim)
for line in ax1.get_xticklines() + ax1.get_yticklines():
	line.set_markersize(10)

ann = ax1.annotate("",
                  xy=(95, 30), xycoords='data',
                  xytext=(96,30), textcoords='data',
                  size=15, va="center", ha="center",
                  bbox=dict(boxstyle="round4", fc="w"),
                  arrowprops=dict(arrowstyle="<|-",
                                  connectionstyle="arc3,rad=0",
								  shrinkA=5, shrinkB=5,
                                  patchA=None,
                                  patchB=None,
								  color=[1,0,0],
								  lw=1.0,
								#   connectionstyle="angle3,angleA=30,angleB=-30",
                                  fc=[1,0,0]),
                             	)

ann = ax1.annotate("",
                  xy=(97, 29.2), xycoords='data',
                  xytext=(98,28), textcoords='data',
                  size=15, va="center", ha="center",
                  bbox=dict(boxstyle="round4", fc="w"),
                  arrowprops=dict(arrowstyle="<|-",
                                  connectionstyle="arc3,rad=0",
								  shrinkA=5, shrinkB=5,
                                  patchA=None,
                                  patchB=None,
								  color=[1,0,0],
								  lw=1.0,
								#   connectionstyle="angle3,angleA=30,angleB=-30",
                                  fc=[1,0,0]),
                             	)

ann = ax1.annotate("",
                  xy=(92.125, 28), xycoords='data',
                  xytext=(92.4,29), textcoords='data',
                  size=15, va="center", ha="center",
                  bbox=dict(boxstyle="round4", fc="w"),
                  arrowprops=dict(arrowstyle="<|-",
                                  connectionstyle="arc3,rad=0",
								  shrinkA=5, shrinkB=5,
                                  patchA=None,
                                  patchB=None,
								  color=[1,0,0],
								  lw=1.0,
								#   connectionstyle="angle3,angleA=30,angleB=-30",
                                  fc=[1,0,0]),
                             	)


# circle = plt.Circle((95,28), 2, color='red', fill=False)
# fig.gca().add_artist(circle)
x = f["x2"]
x = squeeze(np.array(x))
y = f["y2"]
y = squeeze(np.array(y))
ax1.plot(x,y-1.0,'r-',lw=1.5)

x = f["x3"]
x = squeeze(np.array(x))
y = f["y3"]
y = squeeze(np.array(y))
ax1.plot(x[0:800],y[0:800],'r-',lw=1.5)


ann = ax1.annotate("",
                  xy=(102, 39), xycoords='data',
                  xytext=(103,38.5), textcoords='data',
                  size=15, va="center", ha="center",
                  bbox=dict(boxstyle="round4", fc="w"),
                  arrowprops=dict(arrowstyle="<|-",
                                  connectionstyle="arc3,rad=0",
								  shrinkA=5, shrinkB=5,
                                  patchA=None,
                                  patchB=None,
								  color=[1,0,0],
								  lw=1.0,
								#   connectionstyle="angle3,angleA=30,angleB=-30",
                                  fc=[1,0,0]),
                             	)

ann = ax1.annotate("",
                  xy=(103.8, 37.5), xycoords='data',
                  xytext=(104.25,36.5), textcoords='data',
                  size=15, va="center", ha="center",
                  bbox=dict(boxstyle="round4", fc="w"),
                  arrowprops=dict(arrowstyle="<|-",
                                  connectionstyle="arc3,rad=0",
								  shrinkA=5, shrinkB=5,
                                  patchA=None,
                                  patchB=None,
								  color=[1,0,0],
								  lw=1.0,
								#   connectionstyle="angle3,angleA=30,angleB=-30",
                                  fc=[1,0,0]),
                             	)
ann = ax1.annotate("",
                  xy=(100, 39.5), xycoords='data',
                  xytext=(101,39.5), textcoords='data',
                  size=15, va="center", ha="center",
                  bbox=dict(boxstyle="round4", fc="w"),
                  arrowprops=dict(arrowstyle="<|-",
                                  connectionstyle="arc3,rad=0",
								  shrinkA=5, shrinkB=5,
                                  patchA=None,
                                  patchB=None,
								  color=[1,0,0],
								  lw=1.0,
								#   connectionstyle="angle3,angleA=30,angleB=-30",
                                  fc=[1,0,0]),
                             	)


# prepare the colorbar
cmap = mpl.cm.terrain
ax2 = fig.add_axes([0.825000, 0.260018, 0.035714, 0.515678])
bounds = [0,2000,4000,6000,8000]
yticklabel = [r'$0$',r'$2000$',r'$4000$',r'$6000$',r'$8000$']
norm = mpl.colors.Normalize(vmin=-38.000000, vmax=8271.000000)
cb1 = mpl.colorbar.ColorbarBase(ax2, cmap=cmap,norm=norm,ticks=bounds,orientation='vertical')
setp(ax2,yticks=bounds,yticklabels=yticklabel)
ax2.set_ylabel(r'Topography $\si{m}$')

ax1.plot([78,83],[24,24],'-',color=[1,1,1],lw=4)
ax1.text(79,24.5,r'$\textbf{500\,\si{km}}$',fontsize=10,color=[1,1,1])
#leg1 = ax1.legend(
#  loc='lower left',ncol=1, shadow=True,markerscale=1.25,frameon=True,fancybox=True,numpoints=2)
# ax1.tick_params(axis='both', which='major', labelsize=10)
# ax1.tick_params(axis='both', which='minor', labelsize=8)

#prepare the output
# plt.savefig('Fig11.eps',bbox_inches='tight')
plt.savefig('Fig01.pdf',bbox_inches='tight',transparent=True)
# plt.savefig('Fig11.png',dpi=300,bbox_inches='tight',transparent=True)

# os.system('epscrop Fig11')
# os.system('open Fig11.pdf')
# os.system('open Fig11.py')
