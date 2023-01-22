from setuptools import find_packages, setup


if __name__ == "__main__":
    setup(
        name="library_python",
        version="0.0.1",
        description="",
        url="https://github.com/oSoloTurk/library-python",
        long_description_content_type="text/markdown",
        author="oSoloTurk",
        packages=find_packages(exclude=["tests", ".github"]),
        install_requires=[],
    )
