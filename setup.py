import subprocess

def install(name):
    subprocess.call(['pip3', 'install', name])


if __name__ == '__main__':

    requiredPackages = ["itertools", "textwrap", "requests", "bs4", "reportlab", "tqdm"]

    for package in requiredPackages:
        install(package)