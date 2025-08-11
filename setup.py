from setuptools import setup, find_packages

setup(
  name = 'rotary-embedding-triton',
  packages = find_packages(),
  version = '0.0.1',
  license='MIT',
  description = 'Rotary Embedding - Triton',
  long_description_content_type = 'text/markdown',
  author = 'huismiling',
  author_email = 'huismiling@gmail.com',
  url = 'https://github.com/huismiling/rotary-embedding-triton',
  keywords = [
    'artificial intelligence',
    'deep learning',
    'positional embedding'    
  ],
  install_requires=[
    'einops>=0.7',
    'torch>=2.0'
  ],
  classifiers=[
    'Development Status :: 4 - Beta',
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.10',
  ],
)
