from setuptools import setup, find_packages

setup(
    name = 'cblock',
    version = '1.0.0',
    url = 'https://github.com/TakutoYoshikai/cblock.git',
    license = 'MIT LICENSE',
    author = 'Takuto Yoshikai',
    author_email = 'takuto.yoshikai@gmail.com',
    description = 'cblock is a tool for blocking to use camera.',
    install_requires = ['setuptools', "tkinter", "opencv-python"],
    packages = find_packages(),
    entry_points={
        "console_scripts": [
            "cblock = cblock.cblock:main",
        ]
    }
)
