import pytest

import compressed_segmentation as cseg 
import numpy as np

def test_recover_random():

  for dtype in (np.uint32, np.uint64):
    print("dtype", dtype)
    for order in ('C', 'F'):
      print("order", order)
      labels = np.random.randint(255, size=(50, 49, 47), dtype=dtype)
      compressed = cseg.compress(labels, order=order)
      recovered = cseg.decompress(compressed, (50,49,47), dtype=dtype, order=order)

      assert type(compressed) in (bytes, str)
      assert np.all(recovered == labels)

      labels = np.random.randint(255, size=(50, 49, 47, 1), dtype=dtype)
      compressed = cseg.compress(labels, order=order)
      recovered = cseg.decompress(compressed, (50,49,47, 1), dtype=dtype, order=order)
      
      assert type(compressed) in (bytes, str)
      assert np.all(recovered == labels)

