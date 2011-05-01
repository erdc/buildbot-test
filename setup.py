from distutils.core import setup, Extension

## \file setup.py setup.py
#  \brief The python script for building proteus
#

###to turn on debugging in c++
##\todo Finishing cleaning up setup.py/setup.cfg, config.py...
from distutils import sysconfig
cv = sysconfig.get_config_vars()
cv["OPT"] = cv["OPT"].replace("-DNDEBUG","-DDEBUG")
cv["OPT"] = cv["OPT"].replace("-O3","-g")
cv["CFLAGS"] = cv["CFLAGS"].replace("-DNDEBUG","-DDEBUG")
cv["CFLAGS"] = cv["CFLAGS"].replace("-O3","-g")

setup(name='proteus-dummy',
      version='1.0.0',
      description='Python tools for multiphysics modeling',
      author='Chris Kees',
      author_email='christopher.e.kees@usace.army.mil',
      url='https://adh.usace.army.mil/proteus',
      packages = ['proteus-dummy'],
      ext_package='proteus-dummy',
      ext_modules=[Extension('cshockCapturing',
                             ['proteus-dummy/cshockCapturingModule.c','proteus-dummy/shockCapturing.c'],
                             include_dirs=[numpy.get_include(),'include'],
                             libraries=['m'],
                             extra_compile_args=PROTEUS_EXTRA_COMPILE_ARGS,
                             extra_link_args=PROTEUS_EXTRA_LINK_ARGS),
                   ],
      )
