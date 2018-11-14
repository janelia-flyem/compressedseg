# Compress Seg [![Picture](https://raw.github.com/janelia-flyem/janelia-flyem.github.com/master/images/HHMI_Janelia_Color_Alternate_180x40.png)](http://www.janelia.org)
## Library for compressing and decompressing image segmentation (adapted from [neuroglancer](https://github.com/google/neuroglancer))

This library contains routined to decompress and compress segmentation and to manipulate compressed segmentation data defined by the [neuroglancer project](https://github.com/google/neuroglancer/blob/master/src/neuroglancer/sliceview/compressed_segmentation/README.md).

### Features

* Compression and decompression
* (TBD) Interface to relabel and manipulate segmentation from the compressed data
* C++, Python, and Go interface

### C++ Compilation

Compiling as a shared library. Feel free to subsititute e.g. clang for the C++ compiler.

```bash
g++ -std=c++11 -O3 -fPIC -shared -I./include src/compress_segmentation.cc src/decompress_segmentation.cc -o compress_segmentation.so
```

### Python Installation

`pip` Binary Installation  

```bash
$ pip install compressed-segmentation

$ python
>>> import compressed_segmentation as cseg
>>> help(cseg)
```

If there are pre-built binaries available this should just work. 

`pip` Source Installation 

If you need to build from source, you will need to have a C++ compiler installed and do the following:

```bash
$ sudo apt-get install g++ python3-dev 
$ pip install numpy
$ pip install compressed-segmentation

$ python
>>> import compressed_segmentation as cseg
>>> help(cseg)
```

Direct Installation  

_Requires a C++ compiler such as g++ or clang._

Works with both Python 2 and 3. Encodes from / decodes to 3D or 4D numpy ndarrays.  

```bash
$ sudo apt-get install g++ python3-dev 
$ pip install -r requirements.txt
$ python setup.py install

$ python
>>> import compressed_segmentation as cseg
>>> help(cseg)
```

### License

Please see the licenses in this repo.

