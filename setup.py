import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='toolbox',
    version='0.0.3',
    author='Ujjawal',
    author_email='ujjawalojha@gmail.com',
    description='custom logging file',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ujjawalontop2/toolbox',
    license='MIT',
    packages=['toolbox'],
    install_requires=['Python==3.8.10'],
    zip_safe=False
)