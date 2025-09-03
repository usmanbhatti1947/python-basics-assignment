# Given two rectangles, find if the given two rectangles overlap or not. A rectangle is denoted by providing the x and y coordinates of two points: the left top corner and the right bottom corner of the rectangle. Two rectangles sharing a side are considered overlapping. (L1 and R1 are the extreme points of the first rectangle and L2 and R2 are the extreme points of the second rectangle).
# 
# Note: It may be assumed that the rectangles are parallel to the coordinate axis.
def do_rectangles_overlap(L1, R1, L2, R2):
    # Check if one rectangle is to the left of the other
    if L1[0] >= R2[0] or L2[0] >= R1[0]:
        return False
    # Check if one rectangle is above the other
    if L1[1] <= R2[1] or L2[1] <= R1[1]:
        return False
    return True 
# Example rectangles to check
L1 = (0, 10)
R1 = (10, 0)
L2 = (5, 5)
R2 = (15, 0)
print(f"Do the rectangles overlap? {do_rectangles_overlap(L1, R1, L2, R2)}")