from setuptools import setup, find_packages

setup(
    name="mini_blog",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.69",
        "httpx>=0.28",
        "pytest>=7.0",
        "SQLAlchemy>=2.0",
        "asyncpg>=0.26"
    ],
    python_requires=">=3.10",
)
