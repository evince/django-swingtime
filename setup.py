from setuptools import setup, find_packages

setup(
   name = "django-swingtime",
   version = "0.1-dev",
   description = "planning app for django.",
   author = 'Lacombe Antonin',
   packages = find_packages('src'),
   package_dir = {'': 'src'},
   install_requires = [
      'setuptools',
   ],
)