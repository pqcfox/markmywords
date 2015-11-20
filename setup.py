from setuptools import setup

def readme():
    with open('README.rst') as f:
          return f.read()

setup(name='markmywords',
      version='0.2',
      description='A text-generating Markov chain library',
      long_description=readme(),
      classifiers=[
            'Development Status :: 1 - Planning',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3.5',
            'Topic :: Scientific/Engineering :: Artificial Intelligence',
            'Topic :: Software Development :: Libraries',
      ],
      keywords='markov chain artificial intelligence text generation',
      url='http://github.com/useanalias/markmywords',
      author='useanalias',
      author_email='use.an.alias@gmail.com',
      license='MIT',
      test_suite='nose.collector',
      tests_require=['nose'],
      packages=['markmywords'],
      include_package_data=True,
      zip_safe=False)
