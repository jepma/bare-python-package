"""Install packages as defined in this file into the Python environment."""
from setuptools import setup, find_packages

setup(
    name="bare-python-package",
    packages=find_packages("src"),
    package_dir={"": "src"},
    zip_safe=True,
    install_requires=["requests"],
    extras_require={"test_utils": ["black", "flake8-black", "pytest=="]},
    classifiers=["Programming Language :: Python :: 3.8"],
    entry_points={
        "console_scripts": [
            "bare-python-package=bare_python_package.main:main",
        ],
    },

)
