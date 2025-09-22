class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        # Check if reshape is possible
        if m * n != r * c:
            return mat

        # Flatten the original matrix
        flat = [num for row in mat for num in row]

        # Build reshaped matrix
        new_mat = []
        for i in range(r):
            new_mat.append(flat[i * c : (i + 1) * c])
        
        return new_mat
