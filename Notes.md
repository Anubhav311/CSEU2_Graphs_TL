# Notes

## Three ways of keeping track of nodes in a graph
1. Adjacency List
2. Adjacency Matrix
3. Objects (by creating a graph class and edge class)

Let's see these ways on following graph:

![](SIMPLE-GRAPH.jpg)

### Adjacency List (can be implemented with a dictionary) => { O(n) }
{
    A: (B, E, D),
    B: (A, C),
    C: (B, E, F),
    D: (A, E),
    E: (A, D, C, F),
    F: (C, E),
}


### Adjacency Matrix (can be implemented with two dimensional array/ array of arrays) => { O(n^2) }
`1` => connected, `0` => not connected

   A B C D E F
A `0 1 0 1 1 0`
B `1 0 1 0 0 0`
C `0 1 0 0 1 1`
D `1 0 0 0 1 0`
E `1 0 1 1 1 0`
F `0 0 1 0 1 0`

