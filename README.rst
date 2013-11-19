Inspired by http://www.datagenetics.com/blog/november32013/index.html

Takes an input image, flips a coin for each pixel, and "encrypts" to one of two
output images.  Image can only be viewed when output images are lined up.
Ideally, you need all the component images (2 in this case) to recover the
original.  However, if your random number generator is poor, I suspect this is
one potential attack vector.  

Works best on high-contrast images.  Small details will probably be lost.  For
example, Lenna didn't turn out so great.

Usage:
    ``python generate.py mysourceimage.jpg``
        - Generates ``out1.jpg`` and ``out2.jpg``
    ``python show.py out1.jpg out2.jpg``
        - Shows the two images merged together

Requirements:
    pillow (or PIL)
