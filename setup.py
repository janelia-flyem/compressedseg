import os
import setuptools

# NOTE: Run if _compressed_segmentation.cpp does not exist:
# cython -3 --fast-fail -v --cplus -I./include src/compressed_segmentation.pyx

import numpy as np

join = os.path.join

setuptools.setup(
  setup_requires=['numpy', 'pbr'],
  ext_modules=[
    setuptools.Extension(
        'compressed_segmentation',
        optional=True,
        sources=[ join('src', x) for x in ( 
            'compress_segmentation.cc', 'decompress_segmentation.cc',
            'compressed_segmentation.cpp'
        )],
        language='c++',
        include_dirs=[ 'include', np.get_include() ],
        extra_compile_args=[
          '-O3', '-std=c++11'
        ],
    ),
  ],
  pbr=True,
)


