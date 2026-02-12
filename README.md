# PageRank Algorithm Implementation

Python implementation of the PageRank algorithm, inspired by the paper **"The $25,000,000,000 Eigenvector: The Linear Algebra Behind Google"** by Kurt Bryan and Tanya Leise.

📄 **Original paper:** [SIAM Review (2006)](https://www.rose-hulman.edu/~bryan/googleFinalVersionFixed.pdf)

## Authors

| Name | Student ID | Email |
|------|------------|-------|
| Stefano Falcione | s352590 | s352590@studenti.polito.it |
| Paolo Malugani | s359857 | s359857@studenti.polito.it |

## Overview

This project explores the linear algebra behind Google's PageRank algorithm, implementing the power method to compute the dominant eigenvector of a stochastic matrix. PageRank assigns an importance score to each web page based on the link structure.

## Project Structure

```
├── main.py              # Complete working implementation
├── pagerank.ipynb       # Notebook with detailed analysis and visualizations
├── exercises.ipynb      # Solved exercises from the paper (Ex. 1-16)
├── ex1.ipynb            # Exercise 1 with plots
└── data/
    ├── hollins.dat      # Hollins University dataset (6012 pages, 23875 links)
    ├── ex1.dat
    └── ex2.dat
```

## Implementation

### Key Features

- **Power Method**: Iterative method to compute the dominant eigenvector
- **Dangling nodes handling**: Pages with no outgoing links are handled by distributing their "vote" equally
- **Damping factor**: Parameter `m = 0.15` (value used by Google) to guarantee convergence
- **Google Matrix**: Construction of matrix `M = (1-m)A + mS` ensuring a unique solution

### Algorithm

1. Build the adjacency matrix `A` from the link graph
2. Handle dangling nodes (zero columns)
3. Normalize to obtain a column-stochastic matrix
4. Apply the damping factor to get the Google matrix `M`
5. Power method to find the eigenvector with eigenvalue 1

## Usage

```bash
python main.py
```

Example output on the Hollins dataset:
```
Highest ranked page is 1069 -> 0.012345
Top 10 highest ranked pages:
1 (0.012345 points). 1069 -> http://...
2 (0.011234 points). 2045 -> http://...
...
```

## Mathematical Concepts

This project implements the following concepts from the paper:

- **Column-stochastic matrices**: each column sums to 1
- **Perron-Frobenius theorem**: guarantees the existence of a positive eigenvector
- **Power Method convergence**: with damping factor, the second eigenvalue is `λ₂ = 1-m`
- **Probabilistic interpretation**: PageRank represents the stationary probability of a random surfer

## Solved Exercises

The `exercises.ipynb` notebook contains solutions to exercises from the paper:

| Exercise | Description |
|----------|-------------|
| Ex. 1 | Analysis of the effect of adding a page linking to another |
| Ex. 2 | Construction of webs with disconnected subgraphs |
| Ex. 3 | Dimension of eigenspace V₁(A) for connected graphs |
| Ex. 4 | Dangling nodes and sub-stochastic matrix |
| Ex. 5 | Proof: pages with no backlinks have score 0 |
| Ex. 11-14 | Construction and analysis of Google matrix M |
| Ex. 15-16 | Diagonalizability of M |

## Requirements

```
numpy
matplotlib (for visualizations in notebooks)
```

## Dataset

The project was tested on the **Hollins University** dataset (`hollins.dat`):
- 6012 web pages
- 23875 links
- 3189 dangling nodes (handled by the algorithm)

## References

- Bryan, K., & Leise, T. (2006). *The $25,000,000,000 Eigenvector: The Linear Algebra Behind Google*. SIAM Review, 48(3), 569-581. [DOI: 10.1137/050623280](https://doi.org/10.1137/050623280)
- Page, L., Brin, S., Motwani, R., & Winograd, T. (1999). *The PageRank Citation Ranking: Bringing Order to the Web*. Stanford InfoLab.
