from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('class8.py', base=base, targetName = 'EatChicken')
]

setup(name='crossin_pygame',
      version = '1.0',
      description = 'by Tom 2018.01.25',
      options = dict(build_exe = buildOptions),
      executables = executables)
