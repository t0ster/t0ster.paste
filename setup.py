from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='t0ster.paste',
      version=version,
      description="My paster templates",
      long_description="""\
""",
      classifiers=['Topic :: Software Development'],
      keywords='paste',
      author='Roman Dolgiy',
      author_email='roman@bravetstudio.com',
      url='http://bravetstudio.com',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'PasteScript>=1.3',
          'Cheetah==2.4.1',
      ],
      entry_points="""
      [paste.paster_create_template]
      django_project = t0ster.paste.pastertemplates:DjangoProjectTemplate
      django_app = t0ster.paste.pastertemplates:DjangoAppTemplate
      """,
      )
