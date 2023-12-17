import pyvista as pv
import rioxarray as riox
import numpy as np

# Reading in the data
data = riox.open_rasterio("data/input/dem.tif")

data = data[0]

# Saving the raster data as array
values = np.asarray(data)

# Creating meshgrid
x, y = np.meshgrid(data['x'], data['y'])

# Setting zz values
z = np.zeros_like(x)

# Creating Structured Grid
mesh = pv.StructuredGrid(x, y, z)

# Assign Elevation Values
mesh["Elevation"] = values.ravel(order='F')

topo = mesh.warp_by_scalar(scalars="Elevation", factor=0.000015)


p = pv.Plotter()

p.add_mesh(mesh=topo, scalars=topo["Elevation"], cmap='terrain')

p.show_grid(color='black')
p.set_background(color='white')
p.show(cpos="xy")
