from setuptools import setup, find_packages

readme = open('README.txt', 'rb').read()

setup(name          = 'OWSLib.sos',
      version       = '0.4',
      description   = 'OGC Web Service utility library for Sensor Observation Service (SOS)',
      long_description = readme,
      license       = 'BSD',
      keywords      = 'gis ogc ows wfs wms sos csw capabilities metadata',
      author        = 'Sean Gillies',
      author_email  = 'sgillies@frii.com',
      maintainer        = 'Sean Gillies',
      maintainer_email  = 'sgillies@frii.com',
      url           = 'http://trac.gispython.org/lab/wiki/OwsLib',
      namespace_packages  =  ['owslib'],
      install_requires =      ['OWSLib.common'],

      packages      = find_packages(),
      test_suite    = 'tests.test_suite',
      classifiers   = [
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering :: GIS',
        ],
)

