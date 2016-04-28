# -*- coding: utf-8 -*-
"""

  This software is governed by the CeCILL-B license under French law and
  abiding by the rules of distribution of free software.  You can  use,
  modify and/ or redistribute the software under the terms of the CeCILL-B
  license as circulated by CEA, CNRS and INRIA at the following URL
  "http://www.cecill.info".

  As a counterpart to the access to the source code and  rights to copy,
  modify and redistribute granted by the license, users are provided only
  with a limited warranty  and the software's author,  the holder of the
  economic rights,  and the successive licensors  have only  limited
  liability.

  In this respect, the user's attention is drawn to the risks associated
  with loading,  using,  modifying and/or developing or reproducing the
  software by the user in light of its specific status of free software,
  that may mean  that it is complicated to manipulate,  and  that  also
  therefore means  that it is reserved for developers  and  experienced
  professionals having in-depth computer knowledge. Users are therefore
  encouraged to load and test the software's suitability as regards their
  requirements in conditions enabling the security of their systems and/or
  data to be ensured and,  more generally, to use and operate it in the
  same conditions as regards security.

  The fact that you are presently reading this means that you have had
  knowledge of the CeCILL-B license and that you accept its terms.

"""

import sys
import argparse
from os import path
import nibabel
import numpy as np

sys.path.append( path.dirname( path.dirname( path.dirname( path.abspath(__file__) ) ) ) )

from pybtk.io.itk_transforms import read_itk_transform
from pybtk.filters.imagefilters import apply_affine_itk_transform_on_image

if __name__ == '__main__':

  parser = argparse.ArgumentParser()

  parser.add_argument('-i', '--input', help='Moving image filename (required)', type=str, required = True)
  parser.add_argument('-t', '--transform', help='Transform for each input image (required)', type=str, required = True)
  parser.add_argument('-r', '--ref', help='Reference image (required)', type=str, required = True)
  parser.add_argument('-o', '--output', help='Deformed image filename (required)', type=str, required = True)
  
  
  args = parser.parse_args()
  
  movImage = nibabel.load(args.input)
  refImage = nibabel.load(args.ref)
  transform= read_itk_transform(args.transform)
  outputImage = apply_affine_itk_transform_on_image(input_image=movImage,transform=transform[0], center=transform[1], reference_image=refImage, order=3) 
  nibabel.save(outputImage,args.output)
      
  


