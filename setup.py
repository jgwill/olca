from setuptools import setup, find_packages

setup(
    name='olca',
    version = "0.3.2",
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
        'boto3>=1.26.0',                # ...updated dependency...
        'mutagen>=1.45.0',              # ...updated dependency...
        'certifi>=2022.12.7',           # ...updated dependency...
        'charset-normalizer>=2.1.1',    # ...removed duplicate...
        'idna>=3.4',
        'redis>=4.5.1',
        'requests>=2.28.1',
        'markdown>=3.4.2',
        'chardet>=5.0.0',
        'langchain>=0.0.206',
        'langchain-openai>=0.0.206',
        'langchain-community>=0.0.1',
        'langsmith>=0.0.1',
        'langchain-ollama>=0.0.1',
        'langgraph>=0.1.0',
        'llm>=0.1.0',
        'arxiv>=1.2.0',
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
