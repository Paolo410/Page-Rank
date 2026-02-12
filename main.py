import numpy as np

def power_method(A, m):
    n = A.shape[0]
    # Initialize
    x = np.random.rand(n)
    x = x / np.sum(x)
    s = np.full(n, 1/n)
    max_iterations = 1000
    tolerance = 1e-5

    for i in range(max_iterations):
        x_old = x.copy()
        # PageRank iteration
        x = (1 - m )* (A @ x) + m * s
        x = x / np.sum(x)
        # check for convergence
        if np.linalg.norm(x - x_old, 1) < tolerance:
            break
    
    return x, i


def pagerank(file):
    A, names = read_file(file= file)
    n = A.shape[0]
    top_n_pages = min(n, 10)
    # managing dangling nodes
    mask = np.sum(A, axis=0) == 0
    A[:, mask] = 1
    A = A * (np.ones(A.shape, dtype=float)-np.eye(A.shape[0]))
    # finally I can normalize the matrix
    A = A/np.sum(A, axis = 0)
    m = 0.15
    eigenspace_basis, _ = power_method(A, m)
    # I find the normalized eigenspace basis
    normalized = eigenspace_basis/np.sum(eigenspace_basis)
    show_ranking(normalized=normalized, page_names=names, top_n_pages=top_n_pages)


def read_file(file):
    first_line = file.readline().strip().split(" ")
    n_pages = int(first_line[0])
    i = 0
    page_names = []
    for row in file:
        row = row.strip().split(" ")[1]
        page_names.append(row)
        if i >= n_pages-1:
            break
        i = i+1
    A = np.zeros((n_pages, n_pages), dtype=float)
    for row in file:
        row = row.strip().split(" ")
        p1 = int(row[0])
        p2 = int(row[1])
        A[p2-1, p1-1] = 1
    return A, page_names


def show_ranking(normalized, page_names, top_n_pages):
    # Then I find the score of the highest ranked page
    highest_ranked_page = np.argmax(normalized)
    print(f"Highest ranked page is {highest_ranked_page+1} -> {np.max(normalized):.6f}")

    # I want to show the ranking for top_n_pages pages
    print(f"\nTop {top_n_pages} highest ranked pages:")
    top_indices = np.argsort(-normalized)
    for i in range(top_n_pages):
        print(f"{i+1} ({normalized[top_indices[i]]:.6f} points). {top_indices[i]+1} -> {page_names[top_indices[i]]}")


def main():
    file_names = ["hollins.dat", "ex1.dat", "ex2.dat"]
    file = open("./data/"+file_names[0], "r")
    pagerank(file=file)
    file.close()


main()