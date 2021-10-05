import punksComponents as pc
import sys
path = sys.path[0]

colors={}
colors['BCG'] = ['#d3d3d3']
colors['OUT'] = ['#2f2f2f','#6d696a','#50514f']
colors['SKIN'] = ['#b1a7a6']
colors['GLS'] = ['#2f2f2f','#6d696a','#50514f']
#['#363A43','#023e8a','#bf0603','#edc531']

index = 0
for skin in colors['SKIN']:
    for bg in colors['BCG']:
        for out in colors['OUT']:
            for gls in colors['GLS']:
                
                if out == colors['OUT'][0]:
                    hat = colors['OUT'][1]
                elif out == colors['OUT'][1]:
                    hat = colors['OUT'][2]
                else:
                    hat = colors['OUT'][1]
                
                
                x = pc.newPunk(bcg_color=bg) 
                pc.compFace.typeA(x, 15, out, skin)
                pc.compHat.typeA(x,15, hat, hat, out)
                pc.compNose.typeA(x, 15, out)
                pc.compMouth.typeA(x, 15, out)
                pc.compBeard.typeA(x, 5, out)
                pc.compGlasses.typeA(x, 15, gls)
                x.show_results()
                x.save_results(save_to_path = path+'/assets/'+'0x'+str(index)+'.png')
                index += 1
                
                x = pc.newPunk(bcg_color=bg) 
                pc.compFace.typeA(x, 15, out, skin)
                pc.compHat.typeB(x,15, out, hat, hat)
                pc.compNose.typeA(x, 15, out)
                pc.compMouth.typeA(x, 15, out)
                pc.compBeard.typeA(x, 5, out)
                pc.compGlasses.typeA(x, 15, gls)
                x.show_results()
                x.save_results(save_to_path = path+'/assets/'+'0x'+str(index)+'.png')
                index += 1