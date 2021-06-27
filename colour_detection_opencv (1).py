#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import cv2

#creating variables which stores the path of the image and the csv file
img_path='colouredpicture.jpg'
csv_path='colors.csv'

#reading the csv file
df=pd.read_csv('colors.csv')
df.head()

#givng headings to each coloumn
index=["Color","Color_name","Hex","R","G","B"]
df=pd.read_csv('colors.csv',names=index,header=None)
df.head()

#Reading the image with opencv
img = cv2.imread(img_path)
#resizing the image
img= cv2.resize(img,(1000,662),interpolation=cv2.INTER_AREA) 

#declaring global variables
clicked = False
r = g = b = xpos = ypos = 0

#function to calculate minimum distance from all colors and get the most matching color
def getColorName(R,G,B):
    minimum = 10000
    for i in range(len(df)):
        d = abs(R- int(df.loc[i,"R"])) + abs(G- int(df.loc[i,"G"]))+ abs(B- int(df.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = df.loc[i,'Color_name']
    return cname

#function to get x,y coordinates of image on mouse click
#basically binding this function to the mouse click
def draw_function(event,x,y,flags,para):  
    if event == cv2.EVENT_LBUTTONDBLCLK:
        global clicked,r,g,b,xpos,ypos
        clicked = True
        xpos = x
        ypos= y
        b,g,r=img[y,x]
        b=int(b)
        g=int(g)
        r=int(r)
        
#How to display an image
cv2.namedWindow('Image')
cv2.setMouseCallback('Image',draw_function)

while True:
    cv2.imshow('Image',img)
    if clicked:
        #cv2.rectangle(image, start_point, end_point, color, thickness) and -1 fills entire rectangle.
        cv2.rectangle(img,(20,20), (750,60), (b,g,r), -1)
        
        #Creating text string to display( Color name and RGB values )
        text = getColorName(r,g,b) + ' R='+ str(r) +  ' G='+ str(g) +  ' B='+ str(b)
        
        #cv2.putText(image, text, org, font, fontScale, color[, thickness[, lineType[, bottomLeftOrigin]]])
        cv2.putText(img, text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        
        #For very light colours we'll display text in black colour
        if r+g+b >=600:
            cv2.putText(img,text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
            
    if cv2.waitKey(20) & 0xFF ==27: #press escape key to exit the loop.
        break
cv2.destroyAllWindows()   


# In[ ]:




