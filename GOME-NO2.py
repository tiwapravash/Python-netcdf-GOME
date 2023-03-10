#Today we will try to plot the global tropospheric NO2 column using simple libraries of python namely xarray, cartopy and matplotlib.

#Data is sourced from :  https://atmos.eoc.dlr.de/products/ 

#I will be using level 3 NO2 global data from the available products for the year 2016.
#The data-set are available in netcdf(.nc) format.

Lets begin !!!:
#% /usr/bin/env python
import numpy as np
import xarray as xr
import cartopy.crs as ccrs
import cartopy.feature as ftr
from datetime import datetime
from matplotlib import pyplot as plt
date=datetime(2016,1,1)
#Make a loop to open all the months one after the other
mean_value=0
##### If you wish to calculate for seasonal #### specify dates as follows
#Winter
#all_date=[datetime(2016,1,1),datetime(2016,2,1),datetime(2016,12,1)]
#spring
#all_date=[datetime(2016,3,1),datetime(2016,4,1),datetime(2016,5,1)]
#summer
#all_date=[datetime(2016,6,1),datetime(2016,7,1),datetime(2016,8,1)]
#autumn
#all_date=[datetime(2016,9,1),datetime(2016,10,1),datetime(2016,11,1)]
all_date=[datetime(2016,1,1),datetime(2016,2,1),datetime(2016,3,1),datetime(2016,4,1),datetime(2016,5,1),datetime(2016,6,1),datetime(2016,7,1),datetime(2016,8,1),datetime(2016,9,1),datetime(2016,10,1),datetime(2016,11,1),datetime(2016,12,1)]
for date in all_date:
    path="D:/CAS/UCAS_Study/Conference/ACAM Malayasia conference/Miniproject/NO2 GOME/"+date.strftime('%Y')+" NO2/"
    file_name="GOME_NO2_Global_"+date.strftime('%Y%m')+"_METOPA_DLR_v1.nc"
    data=xr.open_dataset(path+file_name)
    prod=xr.open_dataset(path+file_name, group="PRODUCT")
    data["NO2trop"]=prod.NO2trop
    plt_data=data.sel({"latitude": slice(-90,90),"longitude": 
slice(-180,180)})      ####Global plot ########
     mean_value=(mean_value+plt_data.NO2trop)
#Figure size
fig=plt.figure(figsize=[20,16])
#fig.set_dpi(400)
minv=0
maxv=1.5e16
levels=np.log10(np.array((np.arange(100)+1)*(maxv-minv)/99+minv))
spl=plt.axes(projection=ccrs.PlateCarree())

ax=plt.contourf(plt_data.longitude,plt_data.latitude,np.log10(mean_value/len(all_date)),levels=levels,\transform=ccrs.PlateCarree(),zorder=0,cmap='jet')
plt.title(date.strftime('2016_GlobeNO2'))
#show study area, specific point
#plt.scatter(94.73,29.77,transform=ccrs.PlateCarree(),c='r',s=10)
spl.set_xticks([-180,-120,-60,0,60,120,180],crs=ccrs.PlateCarree())
spl.set_yticks([-90,-60,-30,0,30,60,90],crs=ccrs.PlateCarree())
spl.coastlines()
spl.add_feature(ftr.BORDERS)
#for the side bar coordinate
#spl.set_xticks([50,60,70,80,90,100,110],crs=ccrs.PlateCarree())
#spl.set_yticks([20,30,40],crs=ccrs.PlateCarree())
#spl.gridlines()
#fig.add_axes([0.1])
fig.colorbar(ax,label="log10 "+prod.NO2trop.units,orientation="horizontal")
plt.savefig('NO2'+date.strftime('2016_GlobeNO2')+'.png', bbox_inches='tight')
