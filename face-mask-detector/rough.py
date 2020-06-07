
import photohash
im1='no_mask_indiv/person2.jpg'
im2='no_mask_indiv/person3.jpg'
similar = photohash.is_look_alike(im1,im2)
# Opens a image in RGB mode

print (similar)
distance = photohash.distance(im1,im2)
# Setting the points for cropped image 

print (distance)



