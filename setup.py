''' setup module
'''

from distutils.core import setup

# TEMPLATE
setup(
    name='python_template',
    version='0.0',
    description='',
    long_description=open('README.rst').read(),
    author='Christine Madden',
    license=open('LICENSE').read(),
    author_email='',
    packages=['project_name'],
    install_requires=[
        # list other required packages
        "pylint",
        "sphinx",
        "sphinx-readable-theme",
        "sphinxcontrib-napoleon",
        "unittest",
        "black",
        "flake8"
    ],
    entry_points={
        'console_scripts':
        [
            'project_name = project_name.__main__:main',
        ]
    }
)
