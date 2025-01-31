
Let $A$ be an $n \times n$ matrix over the complex numbers. The characteristic polynomial of $A$
is a degree $n$ monic polynomial $\chi_{A}$ defined as $\det(x I_{n} - A)$, where $I_{n}$ is the $n \times n$ identity matrix.
The *Cayley-Hamilton Theorem* states that $\chi_{A}(A) = 0$. In other words, the matrix $\chi_{A}(A)$ is identically 0 when viewed as a linear operator on $\mathbf{C}^n$. We shall begin with observing a case where the theorem is "obvious", namely if $n=1$. Indeed, $1 \times 1$ matrices can simply be identified with $\mathbf{C}$. So if the unique entry of $A$ is $a \in \mathbf{C}$, then  $\chi_{A}(x) = \det(x \cdot 1 - a) = x -a$, and clearly this polynomial will vanish at $A$.

This trivial fact will be "all" we need in a sense. First, diaganolizable matrices are precisely those matrices which fall into the case above for an individual eigenvector $v$, in the sense that $A v = \lambda v$ for some $\lambda \in \mathbf{C}$. So we get that $\chi_{A}(A)v = \chi_{A}(\lambda)v$ and $\lambda$ must be a root of $\chi_{A}$. Since the eigenvectors of $A$ span $\mathbf{C}^n$ iff it is diaganolisable, this is enough to show that $\chi_{A}(A) = 0$. 

Second, consider the map $f: \mathrm{Mat}_{n \times n}(\mathbf{C}) \to \mathrm{Mat}_{n\times n}(\mathbf{C})$ defined by $A \mapsto \chi_{A}(A)$. This is a polynomial function in the entries of the matrix, so if it vanishes "almost everywhere", then it is in fact identically 0. The connection between these two statements is then the following result:

**Theorem.** The subset of diagonalisable matrices $D \subseteq \mathrm{Mat}_{n \times n}(\mathbf{C})$ is dense. More precisely, it contains the complement of the zero-set of a non-zero polynomial function in the entries of matrices.






