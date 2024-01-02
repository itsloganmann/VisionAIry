from setuptools import setup, find_packages

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt', encoding='utf-8') as f:
    requirements = f.read().splitlines()

setup(
    name='webcamgpt',
    version='0.1.0',
    author='Logan Mann',
    author_email='loganmann0324@gmail.com',
    description='WebcamGPT - chat with video stream',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/roboflow/webcamgpt',
    packages=['webcamgpt'],
    include_package_data=False,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.8,<3.12.0',
    install_requires=requirements,
)
