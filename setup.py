from setuptools import setup, find_packages

# Package information
with open("pyproject.toml", encoding="utf-8") as f:
    metadata = dict(
        [line.strip().split("=") for line in f if line.strip().startswith(("name", "version", "description", "author", "license"))]
    )

# Install requirements
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

# Dependencies for testing
test_requirements = [
    "pytest>=8.3.3",
    "pytest-cov>=5.0.0",
    "flake8>=7.1.1",
]

# Define the setup
setup(
    name=metadata["name"],
    version=metadata["version"],
    description=metadata["description"],
    author=metadata["author"],
    license=metadata["license"],
    packages=find_packages(exclude=["tests", "*tests*"]),
    include_package_data=True,
    install_requires=requirements,
    test_suite="tests",
    tests_require=test_requirements,
)