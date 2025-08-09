from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="DarkDrop",
    version="1.0.0",
    author="Karan",
    author_email="your-email@example.com",  # Add your email
    description="A secure file transfer tool with AES-256 encryption",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/karan2527/DarkDrop",
    py_modules=["darkdrop"],  # Since you have a single Python file
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Topic :: Security :: Cryptography",
        "Topic :: System :: Networking",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    keywords="encryption, file-transfer, security, aes-256, cybersecurity",
)
