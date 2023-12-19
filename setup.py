from setuptools import setup, find_packages

setup(
    name="roman_converter",
    version="1.0",
    author="Geoff Clark",
    author_email="geoff@clarktribegames.com",
    description="A utility for converting between Roman numerals and integers",
    license="MIT",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=find_packages(),
    install_requires=[
        "word2number",
    ],
    python_requires=">=3.7",
    entry_points={
        "console_scripts": [
            "roman-converter=roman_converter.app:main",
        ],
    },
)
