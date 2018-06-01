# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def keypose(read):
    a0=50
    zz=24
    zs=float (19)
    yy=18
    k=float (0.048)
    keydic={'Ctrl1':[0,-(a0+20),12],
            'WIN1':[0,-(a0+20),12+zz],
            'Alt1':[0,-(a0+20),12+2*zz],
            ' ':[0,-(a0+20),130],
            'Alt2':[0,-(a0+20),130+12+2*zz],
            'WIN2':[0,-(a0+20),142+3*zz],
            'MClick':[0,-(a0+20),142+4*zz],
            'Ctrl2':[0,-(a0+20),142+5*zz],
            'Shift1':[float (k*yy),-(a0+20+yy),22],
            'z':[float (k*yy),-(a0+20+yy),53],
            'Z':[float (k*yy),-(a0+20+yy),53],
            'x':[float (k*yy),-(a0+20+yy),53+zs],
            'X':[float (k*yy),-(a0+20+yy),53+zs],
            'c':[float (k*yy),-(a0+20+yy),53+2*zs],
            'C':[float (k*yy),-(a0+20+yy),53+2*zs],
            'v':[float (k*yy),-(a0+20+yy),53+3*zs],
            'V':[float (k*yy),-(a0+20+yy),53+3*zs],
            'b':[float (k*yy),-(a0+20+yy),53+4*zs],
            'B':[float (k*yy),-(a0+20+yy),53+4*zs],
            'n':[float (k*yy),-(a0+20+yy),53+5*zs],
            'N':[float (k*yy),-(a0+20+yy),53+5*zs],
            'm':[float (k*yy),-(a0+20+yy),53+6*zs],
            'M':[float (k*yy),-(a0+20+yy),53+6*zs],
            ',':[float (k*yy),-(a0+20+yy),53+7*zs],
            '.':[float (k*yy),-(a0+20+yy),53+8*zs],
            '/':[float (k*yy),-(a0+20+yy),53+9*zs],
            'Shift2':[float (k*yy),-(a0+20+yy),22+10*zs+43],
            'Cap':[float (2*k*yy),-(a0+20+2*yy),17],
            'a':[float (2*k*yy),-(a0+20+2*yy),43],
            'A':[float (2*k*yy),-(a0+20+2*yy),43],
            's':[float (2*k*yy),-(a0+20+2*yy),43+zs],
            'S':[float (2*k*yy),-(a0+20+2*yy),43+zs],
            'd':[float (2*k*yy),-(a0+20+2*yy),43+2*zs],
            'D':[float (2*k*yy),-(a0+20+2*yy),43+2*zs],
            'f':[float (2*k*yy),-(a0+20+2*yy),43+3*zs],
            'F':[float (2*k*yy),-(a0+20+2*yy),43+3*zs],
            'g':[float (2*k*yy),-(a0+20+2*yy),43+4*zs],
            'G':[float (2*k*yy),-(a0+20+2*yy),43+4*zs],
            'h':[float (2*k*yy),-(a0+20+2*yy),43+5*zs],
            'H':[float (2*k*yy),-(a0+20+2*yy),43+5*zs],
            'j':[float (2*k*yy),-(a0+20+2*yy),43+6*zs],
            'J':[float (2*k*yy),-(a0+20+2*yy),43+6*zs],
            'k':[float (2*k*yy),-(a0+20+2*yy),43+7*zs],
            'K':[float (2*k*yy),-(a0+20+2*yy),43+7*zs],
            'l':[float (2*k*yy),-(a0+20+2*yy),43+8*zs],
            'L':[float (2*k*yy),-(a0+20+2*yy),43+8*zs],
            ';':[float (2*k*yy),-(a0+20+2*yy),43+9*zs],
            '\'':[float (2*k*yy),-(a0+20+2*yy),43+10*zs],
            'Enter':[float (2*k*yy),-(a0+20+2*yy),33+20+11*zs],
            'Tab':[float (3*k*yy),-(a0+20+3*yy),15],
            'q':[float (3*k*yy),-(a0+20+3*yy),39],
            'Q':[float (3*k*yy),-(a0+20+3*yy),39],
            'w':[float (3*k*yy),-(a0+20+3*yy),zs+39],
            'W':[float (3*k*yy),-(a0+20+3*yy),zs+39],
            'e':[float (3*k*yy),-(a0+20+3*yy),2*zs+39],
            'E':[float (3*k*yy),-(a0+20+3*yy),2*zs+39],
            'r':[float (3*k*yy),-(a0+20+3*yy),3*zs+39],
            'R':[float (3*k*yy),-(a0+20+3*yy),3*zs+39],
            't':[float (3*k*yy),-(a0+20+3*yy),4*zs+39],
            'T':[float (3*k*yy),-(a0+20+3*yy),4*zs+39],
            'y':[float (3*k*yy),-(a0+20+3*yy),5*zs+39],
            'Y':[float (3*k*yy),-(a0+20+3*yy),5*zs+39],
            'u':[float (3*k*yy),-(a0+20+3*yy),6*zs+39],
            'U':[float (3*k*yy),-(a0+20+3*yy),6*zs+39],
            'i':[float (3*k*yy),-(a0+20+3*yy),7*zs+39],
            'I':[float (3*k*yy),-(a0+20+3*yy),7*zs+39],
            'o':[float (3*k*yy),-(a0+20+3*yy),8*zs+39],
            'O':[float (3*k*yy),-(a0+20+3*yy),8*zs+39],
            'p':[float (3*k*yy),-(a0+20+3*yy),9*zs+39],
            'P':[float (3*k*yy),-(a0+20+3*yy),9*zs+39],
            '[':[float (3*k*yy),-(a0+20+3*yy),10*zs+39],
            ']':[float (3*k*yy),-(a0+20+3*yy),11*zs+39],
            '\\':[float (3*k*yy),-(a0+20+3*yy),12*zs+30+14],
            '`':[float (4*k*yy),-(a0+20+4*yy),float (zs/2)],
            '1':[float (4*k*yy),-(a0+20+4*yy),float (zs/2+zs)],
            '2':[float (4*k*yy),-(a0+20+4*yy),float (zs/2+2*zs)],
            '3':[float (4*k*yy),-(a0+20+4*yy),float (zs/2+3*zs)],
            '4':[float (4*k*yy),-(a0+20+4*yy),float (zs/2+4*zs)],
            '5':[float (4*k*yy),-(a0+20+4*yy),float (zs/2+5*zs)],
            '6':[float (4*k*yy),-(a0+20+4*yy),float (zs/2+6*zs)],
            '7':[float (4*k*yy),-(a0+20+4*yy),float (zs/2+7*zs)],
            '8':[float (4*k*yy),-(a0+20+4*yy),float (zs/2+8*zs)],
            '9':[float (4*k*yy),-(a0+20+4*yy),float (zs/2+9*zs)],
            '0':[float (4*k*yy),-(a0+20+4*yy),float (zs/2+10*zs)],
            '-':[float (4*k*yy),-(a0+20+4*yy),float (zs/2+11*zs)],
            '=':[float (4*k*yy),-(a0+20+4*yy),float (zs/2+12*zs)],
            'BackSpace':[float (4*k*yy),-(a0+20+4*yy),13*zs+19]
            }
    if read in keydic:
        output=keydic.get(read)
        return output
    else:
        print('Whoops! No keys found!')
        return
   
