import numpy as np
import matplotlib.pyplot as plt


q=np.linspace(0., 2*np.pi, 100 )
p=np.linspace(-np.pi/2, np.pi/2, 100 )
r=9
x=r*np.outer(np.cos(q), np.cos(p))
y=r*np.outer(np.sin(q), np.cos(p))
z=(r*3)*np.outer(np.ones(np.size(q)), np.sin(p))
fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')
ax.plot_surface(x,y,z, cmap='plasma')
r=6
x1=r*np.outer(np.cos(q), np.cos(p))+1
y1=r*np.outer(np.sin(q), np.cos(p))-2
z1=(r*3)*np.outer(np.ones(np.size(q)), np.sin(p))+20
ax.plot_surface(x1,y1,z1, cmap='plasma')
r=3
x2=r*np.outer(np.cos(q), np.cos(p))+2
y2=r*np.outer(np.sin(q), np.cos(p))-4
z2=(r*3)*np.outer(np.ones(np.size(q)), np.sin(p))+35
ax.plot_surface(x2,y2,z2, cmap='plasma')