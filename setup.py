import setuptools

setuptools.setup(
    name="rabbitmq2solr",
    version="1.0.0",
    author="Furkan Kalkan",
    author_email="furkankalkan@mantis.com.tr",
    description="RabbitMQ to Solr Indexer",
    url="https://github.com/mantis-software-company/rabbitmq2solr",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    platforms="all",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Topic :: Internet",
        "Topic :: Software Development",
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Operating System :: MacOS",
        "Operating System :: POSIX",
        "Operating System :: Microsoft",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8"
    ],
    install_requires=['aio_pika', 'httpx', 'orjson'],
    python_requires=">3.8.*, <4",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
    scripts=['bin/rabbitmq2solr']
)