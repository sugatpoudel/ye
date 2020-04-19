import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="yenerate-groupbool",
    version="0.0.1",
    author="groupbool",
    description="generate custom ye album art",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/groupbool/yenerate",
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
)
