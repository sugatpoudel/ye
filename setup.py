import setuptools

with open("README.md", "r") as f:
    long_description = f.read()

setuptools.setup(
    name="yenerate",
    version="0.1.0",
    author="groupbool",
    description="generate custom ye album art",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/groupbool/yenerate",
    packages=setuptools.find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "pillow>=7.1.1"
    ],
    entry_points={
        "console_scripts": ["yenerate = yenerate.yenerate:main"],
    },
    package_data={
        "yenerate": [
            "data/ye_album_art.jpg",
            "data/ye_font_num_regular.ttf",
            "data/ye_font_regular.ttf",
        ],
    },
)
