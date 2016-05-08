# file: plotMeanForceCoefficientsVsAoACompareKrishnanEtAl2014.py
# author: Olivier Mesnard (mesnardo@gwu.edu)
# description: Computes and plots the mean force coefficients 
#              versus the angle of attack 
#              and compares with results from Krishnan et al. (2014).


import os

from matplotlib import pyplot
from matplotlib import gridspec

from snake.ibamr.simulation import IBAMRSimulation
from snake.cuibm.simulation import CuIBMSimulation


aoa = [25, 30, 35, 40]

# compute mean coefficients of each IBAMR simulations with boundary markers
cd_boundary, cl_boundary = [], []
directory = os.path.join(os.environ['HOME'], 'simulations_IBAMR',
                         'flyingSnake2d', 'discretizedBoundary')
folders = ['flyingSnake2dRe1000AoA25_20150717',
           'flyingSnake2dRe1000AoA30_20150717',
           'flyingSnake2dRe1000AoA35_stabilized_20150907',
           'flyingSnake2dRe1000AoA40_20150717',
           'flyingSnake2dRe2000AoA25_stabilized_20150728',
           'flyingSnake2dRe2000AoA30_stabilized_20150907',
           'flyingSnake2dRe2000AoA35_stabilized_20150727',
           'flyingSnake2dRe2000AoA40_stabilized_20150907']
for folder in folders:
  simulation = IBAMRSimulation(directory=os.path.join(directory, folder))
  simulation.read_forces()
  simulation.get_mean_forces(limits=[32.0, 64.0])
  cd_boundary.append(-2.0*simulation.forces[0].mean['value'])
  cl_boundary.append(-2.0*simulation.forces[1].mean['value'])

# compute mean coefficients of each IBAMR simulations with body markers
cd_body, cl_body = [], []
directory = os.path.join(os.environ['HOME'], 'simulations_IBAMR',
                         'flyingSnake2d', 'discretizedBody')
folders = ['flyingSnake2dRe1000AoA25_20151123',
           'flyingSnake2dRe1000AoA30_20151123',
           'flyingSnake2dRe1000AoA35_20151123',
           'flyingSnake2dRe1000AoA40_20151123',
           'flyingSnake2dRe2000AoA25_20151119',
           'flyingSnake2dRe2000AoA30_20151123',
           'flyingSnake2dRe2000AoA35_20151115',
           'flyingSnake2dRe2000AoA40_20151123']
for folder in folders:
  simulation = IBAMRSimulation(directory=os.path.join(directory, folder))
  simulation.read_forces()
  simulation.get_mean_forces(limits=[32.0, 64.0])
  cd_body.append(-2.0*simulation.forces[0].mean['value'])
  cl_body.append(-2.0*simulation.forces[1].mean['value'])

# compute mean coefficients of each simulations from Krishnan et al. (2014)
cd_krishnan, cl_krishnan = [], []
for Re in [1000, 2000]:
  for a in aoa:
    directory = os.path.join(os.environ['SNAKE'],
                             'resources',
                             'flyingSnake2d_cuibm_anush',
                             'flyingSnake2dRe{}AoA{}'.format(Re, a))
    krishnan = CuIBMSimulation(directory=directory)
    krishnan.read_forces()
    krishnan.get_mean_forces(limits=[32.0, 64.0])
    cd_krishnan.append(2.0*krishnan.forces[0].mean['value'])
    cl_krishnan.append(2.0*krishnan.forces[1].mean['value'])

# plot mean drag coefficient versus angle of attack for Re=1000 and Re=2000
pyplot.style.use(os.path.join(os.environ['SNAKE'], 
                              'snake', 
                              'styles', 
                              'snakeReproducibility.mplstyle'))
fig = pyplot.figure(figsize=(6, 8))
gs = gridspec.GridSpec(3, 2, 
                       height_ratios=[1, 1, 0.5])
ax1 = pyplot.subplot(gs[0, :])
ax2 = pyplot.subplot(gs[1, :])
ax3 = pyplot.subplot(gs[2, 0])
ax4 = pyplot.subplot(gs[2, 1])
gs.update(wspace=0.5, hspace=0.1)
# drag coefficient versus angle-of-attack
ax1.grid(True, zorder=0)
ax1.set_ylabel('drag coefficient')
# Re=1000
l1, = ax1.plot(aoa, cd_boundary[:len(aoa)],  
               label='IBAMR (boundary markers)',
               color='#348ABD', 
               linestyle='-', 
               marker='o', 
               zorder=11)
l2, = ax1.plot(aoa, cd_body[:len(aoa)],  
               label='IBAMR (body markers)',
               color='#1B9E77', 
               linestyle='-', 
               marker='o', 
               zorder=12)
l3, = ax1.plot(aoa, cd_krishnan[:len(aoa)],  
               label='Krishnan et al. (2014)',
               color='#666666', 
               linestyle=':', 
               marker='o',
               markersize=8,
               markeredgewidth=2, 
               markeredgecolor='#111111', 
               markerfacecolor='none',
               zorder=10)
# Re=2000
l4, = ax1.plot(aoa, cd_boundary[len(aoa):],  
               label='IBAMR (boundary markers)',
               color='#A60628', 
               linestyle='-', 
               marker='s', 
               zorder=11)
l5, = ax1.plot(aoa, cd_body[len(aoa):],  
               label='IBAMR (body markers)',
               color='#D95F02', 
               linestyle='-', 
               marker='s', 
               zorder=12)
l6, = ax1.plot(aoa, cd_krishnan[len(aoa):],  
               label='Krishnan et al. (2014)',
               color='#666666', 
               linestyle='--', 
               marker='s',
               markersize=8,
               markeredgewidth=2, 
               markeredgecolor='#111111', 
               markerfacecolor='none',
               zorder=10)
ax1.set_xlim(aoa[0]-1.0, aoa[-1]+1.0)
ax1.set_xticks(aoa)
ax1.set_xticklabels([])
# lift coefficient versus angle-of-attack
ax2.grid(True, zorder=0)
ax2.set_xlabel('angle of attack')
ax2.set_ylabel('lift coefficient')
# Re=1000
ax2.plot(aoa, cl_boundary[:len(aoa)],  
         label='IBAMR (boundary markers)',
         color='#348ABD', 
         linestyle='-', 
         marker='o', 
         zorder=11)
ax2.plot(aoa, cl_body[:len(aoa)],  
         label='IBAMR (body markers)',
         color='#1B9E77', 
         linestyle='-', 
         marker='o',
         zorder=12)
ax2.plot(aoa, cl_krishnan[:len(aoa)],  
         label='Krishnan et al. (2014)',
         color='#666666', 
         linestyle=':',
         marker='o', 
         markersize=8,
         markeredgewidth=2, 
         markeredgecolor='#111111', 
         markerfacecolor='none',
         zorder=10)
# Re=2000
ax2.plot(aoa, cl_boundary[len(aoa):],  
         label='IBAMR (boundary markers)',
         color='#A60628', 
         linestyle='-', 
         marker='s', 
         zorder=11)
ax2.plot(aoa, cl_body[len(aoa):],  
         label='IBAMR (body markers)',
         color='#D95F02',
         linestyle='-', 
         marker='s',
         zorder=12)
ax2.plot(aoa, cl_krishnan[len(aoa):],  
         label='Krishnan et al. (2014)',
         color='#666666', linestyle='--', 
         marker='s',
         markersize=8,
         markeredgewidth=2, 
         markeredgecolor='#111111', 
         markerfacecolor='none',
         zorder=10)
ax2.set_xlim(aoa[0]-1.0, aoa[-1]+1.0)
aoa_labels = [str(a)+'$^o$' for a in aoa]
ax2.set_xticks(aoa)
ax2.set_xticklabels(aoa_labels)
# create legend
handles, labels = ax1.get_legend_handles_labels()
ax3.axis('off')
legend = ax3.legend(handles[:len(handles)/2], 
                    labels[:len(labels)/2], 
                    title='Re = 1000',
                    loc='lower left',
                    prop={'size': 9})
legend.get_title().set_fontsize('9')
ax4.axis('off')
legend = ax4.legend(handles[len(handles)/2:], 
                    labels[len(labels)/2:], 
                    title='Re = 2000',
                    loc='lower right',
                    prop={'size': 9})
legend.get_title().set_fontsize('9')
pyplot.savefig('ibamr_forceCoefficientsVsAoA.pdf',
               bbox_inches='tight',
               format='pdf')
