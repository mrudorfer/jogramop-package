import setuptools
from pathlib import Path

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

python_versions = '>=3.7, <3.11'  # restricted by open3d

requirements_default = [
    #'git+https://github.com/mrudorfer/burg-toolkit@dev',  # needs to be manually pre-installed
]

# add files to package data
all_files = []
data_dir = Path('jogramop/data')
for p in data_dir.rglob('*'):
    if p.is_file():
        # remove pdata/ and convert to string
        all_files.append(str(Path(*p.parts[1:])))

package_data = {
    '': all_files
}

setuptools.setup(
    name='jogramop',
    version='0.1.0',
    python_requires=python_versions,
    install_requires=requirements_default,
    packages=setuptools.find_packages(),
    zip_safe=False,
    package_data=package_data,
    url='https://github.com/mrudorfer/jogramop-package',
    license='',
    author='Martin Rudorfer, Jiri Hartvich, Vojtech Vonasek',
    author_email='m.rudorfer@aston.ac.uk',
    description='scenarios for joint grasp and motion planning in confined spaces',
    long_description=long_description
)
