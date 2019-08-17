# fast.ai  deep learning part 1, 2018 version (fastai v0.7)

Lecture pace is slower & easier to understand compared to 2019 version.
Doesn't use cat breeds and dog breeds categories, but just cats vs dogs.
Gets 99.99% accuracy, but is easier to understand.

#### Tasks 

  * Setup Paperspace GPU -- 40 cents per hour.  Prebuilt fastai machine.
    * Periodically "git pull" fastai module, conda3 packages.
    
  * Try notebook 1 with my own images and labels, few hundred data.
    * Image augmentation -- zoom by small amounts, rotate by small degrees, lf-rt flip OK when it makes sense, tint & hue change by small amount.  Still a cat, but add extra data points.  
    
#### Code from Notebook 1 -- resnet34 transfer learning.  

  * To copy -- main model cell.
  
  A really cool way to visualize the filter.  Image of a horizontal sorbel filter.     
  ![sorbel kernel excerpt](sorbel_kernel_demo.png)  
  
  See website [Image Kernels by Victor Powell](http://setosa.io/ev/image-kernels/)  
   - Choose "top sobel" in the drop-down box to see the horizontal sorbel filter.  
   - A Sorbel filter increases weights on the center points.  For example, instead of the top line being (1, 1, 1) it is (1, 2, 1).

