import numpy as np
import matplotlib.pyplot as plt 
from matplotlib.pyplot import figure

chars = plt.imread('Segmentation.bmp')


def different_neighborchk(row_idx,column_idx,imgtracer,img):
    """
    The mini Kernel will be the adjacent neighbors to the center
    """
    idxchanger = [-1,0,1]
    adjacentlist = []
    next_trace_coord = []
    next_trace_coord_li = []
    if ((imgtracer[row_idx, column_idx,0] < 127) == (img[row_idx, column_idx,0] < 127)):
        """
        first difneighbool check
        if the check fails that means the center point has already been modified
        Below is a mini kernel to check the center point
        """
        adjacentlist = np.array([[img[row_idx-1, column_idx-1],img[row_idx-1, column_idx-0],img[row_idx-1, column_idx+1]],\
                                 [img[row_idx-0, column_idx-1],img[row_idx-0, column_idx-0],img[row_idx-0, column_idx+1]],\
                                 [img[row_idx+1, column_idx-1],img[row_idx-1, column_idx-0],img[row_idx+1, column_idx+1]]] )
        if np.all(adjacentlist < 127 ) or np.all(adjacentlist > 127):
            """
        last difneighbool check
        following iteration :
        the center point in the img file has at least one different neighbor if the above clause is false
            """
            return False , adjacentlist ,next_trace_coord
        for iter_rownum in idxchanger :
            """
        second difneighbool check
        if iteration succeeds :
        the center point in the img file has at least one different neighbor
            """
            for iter_column in idxchanger:
                neighbor_on_edge_check = np.array([[img[row_idx+iter_rownum-1, column_idx+iter_column-1],img[row_idx+iter_rownum-1, column_idx+iter_column-0],img[row_idx+iter_rownum-1, column_idx+iter_column+1]],\
                                                   [img[row_idx+iter_rownum-0, column_idx+iter_column-1],img[row_idx+iter_rownum-0, column_idx+iter_column-0],img[row_idx+iter_rownum-0, column_idx+iter_column+1]],\
                                                   [img[row_idx+iter_rownum+1, column_idx+iter_column-1],img[row_idx+iter_rownum-1, column_idx+iter_column-0],img[row_idx+iter_rownum+1, column_idx+iter_column+1]]] )
                if (imgtracer[row_idx+iter_rownum, column_idx+iter_column,0] > 127) \
                and (((imgtracer[row_idx+iter_rownum, column_idx+iter_column,0]) == (img[row_idx+iter_rownum, column_idx+iter_column,0])))\
                and (not np.all(neighbor_on_edge_check < 127) and not np.all(neighbor_on_edge_check > 127)) :
                    """
                    finding the next_trace_coord inate
                    """
                    next_trace_coord_li.append([row_idx+iter_rownum, column_idx+iter_column])
                    next_trace_coord = (row_idx+iter_rownum, column_idx+iter_column)

        return True , adjacentlist , next_trace_coord
    else:
        return False , adjacentlist ,next_trace_coord
    
def dilation(img, kernel_size = 3, border= 10):
    # kernel_size is the width of the outline
    #border protects from index out of bounds exception
    if( border <= kernel_size ):
        border = kernel_size + 1
    imgcopy = np.copy(img)
    imgtracer = np.copy(img)
    columns , rows  = np.shape(chars)[0],np.shape(chars)[1] # size in pixels
    low = border
    high = columns - border if( columns < rows ) else  rows - border
    row_idx = low
    while row_idx < high:
        column_idx = low
        while column_idx < high :
            difneigh_bool , difneigh_li , next_trace_coord = different_neighborchk(row_idx,column_idx,imgtracer,img )           
            while np.all(img[row_idx,column_idx] > 127) \
            and difneigh_bool \
            and (imgtracer[row_idx, column_idx,0] > 127) == (img[row_idx, column_idx,0] > 127):
                while len(next_trace_coord) != 0 \
                and img[next_trace_coord[0],next_trace_coord[1],0] == imgtracer[next_trace_coord[0],next_trace_coord[1],0]:                        
                    if len(next_trace_coord) != 0\
                    and img[next_trace_coord[0],next_trace_coord[1],0] == imgtracer[next_trace_coord[0],next_trace_coord[1],0] :
                        imgtracer[next_trace_coord[0],next_trace_coord[1]] = 0
                        imgcopy[(next_trace_coord[0]-(kernel_size//2)):(next_trace_coord[0]+(kernel_size//2+1)) , (next_trace_coord[1]-(kernel_size//2)):(next_trace_coord[1]+(kernel_size//2+1))] = 0
                    difneigh_bool , difneigh_li , next_trace_coord = different_neighborchk(row_idx,column_idx,imgtracer,img )
                column_idx += 1
            column_idx += 1 
        row_idx += 1
    return imgcopy

figure(dpi=120)

#plt.imshow(chars)   # BEFORE
dilated = dilation(chars, kernel_size = 3, border = 20)
plt.imshow(dilated) 
plt.show()
plt.imshow(dilated) 
plt.savefig("operation.jpeg")