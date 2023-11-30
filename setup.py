import setuptools
import versioneer

with open("README.rst", "r") as fh:
    long_description = fh.read()
with open("requirements.txt", "r") as fh:
    requirements = [line.strip() for line in fh]

setuptools.setup(
    name="morrisseau-cleaner",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Ali Shajari",
    author_email="ali0shajari@gmail.com",
    description="A Python library to clean data for Morrisseau Project",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    packages=setuptools.find_packages(),
    setup_requires=[
        'cython==3.0.6',
    ],
    install_requires=[
        'attr===0.3.2',
        'brotli===1.1.0',
        'brotlicffi===1.1.0.0',
        'ConfigParser===6.0.0'
        'contextlib2===21.6.0'
        'cryptography===41.0.7'
        'cx_Freeze==6.15.11'
        'docutils===0.20.1'
        'HTMLParser===0.0.2'
        'importlib_metadata==6.8.0'
        'ipython==8.18.1'
        'ipywidgets==8.1.1'
        'Jinja2===3.1.2'
        'jnius==1.1.0'
        'keyring==24.3.0'
        'lockfile==0.12.2'
        'mock===5.1.0'
        'Pillow==10.0.1'
        'Pillow==10.1.0'
        'protobuf==4.21.12'
        'py2exe==0.13.0.1'
        'pyfiglet==1.0.2'
        'pyOpenSSL==23.3.0'
        'railroad==0.5.0'
        'setuptools==68.2.2'
        'simplejson==3.19.2'
        'Sphinx===7.2.6'
        'termcolor==2.3.0'
        'thread==0.1.2'
        'tornado===6.4'
        'truststore==0.8.0'
        'urllib3_secure_extra==0.1.0'
        'xmlrpclib==1.0.1'
        'zstandard==0.22.0'
    ],
    entry_points={
        'console_scripts': [
            'morrisseau-cleaner = morrisseau_cleaner.morrisseau_cleaner:main',
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=requirements,
)
