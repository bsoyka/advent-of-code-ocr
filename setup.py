from pathlib import Path

from setuptools import setup

here = Path(__file__).parent.resolve()

readme = (here / "README.md").read_text()

about = {}
exec((here / "advent_of_code_ocr" / "__version__.py").read_text(), about)

setup(
    name=about["__title__"],
    description=about["__description__"],
    version=about["__version__"],
    long_description=readme,
    long_description_content_type="text/markdown",
    author=about["__author__"],
    author_email=about["__author_email__"],
    license=about["__license__"],
    packages=["advent_of_code_ocr"],
    install_requires=["numpy==1.19.4"],
    url="https://github.com/bsoyka/advent-of-code-ocr",
    project_urls={
        "Bug Tracker": "https://github.com/bsoyka/advent-of-code-ocr/issues",
        "Source Code": "https://github.com/bsoyka/advent-of-code-ocr",
    },
)
