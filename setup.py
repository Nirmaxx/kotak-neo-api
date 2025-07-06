from setuptools import setup, find_packages

NAME = "neo-api-client"
VERSION = "1.2.1"

# Updated and cleaned dependency versions
REQUIRES = ["bidict", "certifi", "idna", "numpy", "pyjsparser", "PyJWT", "python-dateutil", "python-dotenv", "requests", 
            "six", "urllib3", "websocket-client", "websockets", "pandas"]

setup(
    name=NAME,
    version=VERSION,
    description="Neo Trade API Client (Updated for Python 3.10+)",
    author="Neo API",
    author_email="",
    url="https://github.com/<your-username>/kotak-neo-api",  # Replace with actual URL
    keywords=["Neo-Trade API", "Kotak Neo", "Trading"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    python_requires=">=3.10",
    long_description="Neo Trade API Python SDK (forked and updated for modern compatibility)",
    long_description_content_type="text/plain"    
)
