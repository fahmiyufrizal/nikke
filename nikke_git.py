# nikke simple launcher
# by fahmiyufrizal@2023

import os
import subprocess
from os import path
from sys import exit
import asyncio
import pathlib

# parameters
version = 'v1.0'
titlewindow = 'fahmiyufrizal@2023 [github.com/fahmiyufrizal]'
NIKKEFN = (r'NIKKE_NetCafe_Launcher.exe')
NIKKELN = (r'Launcher\nikke_launcher.exe')
NIKKELN_game = (r'Launcher')
dp0 = os.getcwd()

#the_folders
Unity = path.expandvars(r'%userprofile%\AppData\LocalLow\Unity')
data_unity = (r'_Data_\AppDataLow\Unity')

com_proximabeta = path.expandvars(r'%userprofile%\AppData\LocalLow\com_proximabeta')
data_com_proximabeta = (r'_Data_\AppDataLow\com_proximabeta')

comdotproximabeta = path.expandvars(r'%userprofile%\AppData\LocalLow\com.proximabeta')
data_comdotproximabeta = (r'_Data_\AppDataLow\com.proximabeta')

nikke_launcher = path.expandvars(r'%AppData%\nikke_launcher')
data_nikke_launcher = (r'_Data_\Roaming\nikke_launcher')

NikkeMiniloader = path.expandvars(r'%LocalAppData%\NikkeMiniloader')
data_NikkeMiniloader = (r'_Data_\LocalAppData\NikkeMiniloader')

#protection
if not path.exists (NIKKEFN):
	print(" [x] Don't change filename!")
	async def display():
		await asyncio.sleep(5)
	asyncio.run(display())
	exit()
if not path.exists (NIKKELN):
	print(" [x] Launcher\nikke_launcher.exe not found, Place inside NIKKE folder!")
	async def display():
		await asyncio.sleep(5)
	asyncio.run(display())
	exit()

#launch-in-webbrowser
print("[+] Launching NIKKE PC Launcher....")
async def display():
	await asyncio.sleep(5)
asyncio.run(display())
launchhh = open(r'launchhh.bat','w+')
launchhh.write(r'start "" "%~dp0Launcher\nikke_launcher.exe"')
launchhh.close()
subprocess.call([r'launchhh.bat'], stdout=subprocess.DEVNULL,
	stderr=subprocess.STDOUT)
os.remove('launchhh.bat')