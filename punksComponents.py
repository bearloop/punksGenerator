from PIL import Image, ImageDraw, ImageFont

class newPunk:
    
    # -------------------------------------------------
    def __init__(self, width_size=420, height_size=420, base=0, head=320-60, start=290, sqs=15, bcg_color='white'):
        
        # Image dimensions
        self.width_size = width_size         
        self.height_size = height_size

        # Controllers
        self.base=base
        self.head=head
        self.start=start
        self.sqs = sqs
        self.bcg_color = bcg_color

        self.canvas = Image.new('RGB', (width_size, height_size), self.bcg_color)
        self.img_draw = ImageDraw.Draw(self.canvas)
    
    # -------------------------------------------------
    # ------- Image background called rect(angular)
    def rect(self, left, top, right, bottom, color):
        '''Distance from left, top, right, bottom.'''
        return self.img_draw.rectangle(
                        [
                         (left, self.height_size-bottom),
                         (self.width_size-right, top)
                        ], outline=None, fill=color)
    
    # -------------------------------------------------
    # ------- Add a square on canvas
    def square(self, left, bottom, color, square_size=15):
        ''''''
        return self.rect(left=left,
                    top=self.height_size-bottom,
                    right=self.width_size-left-square_size,
                    bottom=bottom+square_size, color=color)
    # -------------------------------------------------
    # ------- Show results
    def show_results(self,title_name='bla'):
        self.canvas.show(title = title_name)
    
    # -------------------------------------------------
    # ------- Save results
    def save_results(self,save_to_path):
        # Suggested: path+'/assets/'+'0x'+str(index)+'.png'
        self.canvas.save(save_to_path,format='PNG')

##############################################################################################################

class compNose(newPunk):
    
    # -------------------------------------------------
    def __init__(self):
        newPunk.__init__(self,start,sqs)
    
    # -------------------------------------------------
    # ------- Type A:
    def typeA(self, sq_size, col):
        # Nose
        for i in range(self.start-self.sqs*7,self.start-self.sqs*6):
            self.square(i,self.head-self.sqs*9,  col, sq_size)
            
    # -------------------------------------------------
    # ------- Type B:
    def typeB(self, sq_size, col):
        # Nose
        for i in range(self.start-self.sqs*11,self.start-self.sqs*10):
            self.square(i,self.head-self.sqs*9,  col, sq_size)
    # -------------------------------------------------


##############################################################################################################

class compMouth(newPunk):
    
    # -------------------------------------------------
    def __init__(self):
        newPunk.__init__(self,start,sqs)
    
    # -------------------------------------------------
    # ------- Type A:
    def typeA(self, sq_size, col):
        # Mouth
        for i in range(self.start-self.sqs*7,self.start-self.sqs*5):
            self.square(i,self.head-self.sqs*12, col, sq_size)
            
    # -------------------------------------------------
    # ------- Type B:
    def typeB(self, sq_size, col):
        # Mouth
        for i in range(self.start-self.sqs*11,self.start-self.sqs*9):
            self.square(i,self.head-self.sqs*12, col, sq_size)
    # -------------------------------------------------

##############################################################################################################

class compBeard(newPunk):
    
    # -------------------------------------------------
    def __init__(self):
        newPunk.__init__(self,start,sqs)
        
    # -------------------------------------------------
    # ------- Type A:
    def typeA(self,sq_size,col):
        
        # Facial hair
        for i in range(self.start-self.sqs*8,self.start-self.sqs*1,self.sqs*2):
            self.square(i,self.head-self.sqs*10-1, col, sq_size)
            
        for i in range(self.start-self.sqs*7,self.start,self.sqs*2):
            self.square(i,self.head-self.sqs*10.5-1, col, sq_size)
            
        for i in range(self.start-self.sqs*8,self.start-self.sqs*6,self.sqs*2):
            self.square(i,self.head-self.sqs*11.7-1,col, sq_size)
            
        for i in range(self.start-self.sqs*3,self.start,self.sqs*2):
            self.square(i,self.head-self.sqs*11.7-1,col, sq_size)
            
        self.square(self.start-self.sqs*2,self.head-self.sqs*11.2-1,col,  sq_size)
        
        for i in range(self.start-self.sqs*8,self.start-self.sqs*1,self.sqs*2):
            self.square(i,self.head-self.sqs*12.7-1, col, sq_size)
            
        for i in range(self.start-self.sqs*7,self.start,self.sqs*2):
            self.square(i,self.head-self.sqs*13.2-1, col, sq_size)
    
            
    # -------------------------------------------------
    # ------- Type B:
    def typeB(self, sq_size, col):
        pass
    # -------------------------------------------------
    # ------- Type C:
    def typeC(self, sq_size, col):
        pass

##############################################################################################################

class compGlasses(newPunk):
    
    # -------------------------------------------------
    def __init__(self):
        newPunk.__init__(self,start,sqs)
        
    # -------------------------------------------------
    # ------- Type A:
    def typeA(self,sq_size,col):
        
        # Glasses
        for i in range(self.start-self.sqs*11,self.start+self.sqs+1):
            self.square(i,self.head-self.sqs*5, col, sq_size)
        
        for i in range(self.start-self.sqs*11,self.start-self.sqs*8+1):
            self.square(i,self.head-self.sqs*6-1, col, sq_size)
            
        for i in range(self.start-self.sqs*10,self.start-self.sqs*9+1):
            self.square(i,self.head-self.sqs*7-2, col, sq_size)
            
        for i in range(self.start-self.sqs*5,self.start-self.sqs*2+1):
            self.square(i,self.head-self.sqs*6-1, col, sq_size)
            
        for i in range(self.start-self.sqs*4,self.start-self.sqs*3+1):
            self.square(i,self.head-self.sqs*7-2, col, sq_size)
            
    # -------------------------------------------------
    # ------- Type B:
    def typeB(self, sq_size, col):
        pass

##############################################################################################################

class compHat(newPunk):
    
    # -------------------------------------------------
    def __init__(self):
        newPunk.__init__(self,start,sqs)
        
    # -------------------------------------------------
    # ------- Type A:
    def typeA(self, sq_size, col_main, col_detail, col_outline):
        
        # Top two lines
        for i in range(self.start-self.sqs*8+1, self.start-self.sqs*2):
            self.square(i,self.head+self.sqs*2-1, col_outline, sq_size)
            
        for i in range(self.start-self.sqs*8, self.start-self.sqs*2+1):
            self.square(i,self.head+self.sqs-1,  col_main,   sq_size)

        # Right side and individual dots
        self.square(self.start-self.sqs*2, self.head+self.sqs-1,    col_detail, sq_size)
        self.square(self.start-self.sqs*1, self.head+self.sqs-1,    col_outline, sq_size)
        self.square(self.start-self.sqs*9, self.head+self.sqs-1,    col_outline, sq_size)
        self.square(self.start-self.sqs*10, self.head-1,       col_outline, sq_size)
        self.square(self.start-self.sqs*12, self.head-self.sqs*2-2, col_outline, sq_size)
        self.square(self.start, self.head-1,                col_outline, sq_size)
        self.square(self.start, self.head-self.sqs,            col_outline, sq_size)
        self.square(self.start, self.head-self.sqs*2,          col_outline, sq_size)

        for i in range(self.start-self.sqs*9, self.start-self.sqs+1):
            self.square(i, self.head-1, col_main, sq_size)

        self.square(self.start-self.sqs*1, self.head-1,col_detail,sq_size)

        # Bottom side
        for i in range(self.start-self.sqs*10, self.start-self.sqs+1):
            self.square(i,self.head-self.sqs-1,  col_main,    sq_size)
            
        for i in range(self.start-self.sqs*9,  self.start-self.sqs+1):
            self.square(i,self.head-self.sqs*2-1,col_main,    sq_size)
            
        for i in range(self.start-self.sqs*11, self.start-self.sqs*4+1):
            self.square(i,self.head-self.sqs-1,  col_main,    sq_size)
            
        for i in range(self.start-self.sqs*11, self.start-self.sqs*4+1):
            self.square(i,self.head-self.sqs*2-1, col_detail,    sq_size)

        for i in range(self.start-self.sqs*11, self.start-self.sqs*3+1):
            self.square(i,self.head-self.sqs-1,   col_outline, sq_size)
            
        for i in range(self.start-self.sqs*12, self.start+1):
            self.square(i,self.head-self.sqs*3-1, col_outline, sq_size)
            
        self.square(self.start-self.sqs*3, self.head-self.sqs*2-2, col_outline, sq_size)
        
            
    # -------------------------------------------------
    # ------- Type B:
    def typeB(self, sq_size, col_main, col_detail, col_detail_2):

            for i in range(self.start-self.sqs*12+1, self.start+self.sqs*2): self.square(i,self.head-self.sqs*2-1,col_main, sq_size)
            for i in range(self.start-self.sqs*13+1, self.start+self.sqs*3): self.square(i,self.head-self.sqs*1-1,col_main, sq_size)
            
            for i in range(self.start-self.sqs*10+1, self.start+self.sqs*0): self.square(i,self.head-1,col_main, sq_size)
            for i in range(self.start-self.sqs*10+1, self.start+self.sqs*0): self.square(i,self.head+self.sqs*1-1,col_main, sq_size)
            for i in range(self.start-self.sqs*10+1, self.start+self.sqs*0): self.square(i,self.head+self.sqs*2-1,col_main, sq_size)
            for i in range(self.start-self.sqs*9+1, self.start-self.sqs*1): self.square(i,self.head+self.sqs*3-1,col_main, sq_size)
            for i in range(self.start-self.sqs*8+1, self.start-self.sqs*2): self.square(i,self.head+self.sqs*4-1,col_main, sq_size)
            
            
            for i in range(self.start-self.sqs*8+1, self.start-self.sqs*1): self.square(i,self.head-self.sqs*1-2,col_detail, sq_size)
            for i in range(self.start-self.sqs*9+1, self.start-self.sqs*1): self.square(i,self.head+self.sqs*0-2,col_detail, sq_size)
            for i in range(self.start-self.sqs*9+1, self.start-self.sqs*2): self.square(i,self.head+self.sqs*1-2,col_detail, sq_size)
            for i in range(self.start-self.sqs*8+1, self.start-self.sqs*3): self.square(i,self.head+self.sqs*2-2,col_detail, sq_size)
            for i in range(self.start-self.sqs*7+1, self.start-self.sqs*4): self.square(i,self.head+self.sqs*3-2,col_detail, sq_size)
                
            for i in range(self.start-self.sqs*8+1, self.start-self.sqs*3): self.square(i,self.head-self.sqs*1-2,col_detail_2, sq_size)
            for i in range(self.start-self.sqs*9+1, self.start-self.sqs*4): self.square(i,self.head+self.sqs*0-2,col_detail_2, sq_size)
            for i in range(self.start-self.sqs*9+1, self.start-self.sqs*5): self.square(i,self.head+self.sqs*1-2,col_detail_2, sq_size)
            for i in range(self.start-self.sqs*8+1, self.start-self.sqs*6): self.square(i,self.head+self.sqs*2-2,col_detail_2, sq_size)
                
            self.square(self.start-self.sqs*7+1,self.head-self.sqs*1-2,col_detail, sq_size)
            self.square(self.start-self.sqs*8+1,self.head-self.sqs*1-2,col_detail, sq_size)
            self.square(self.start-self.sqs*8+1,self.head-self.sqs*0-2,col_detail, sq_size)
            self.square(self.start-self.sqs*9+1,self.head-self.sqs*0-2,col_detail, sq_size)
            self.square(self.start-self.sqs*9+1,self.head+self.sqs*1-2,col_detail, sq_size)
        


##############################################################################################################

class compFace(newPunk):
    
    # -------------------------------------------------
    def __init__(self):
        newPunk.__init__(self,start,sqs)
        
    # -------------------------------------------------
    # ------- Type A:
    def typeA(self, sq_size, col_outline, col_skin):
        # Left side
        for i in range(self.base+self.sqs*4,self.head-self.sqs*3):
            self.square(self.start-self.sqs*10,i, col_outline, sq_size)

        for i in range(self.base,self.base+self.sqs*2):
            self.square(self.start-self.sqs*4,i, col_outline, sq_size)

        self.square(self.start-self.sqs*9,self.base+self.sqs*3, col_outline, sq_size)

        # Right side
        for i in range(self.base, self.head-self.sqs*3):
            self.square(self.start, i, col_outline, sq_size)

        for i in range(self.head-self.sqs*8, self.head-self.sqs*5):
            self.square(self.start+self.sqs, i,  col_outline, sq_size)

        # Top side
        for i in range(self.start-self.sqs*10, self.start+1):
            self.square(i,self.head-self.sqs*3-1, col_outline, sq_size)

        # Bottom side
        for i in range(self.start-self.sqs*8, self.start-self.sqs*5):
            self.square(i, self.base+self.sqs*2-1, col_outline, sq_size)

        # Skin
        for i in range(self.head-60-self.sqs*3,self.head-60-self.sqs):
            self.square(self.start,i,      col_skin, sq_size)
            
        for i in range(self.base,self.head-self.sqs*4):
            self.square(self.start-self.sqs,i, col_skin, sq_size)
            
        for i in range(self.base,self.head-self.sqs*4):
            self.square(self.start-self.sqs*2,i, col_skin, sq_size)
            
        for i in range(self.base,self.head-self.sqs*4):
            self.square(self.start-self.sqs*3,i, col_skin, sq_size)
            
        for i in range(self.base+self.sqs*3,self.head-self.sqs*4):
            self.square(self.start-self.sqs*4,i, col_skin, sq_size)
            
        for i in range(self.base+self.sqs*3,self.head-self.sqs*4):
            self.square(self.start-self.sqs*5,i,    col_skin, sq_size)
            
        for i in range(self.base+self.sqs*3,self.head-self.sqs*4):
            self.square(self.start-self.sqs*6,i,    col_skin, sq_size)
            
        for i in range(self.base+self.sqs*3,self.head-self.sqs*4):
            self.square(self.start-self.sqs*7,i,    col_skin, sq_size)
            
        for i in range(self.base+self.sqs*3,self.head-self.sqs*4):
            self.square(self.start-self.sqs*8,i,    col_skin, sq_size)
            
        for i in range(self.base+self.sqs*4,self.head-self.sqs*4):
            self.square(self.start-self.sqs*9,i,    col_skin, sq_size)
            
    # -------------------------------------------------
    # ------- Type B:
    def typeB(self, sq_size, col):
        pass


##############################################################################################################


# # # Controllers
# # base=0
# # head=320-60
# # start=280
# # sqs = 15
# # width_size = 420
# # height_size = 420

# class newPunk:

#     def __init__(self, width_size, height_size, base, head, start, sqs):
        
#         # Image dimensions
#         self.width_size = width_size         
#         self.height_size = height_size

#         # Controllers
#         self.base=base
#         self.head=head
#         self.start=start
#         self.sqs = sqs

#     canvas = Image.new('RGB', (width_size, height_size), 'white')
#     img_draw = ImageDraw.Draw(canvas)

#     def rect(left, top, right, bottom, color):
#         '''Distance from left, top, right, bottom.'''
#         return img_draw.rectangle(
#                         [
#                             (left, height_size-bottom),
#                             (width_size-right, top)
#                         ], outline=None, fill=color)

#     def square(left, bottom, color, square_size=15):
#         ''''''
#         return rect(left=left,
#                     top=height_size-bottom,
#                     right=width_size-left-square_size,
#                     bottom=bottom+square_size, color=color)

#     def facial_hair(sq_size,col):
        
#         # Facial hair
#         for i in range(start-sqs*8,start-sqs*1,sqs*2):square(i,head-sqs*10-1,col,square_size=sq_size)
#         for i in range(start-sqs*7,start,sqs*2):square(i,head-sqs*10.5-1,col,square_size=sq_size)
#         for i in range(start-sqs*8,start-sqs*6,sqs*2):square(i,head-sqs*11.7-1,col,square_size=sq_size)
#         for i in range(start-sqs*3,start,sqs*2):square(i,head-sqs*11.7-1,col,square_size=sq_size)
#         square(start-sqs*2,head-sqs*11.2-1,col,square_size=sq_size)
#         for i in range(start-sqs*8,start-sqs*1,sqs*2):square(i,head-sqs*12.7-1,col,square_size=sq_size)
#         for i in range(start-sqs*7,start,sqs*2):square(i,head-sqs*13.2-1,col,square_size=sq_size)

#     def nose_mouth(sq_size,col):
        
#         # Nose and mouth
#         for i in range(start-sqs*7,start-sqs*6): square(i,head-sqs-sqs*8,  col, square_size=sq_size)
#         for i in range(start-sqs*7,start-sqs*5): square(i,head-sqs-sqs*11, col, square_size=sq_size)

#     def glasses_v_type(sq_size,col):
#         # Glasses
#         for i in range(start-sqs*11,start+sqs+1): square(i,head-sqs*5,col,square_size=sq_size)
#         for i in range(start-sqs*11,start-sqs*8+1): square(i,head-sqs*6-1,col,square_size=sq_size)
#         for i in range(start-sqs*10,start-sqs*9+1): square(i,head-sqs*7-2,col,square_size=sq_size)
#         for i in range(start-sqs*5,start-sqs*2+1): square(i,head-sqs*6-1,col,square_size=sq_size)
#         for i in range(start-sqs*4,start-sqs*3+1): square(i,head-sqs*7-2,col,square_size=sq_size)
            
#     def simple_hat(sq_size, col_main, col_detail, col_outline):
#         # Simple Hat
#         # Top two lines
#         for i in range(start-sqs*8+1, start-sqs*2): square(i,head+sqs*2-1,col_outline,square_size=sq_size)
#         for i in range(start-sqs*8, start-sqs*2+1): square(i,head+sqs-1,  col_main,   square_size=sq_size)
        
#         # Right side and individual dots
#         square(start-sqs*2, head+sqs-1,    col_detail, square_size=sq_size)
#         square(start-sqs*1, head+sqs-1,    col_outline, square_size=sq_size)
#         square(start-sqs*9, head+sqs-1,    col_outline, square_size=sq_size)
#         square(start-sqs*10, head-1,       col_outline, square_size=sq_size)
#         square(start-sqs*12, head-sqs*2-2, col_outline, square_size=sq_size)
#         square(start, head-1,                col_outline, square_size=sq_size)
#         square(start, head-sqs,            col_outline, square_size=sq_size)
#         square(start, head-sqs*2,          col_outline, square_size=sq_size)

#         for i in range(start-sqs*9, start-sqs+1):   square(i, head-1, col_main, square_size=sq_size)
        
#         square(start-sqs*1, head-1,col_detail,square_size=sq_size)
        
#         # Bottom side
#         for i in range(start-sqs*10, start-sqs+1):   square(i,head-sqs-1,  col_main,    square_size=sq_size)
#         for i in range(start-sqs*9,  start-sqs+1):   square(i,head-sqs*2-1,col_main,    square_size=sq_size)
#         for i in range(start-sqs*11, start-sqs*4+1): square(i,head-sqs-1,  col_main,    square_size=sq_size)
#         for i in range(start-sqs*11, start-sqs*4+1): square(i,head-sqs*2-1,col_detail,    square_size=sq_size)
        
#         for i in range(start-sqs*11, start-sqs*3+1): square(i,head-sqs-1,   col_outline, square_size=sq_size)
#         for i in range(start-sqs*12, start+1):       square(i,head-sqs*3-1, col_outline, square_size=sq_size)
#         square(start-sqs*3, head-sqs*2-2, col_outline, square_size=sq_size)

#     def face_and_neck(sq_size, col_outline, col_skin):

#         # Left side
#         for i in range(base+sqs*4,head-sqs*3): square(start-sqs*10,i,        col_outline, square_size=sq_size)
#         for i in range(base,base+sqs*2): square(start-sqs*4,i,        col_outline, square_size=sq_size)
#         square(start-sqs*9,base+sqs*3,col_outline,square_size=sq_size)
        
#         # Right side
#         for i in range(base, head-sqs*3): square(start, i,        col_outline, square_size=sq_size)
#         for i in range(head-sqs*8, head-sqs*5): square(start+sqs, i,  col_outline, square_size=sq_size)
        
#         # Top side
#         for i in range(start-sqs*10, start+1):       square(i,head-sqs*3-1, col_outline, square_size=sq_size)
        
#         # Bottom side
#         for i in range(start-sqs*8, start-sqs*5):    square(i, base+sqs*2-1, col_outline, square_size=sq_size)

#         # Skin
#         for i in range(head-60-sqs*3,head-60-sqs): square(start,i,      col_skin, square_size=sq_size)
#         for i in range(base,head-sqs*4): square(start-sqs,i,            col_skin, square_size=sq_size)
#         for i in range(base,head-sqs*4): square(start-sqs*2,i,          col_skin, square_size=sq_size)
#         for i in range(base,head-sqs*4): square(start-sqs*3,i,          col_skin, square_size=sq_size)
#         for i in range(base+sqs*3,head-sqs*4): square(start-sqs*4,i,    col_skin, square_size=sq_size)
#         for i in range(base+sqs*3,head-sqs*4): square(start-sqs*5,i,    col_skin, square_size=sq_size)
#         for i in range(base+sqs*3,head-sqs*4): square(start-sqs*6,i,    col_skin, square_size=sq_size)
#         for i in range(base+sqs*3,head-sqs*4): square(start-sqs*7,i,    col_skin, square_size=sq_size)
#         for i in range(base+sqs*3,head-sqs*4): square(start-sqs*8,i,    col_skin, square_size=sq_size)
#         for i in range(base+sqs*4,head-sqs*4): square(start-sqs*9,i,    col_skin, square_size=sq_size)
        

#     def create_new_punk(index, background_color, outline_color, skin_color, facial_hair_color,
#                         nose_mo_color, glasses_color, hat_color, hat_detail_color):
        
        
#         rect(left=0,top=0,right=0,bottom=0,color=background_color)

#         # Add neck and face
#         face_and_neck(sq_size=sqs, col_outline=outline_color, col_skin=skin_color)
        
#         # Add facial hair
#         facial_hair(sq_size=sqs/5,col=facial_hair_color)
        
#         # Add glasses V type
#         glasses_v_type(sq_size=sqs,col=glasses_color)
        
#         # Add nose and mouth
#         nose_mouth(sq_size=sqs,col=nose_mo_color)
        
#         # Add simple hat
#         simple_hat(sq_size=sqs,col_main=hat_color,col_detail=hat_detail_color, col_outline=outline_color)
        
#     #     canvas.show(title = 'title')
#         canvas.save(path+'/assets/'+'0x'+str(index)+'.png',format='PNG')