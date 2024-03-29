
import setuptools
import io

with io.open('README.md', encoding='utf8') as fp:
  long_description = fp.read()

setuptools.setup(
  name = 'nr.cli',
  version = '1.0.2',
  author = 'Niklas Rosenstein',
  author_email = 'rosensteinniklas@gmail.com',
  description = 'The command-line interface for tools in the "nr" libraries.',
  long_description = long_description,
  long_description_content_type = 'text/markdown',
  url = 'https://github.com/NiklasRosenstein/python-nr/tree/master/nr.cli',
  license = 'MIT',
  packages = setuptools.find_packages('src'),
  package_dir = {'': 'src'},
  namespace_packages = ['nr'],
  entry_points = {
    'console_scripts': [
      'nr = nr.cli:main'
    ]
  }
)
