triomino_solver
===============

A solver for the tiling with triominos problem described by Jeff Erickson

In his notes about proof by induction (Appendix I on this page: http://web.engr.illinois.edu/~jeffe/teaching/algorithms/), Jeff Erickson describes the problem of tiling a 2^n x 2^n square grid with triominos (L-shaped pieces).  He proves by induction that any such square grid with one square 'blocked in' can be tiled using triominos.  The python code in this repository acts as a 'computational proof' of the claim.

The code follows the inductive proof (specifically the top-down approach) introduced by Professor Erickson.

The user provides an integer n (1 to 5 work with no problems, after that the size of the grid becomes an issue but the code should still work) and a 2^n x 2^n grid is created.  A square in the grid is randomly chosen to be the pre-filled square, and the algorithm proceeds to fill the rest of the grid with triominos.

The code is fairly messy, mainly due to how I chose to implement the 'graphics'.  A better solution is certainly possible.

There are a few spots in the code where intermediate boards are printed to the console.  These lines may be toggled to see or ignore partially solved boards.
