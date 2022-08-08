#################### Maintained by Hatch ####################
# This file is auto-generated by hatch. If you'd like to customize this file
# please add your changes near the bottom marked for 'USER OVERRIDES'.
# EVERYTHING ELSE WILL BE OVERWRITTEN by hatch.
#############################################################
from io import open

from setuptools import find_packages, setup

with open('ocrpy/__init__.py', 'r') as f:
    for line in f:
        if line.startswith('__version__'):
            version = line.strip().split('=')[1].strip(' \'"')
            break
    else:
        version = '0.3.6'

with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

REQUIRES = []

kwargs = {
    'name': 'ocrpy',
    'version': version,
    'description': 'Unified interface to google vision, aws textract, azure and tesseract OCR tools.',
    'long_description': readme,
    'author': 'Maxentlabs',
    'author_email': 'info@maxentlabs.com',
    'maintainer': 'Maxentlabs',
    'maintainer_email': 'info@maxentlabs.com',
    'url': 'https://github.com/maxent-ai/ocrpy',
    'license': 'MIT/Apache-2.0',
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Intended Audience :: Education',
        'Intended Audience :: Healthcare Industry',
        'Intended Audience :: Legal Industry',
        'Intended Audience :: Telecommunications Industry',
        'Intended Audience :: Other Audience',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Financial and Insurance Industry',

    ],
    'install_requires': REQUIRES,
    'dependency_links' : ['https://github.com/facebookresearch/detectron2.git@v0.5#egg=detectron2'],
    'tests_require': ['coverage', 'pytest'],
    'packages': find_packages(exclude=('tests', 'tests.*')),
    'project_urls': {
        'Documentation': 'maxentlabs.com/ocrpy/', 
        'Source': 'https://github.com/maxent-ai/ocrpy'}
}

#################### BEGIN USER OVERRIDES ####################
# Add your customizations in this section.

###################### END USER OVERRIDES ####################

setup(**kwargs)
