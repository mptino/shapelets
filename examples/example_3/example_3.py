########################################################################################################################
# Copyright 2023 the authors (see AUTHORS file for full list).                                                         #
#                                                                                                                      #
# This file is part of shapelets.                                                                                      #
#                                                                                                                      #
# Shapelets is free software: you can redistribute it and/or modify it under the terms of the GNU Lesser General       #
# Public License as published by the Free Software Foundation, either version 2.1 of the License, or (at your option)  #
# any later version.                                                                                                   #
#                                                                                                                      #
# Shapelets is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied      #
# warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more  #
# details.                                                                                                             #
#                                                                                                                      #
# You should have received a copy of the GNU Lesser General Public License along with shapelets. If not, see           #
# <https://www.gnu.org/licenses/>.                                                                                     #
########################################################################################################################

## Section 1: importing modules
import os 
from pathlib import Path

from shapelets.self_assembly import (
    read_image,
    orientation,
    process_output
) 

## Section 2: parameters
image_name = "sqrAFM2.png"
pattern_order = "square"

## Section 3: code

# 3.1: image and output directory handling
image_path = os.path.join(Path(__file__).parents[0], 'images')
image = read_image(image_name = image_name, image_path = image_path, do_rescale=False)
save_path = os.path.join(Path(__file__).parents[0], 'output')
if not os.path.exists(save_path): 
    os.mkdir(save_path)

# 3.2: compute the local pattern orientation
mask, dilate, blended, maxval = orientation(image = image, pattern_order = pattern_order)

# 3.3: processing and saving the results to the **output/** directory 
process_output(image = image, image_name = image_name, save_path = save_path, output_from = 'orientation', mask = mask, dilate = dilate, orientation = blended, maxval = maxval)
