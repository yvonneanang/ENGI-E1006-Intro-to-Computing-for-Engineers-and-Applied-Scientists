#submitted by Yvonne Naa Ardua Anang 
# completed by Mikaela Zhang and Yvonne Naa Ardua Anang

# problem 1 - in class set 1

height_in_cm = int(input ("Please type height in centimeters:"))
width_in_cm = int(input ("Please type width in centimeters:"))
length_in_cm = int(input ("Please type length in centimeters:"))


area_to_be_painted_cm_squared = (2 * width_in_cm*height_in_cm) + (2 * length_in_cm * height_in_cm) + (length_in_cm * width_in_cm)
area_to_be_painted_m_squared = area_to_be_painted_cm_squared/10000
paint_in_liters = area_to_be_painted_m_squared/10 * 2.5
print ('The volume of paint needed is ',(paint_in_liters), 'liters')


