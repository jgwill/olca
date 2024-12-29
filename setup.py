from setuptools import setup, find_packages

setup(
    name='olca',
    version = "0.2.60",
    author='Jean GUillaume ISabelle',
    author_email='jgi@jgwill.com',
    description='A Python package for experimenting with Langchain agent and interactivity in Terminal modalities.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/jgwill/olca',
    packages=find_packages(
        include=["olca", "test-*.py"], exclude=["test*log", "*test*csv", "*test*png"]
    ),
    #package_dir={'': 'coaiapy'},
    install_requires=[
        'boto3',
        'mutagen',
        'certifi',
        'charset-normalizer',
        'idna',
        'redis',
        'requests',
        'markdown',
        'chardet',
        'charset-normalizer',
        'langchain',
        'langchain-openai',
        'langchain-community',
        'langsmith',
        'langchain-ollama',
        'langgraph',
        'llm',
        'langgraph'
    ],
    entry_points={
        'console_scripts': [
            'olca2=olca.olcacli:main',
            'fusewill=olca.fusewill_cli:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
