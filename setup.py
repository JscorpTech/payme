import setuptools

setuptools.setup(
    name="JscorpTechPayme",
    version="1.0.1",
    author="A'zamov Samandar",
    author_email="JscorpTech@gmail.com",
    description="JscorpTech Payme",
    long_description_content_type="text/markdown",
    python_requires=">=3.5",
    install_requires=['requests', 'django', 'djangorestframework'],
    url="https://github.com/JscorpTech/payme/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ]
)
