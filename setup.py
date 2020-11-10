import setuptools

setuptools.setup(
    name="roundup-csv",
    version="1.1.1",
    description="Rounds up transactions in CSV file",
    url="https://github.com/reedhaffner/CSV-RoundUps",
    packages=setuptools.find_packages(),
    author="Reed Haffner",
    author_email="reedhaffner@pm.me",
    license="GPL 3.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Topic :: Office/Business :: Financial",
        "Topic :: Office/Business :: Financial :: Spreadsheet"
    ],
    entry_points={
        "console_scripts": ["roundup = roundup.roundup:roundup"]
    }
)
