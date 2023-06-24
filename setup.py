import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nft_market",
    version="1.39",
    author="ukaznil",
    author_email="ukaznil@gmail.com",
    description="NFT market is in your hands.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ukaznil/nft-market",
    project_urls={
        "Bug Tracker": "https://github.com/ukaznil/nft-market/issues",
        },
    packages=setuptools.find_packages(),
    install_requires=[
        "selenium",
        "webdriver-manager",
        ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        ],
    python_requires=">=3.6",
    )
