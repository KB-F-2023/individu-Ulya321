# Inisialisasi graf yang merepresentasikan peta
graph = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V': ['SA', 'NSW']
}

# Inisialisasi variabel
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V']

# Inisialisasi domain nilai untuk setiap variabel
domain = {
    'WA': ['red', 'green', 'blue'],
    'NT': ['red', 'green', 'blue'],
    'SA': ['red', 'green', 'blue'],
    'Q': ['red', 'green', 'blue'],
    'NSW': ['red', 'green', 'blue'],
    'V': ['red', 'green', 'blue']
}

# Fungsi untuk mengecek apakah nilai yang diberikan pada variabel konflik dengan variabel tetangga
def is_consistent(var, value, assignment):
    for neighbor in graph[var]:
        if neighbor in assignment and assignment[neighbor] == value:
            return False
    return True

# Fungsi rekursif untuk mencari solusi
def backtrack(assignment):
    # Jika assignment sudah memenuhi semua variabel, return assignment
    if len(assignment) == len(variables):
        return assignment
    
    # Pilih variabel yang belum memiliki nilai
    unassigned_vars = [var for var in variables if var not in assignment]
    var = unassigned_vars[0]
    
    # Coba semua nilai yang mungkin untuk variabel tersebut
    for value in domain[var]:
        if is_consistent(var, value, assignment):
            # Jika nilai memenuhi kendala, tambahkan ke assignment dan coba variabel berikutnya
            assignment[var] = value
            result = backtrack(assignment)
            if result is not None:
                return result
            # Jika solusi tidak ditemukan, kembalikan variabel ke keadaan sebelumnya dan coba nilai berikutnya
            del assignment[var]
    
    # Jika tidak ada nilai yang memenuhi kendala, kembalikan None
    return None

# Cetak solusi
solution = backtrack({})
print(solution)
