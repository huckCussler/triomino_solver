#! /usr/bin/python

# Draw a s x s checkerboard
#
# param s: length of each side of the board
#
# optional param dct: should not be passed by humans
def drawBoard(s, dct=dict()):
    import sys
    if len(dct) == 0:
        for i in range(s):
            for j in range(s):
                dct[i, j] = [0, False]
    for i in range(s):
        sys.stdout.write(" _")
    sys.stdout.write("\n")
    for i in range(s):
        for j in range(s):
            if dct[i, j][0] == 0 or dct[i, j][0] == 201 \
               or dct[i, j][0] == 211 or dct[i, j][0] == 220 \
               or dct[i, j][0] == 222 or dct[i, j][0] == 232:
                sys.stdout.write("|_")
            elif dct[i, j][0] == 200 or dct[i, j][0] == 210 \
                 or dct[i, j][0] == 230:
                sys.stdout.write("| ")
            elif dct[i, j][0] == 202 or dct[i, j][0] == 212 \
                 or dct[i, j][0] == 231:
                sys.stdout.write(" _")
            elif dct[i, j][0] == 221:
                sys.stdout.write("  ")
#+ "\u035F"
            elif dct[i, j][0] == 1:
                sys.stdout.write("|" + "X")
        sys.stdout.write("|\n")
    print("")

# Solves a triomono problem of size 2^n x 2^n where the 'blacked in'
# square (denoted with an 'X') is chosen randomly from the board
#
# param n: 2^n will be the length of each side of the board
def solve(n):
    import random
    side = 2**n
    d = dict()
    for i in range(side):
        for j in range(side):
            d[i, j] = [0, False]
    start_x = random.randrange(side)
    start_y = random.randrange(side)
    d[start_x, start_y] = [1, True]
    drawBoard(side, d)  # draws the initial board
    raw_input()
    recurSolve([0, side-1], [0, side-1], side, d)
    drawBoard(side, d)  # draws the final board

# Helper function for solve()
# If size of board to be solved is 2 x 2, there will be one 'marked' square and
# three unmarked squares.  Therefore, we draw the appropriate shape to
# fill in the three unmarked squares of the board and return.
#
# Otherwise, divides the box into four smaller boxes, marks appropriate
# squares and draws the correct shape in those squares, then recursively
# solves each smaller square
#
# param r: list of two integers denoting the minimum row index and maximum
#          row index for the sub-square being solved
#
# param c: same as param r except for columns
#
# param s: size of each side of the full square
#
# param d: dictionary that maps each row by column index in the full square
#          to two values, [int, Boolean].  The int tells the draw method what
#          should be drawn at that index.  The Boolean is used as a flag to
#          determine which squares need to be marked as 'solved' in order to
#          determine how the surrounding squares will be solved.
def recurSolve(r, c, s, d):
    # if the board is 2x2, identify the 'marked' square and fill in the
    # remaining three squares with the appropriate shape
    # a 2x2 square is our base case
    if r[1] - r[0] == 1:
        if d[r[0], c[0]][1]:
            d[r[0], c[1]][0] = 200
            d[r[1], c[0]][0] = 201
            d[r[1], c[1]][0] = 202
        elif d[r[0], c[1]][1]:
            d[r[0], c[0]][0] = 210
            d[r[1], c[0]][0] = 211
            d[r[1], c[1]][0] = 212
        elif d[r[1], c[0]][1]:
            d[r[0], c[0]][0] = 220
            d[r[0], c[1]][0] = 221
            d[r[1], c[1]][0] = 222
        elif d[r[1], c[1]][1]:
            d[r[0], c[0]][0] = 230
            d[r[0], c[1]][0] = 231
            d[r[1], c[0]][0] = 232
        #drawBoard(s, d) # uncomment to see how each 2x2 sub-square is solved
        #raw_input()
        return
    # the board is NOT 2x2, in which case we divide into four equally sized
    # boards, identify the sub-board that is 'marked' then find the appropriate
    # shape to mark the remaining three boards and draw that shape on the
    # larger board.  Now we have four smaller boards, each with one marked
    # square and we recursively call this function on each of those four boards
    maxR = r[1]
    minR = r[0]
    maxC = c[1]
    minC = c[0]
    subMaxR = minR + (maxR - minR) // 2
    subMinR = subMaxR + 1
    subMaxC = minC + (maxC - minC) // 2
    subMinC = subMaxC + 1
    f1 = False
    f2 = False
    f3 = False
    f4 = False
    for r in range(minR, maxR+1):
        for c in range(minC, maxC+1):
            if r <= subMaxR and c <= subMaxC:
                if d[r, c][1]:
                    f1 = True
            elif r <= subMaxR and c > subMaxC:
                if d[r, c][1]:
                    f2 = True
            elif r > subMaxR and c <= subMaxC:
                if d[r, c][1]:
                    f3 = True
            elif r > subMaxR and c > subMaxC:
                if d[r, c][1]:
                    f4 = True
    if f1:
        d[subMaxR, subMinC] = [200, True]
        d[subMinR, subMaxC] = [201, True]
        d[subMinR, subMinC] = [202, True]
    elif f2:
        d[subMaxR, subMaxC] = [210, True]
        d[subMinR, subMaxC] = [211, True]
        d[subMinR, subMinC] = [212, True]
    elif f3:
        d[subMaxR, subMaxC] = [220, True]
        d[subMaxR, subMinC] = [221, True]
        d[subMinR, subMinC] = [222, True]
    elif f4:
        d[subMaxR, subMaxC] = [230, True]
        d[subMaxR, subMinC] = [231, True]
        d[subMinR, subMaxC] = [232, True]
    #drawBoard(s, d) # uncomment to see EVERY step in the solution
    #raw_input()
    recurSolve([minR, subMaxR], [minC, subMaxC], s, d)
    recurSolve([minR, subMaxR], [subMinC, maxC], s, d)
    recurSolve([subMinR, maxR], [minC, subMaxC], s, d)
    recurSolve([subMinR, maxR], [subMinC, maxC], s, d)

if __name__ == "__main__":
    print("Integer from 1 to ?:")
    n = raw_input()
    solve(int(n))
