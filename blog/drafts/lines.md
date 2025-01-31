# Who Cares About Algebraic Geometry?

*Prerequisites: Linear algebra. Some knowledge of (abstract) algebra, topology and combinatorics is also useful.*

## Introduction

Algebraic geometry is often introduced as "the geometric study of shapes defined by
polynomial equations." While this is certainly true, to the prospective student , this gives little motivation. Moreover, they are likely to be confronted
with many technical topics before the heart of the subject really comes into focus (e.g.
commutative algebra, sheaf theory, schemes; all beautiful subjects of course, but
perhaps hard to appreciate at first).

In view of this, the goal of the following article is to present an interesting
geometric problem (which requires no knowledge of algebraic geometry to understand)
and then explain how the tools afforded to us by algebraic geometry lead to an
elegant solution. We'll also hint at the results one would need to make our argument
fully rigorous. 

## The Problem: Counting Lines

Suppose there are four lines in three-dimensional space. Our problem is to count the
number of lines intersecting all of them. Before moving onto the solution, it is
worth asking some follow-up questions. 

The first question is, can we even count them? i.e. are there even guaranteed to be
finitely many? The answer in general is no. For example, if all 4 lines are parallel
lines in a plane, then there are clearly infinitely many lines meeting all of them.
However, as we shall see, for almost all choices of four lines (in a sense we shall
make precise), there are only finitely many lines intersecting all of them, in fact
it is almost always the same amount!

Second, we have not said exactly what is meant by "three-dimensional space." First,
we do not restrict our coordinates to real numbers, but also allow complex numbers.
This technically makes our lines two-dimensional in a topological sense, but they
still very much act like typical lines; for instance, if we were to take lines in a
plane, any pair of lines would still intersect in at most one point. At most one,
since parallel lines do not intersect, however by adding some extra points you can
make them. This is our second specification: we use *projective* space, as opposed to
*affine* space: space where points are given by triples of complex numbers. In
general, we shall write $\mathbf{A}^n$ for the set of all $n$-tuples of complex
numbers, and call it affine $n$-space.

## Projective Space

To formalise the notion of "points at infinity", we start by examining stereographic
projections.
Consider the unit circle in $\mathbf{R}^2$. We define a map from the unit circle minus
the point $(0,1)$ to the $x$-axis by drawing a line from $(0,1)$ to a point $P$ on
the circle, and seeing where this intersects the $x$-axis. Playing around with a few
examples, you might notice that the bottom "hemisphere" of the circle is mapped into
the interval $(-1,1)$. Inversely, points in the top hemisphere cover the rest of the
$x$-axis. In particular, when you approach $(0,1)$ from the right, the projection
tends towards $+\infty$, and from the left towards $- \infty$. The idea is here is
that if we were to extend this map to the entire unit circle, then $(0,1)$ would get
mapped to such a point at infinity, what both the points on the right and left
are tending towards. The answer turns out to be to flip the problem
on its head.

Notice that the reason we did not originally define the map on all of the unit
circle was that the tangent line to the circle at $(0,1)$ does not intersect the
$x$-axis. However, upon closer inspection, one notices that the lines in the
construction that do meet the $x$-axis are in one-to-one correspondence with it,
given by the $x$-intercept. The solution is then simple: *we take the lines as our
points*, making the troublesome parallel line itself our point at infinity!
This correspondence also preserves the continuity of points, and both
negative and positive directions on the line tend tend towards it, as was observed
in the projection. For those who know some topology, this is an example of a 
*one-point compactification*, in this case applied to $\mathbf{R}$ and yielding the
circle $\mathbf{S}^1$. 

Of course, to speak of all lines going through $(0,1)$, we can simply translate
the situation to the origin, in which case we are talking about all 1-dimensional
vector subspaces of $\mathbf{R}^2$. In fact, as mentioned earlier, we will prefer
to work over the field of complex numbers, $\mathbf{C}$, and in fact, over some fixed
algebraically closed field of characteristic zero $k$ (if you don't know what those 
words mean, it's fine to take $k = \mathbf{C}$). For a general vector space $V$ over
$k$, a one-dimensional subspace can be represented by any non-zero vector $v$ it
contains, and since it is one-dimensional, all other non-zero vectors can be
obtained by scaling $v$. So for our "line plus a point at infinity" construction,
we would take *homogeneous coordinates* $[a,b]$ with $a,b \in k$ not both 0, subject
to the relation $[a,b] \sim [c,d]$ iff there is a $\lambda \in k$ such that
$\lambda \cdot (a,b) = (c,d)$.

In the case $k = \mathbf{C}$, the picture here
is a sphere, with one hemisphere all the points inside the unit disc, and the other
all other points of the complex plane, tending towards our added point at infinity
at the "south pole". Notice that if, say, $a \neq 0$, then by dividing out by $a$, we
get a canonical representative of the form $[1, c]$. You should convince yourself
that this is the same as the correspondence between lines through (0,1) and points
on the $x$-axis described above. In general, for a finite dimensional
vector space $V$ over $k$, we shall define its *projectivization* $\mathbf{P}(V)$
as the set of all one-dimensional subspaces of $V$. Thus, any choice of basis for $V$
gives a system of homogeneous coordinates for $\mathbf{P}(V)$. For convenience,
$\mathbf{P}(k^{n+1})$ is written $\mathbf{P}^n$, and we often use the coordinates
afforded to us by the standard basis 
$e_1 = (1, 0, ..., 0), e_2 = (0, 1, 0, ..., 0), ..., e_{n+1} = (0, 0, ..., 1)$.  

## Lines in $\mathbf{P}^2$ and $\mathbf{P}^3$

The idea is that a line in $\mathbf{P}^n$ should extend the notion as it exists
in $\mathbf{A}^n$. Earlier, we described an inclusion
$\mathbf{A}^1 \xhookrightarrow{i} \mathbf{P}^1$, where $i(x) = [1,x]$. We could of
course also have $x$ map to $[x,1]$. Clearly, these two copies of $\mathbf{A}^1$
in $\mathbf{P}^1$ cover the latter. A simple generalization follows for $n>1$, where
we need $n+1$ copies of $\mathbf{A}^n$ to cover $\mathbf{P}^n$. Thus we shall say
that any "sensible" definition of a line in projective space must be such that for a
line $L \subset \mathbf{P}^n$, $L$ intersected with any copy of $\mathbf{A}^n$ is
a line in that affine space (by our indentification of $\mathbf{A}^n$ with the copy,
though we will not usually say this explicitely). To simplify notation, let's think
about what this means specifically for $\mathbf{P}^2$. The points of $L$ 
$[a_0, a_1, a_2]$ with $a_0 \neq 0$ are exactly those such that
$c_1 \frac{a_1}{a_0} + c_2 \frac{a_2}{a_0} = c_0$, where the coefficients 
$c_0, c_1, c_2$ define our required line.  
