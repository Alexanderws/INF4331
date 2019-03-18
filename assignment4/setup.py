from distutils.core import setup
from Cython.Build import cythonize

setup(
	packages = ["integrator", "integrator/test"],
  	ext_modules = cythonize("cython_integrator.pyx"),
)