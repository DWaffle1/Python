import numpy as np
import matplotlib.pyplot as plt


q=np.linspace(0., 2*np.pi, 100 )
p=np.linspace(-np.pi/2, np.pi/3, 100 )
[p,q]=np.meshgrid(p,q)
r=5
x=r*np.cosh(p)*np.cos(q)+7
y=r*np.cosh(p)*np.sin(q)-9
z=((r)*np.sinh(p))+6
fig=plt.figure()
ax=fig.add_subplot(111, projection='3d')
ax.plot_surface(x,y,z, color="black" , alpha=1)
r=12
q=np.linspace(0., 2*np.pi, 100 )
p=np.linspace(-np.pi/2, 0, 100 )
[p,q]=np.meshgrid(p,q)
x=r*np.cos(p)*np.cos(q)+11
y=r*np.cos(p)*np.sin(q)-17
z=(r)*np.sin(p)
fig=plt.figure()
ax.plot_surface(x,y,z,color="black", alpha=1)