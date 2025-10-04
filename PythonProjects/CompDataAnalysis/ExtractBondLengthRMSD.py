import numpy as np

"for reading the xyz file and extract atomic symbols and coordinates"
def read_xyz(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        
        atoms = []
        coords = []
        for line in lines[2:]:
            parts = line.split()
            if len(parts) < 4:
                continue
            atoms.append(parts[0])
            coords.append([float(parts[1]), float(parts[2]), float(parts[3])])
            
        return np.array(atoms), np.array(coords)
        
        
"compyte bond length btwn two atoms given their indices"        
def bond_length(coords, atom1, atom2):
    return np.linalg.norm(coords[atom1] - coords[atom2])
    
"compute RMSD btwn two geometries"            
def rmsd(coords1, coords2):
    return np.sqrt(np.mean(np.sum((coords1 - coords2) ** 2, axis=1)))
    
# define input xyzfile
file1 = "/Users/monicautashiro-aichouri/Library/CloudStorage/OneDrive-BowlingGreenStateUniversity/TarnovskyResearch/HYQORCA6Calcs/GeomOptGasPhaseStep1a/BP86/HYQGeomOptBP86GasPhase2.xyz"
file2 = "/Users/monicautashiro-aichouri/Library/CloudStorage/OneDrive-BowlingGreenStateUniversity/TarnovskyResearch/HYQORCA6Calcs/GeomOptGasPhaseStep1a/BP86/BP86withDispersion/HYQGeomOptBP86GasPhase1.xyz"

# read files inputted
atoms1, coords1 = read_xyz(file1)
atoms2, coords2 = read_xyz(file2)

#Defining specific bond indices
CO_bond1_atoms = (1,7)
CO_bond2_atoms = (0,2)

#computing bond length
CO_bond1_file1 = bond_length(coords1, *CO_bond1_atoms)
CO_bond2_file1 = bond_length(coords1, *CO_bond2_atoms)
CO_bond1_file2 = bond_length(coords2, *CO_bond1_atoms)
CO_bond2_file2 = bond_length(coords2, *CO_bond2_atoms)


# Computing RMSD
if len(coords1) == len(coords2):
    rmsd_value = rmsd(coords1, coords2)
    
else:
    print("Error: the two geometries have different number of atoms")
    rmsd_value = None
    
#print results
print("\n=== Bond Lengths & RMSD Comparison ===")
print(f"File 1: {file1}")
print(f"  C-O Bond (Atom {CO_bond1_atoms[0]+1}-{CO_bond1_atoms[1]+1}): {CO_bond1_file1:.4f} Å")
print(f"  C-O Bond (Atom {CO_bond2_atoms[0]+1}-{CO_bond2_atoms[1]+1}): {CO_bond2_file1:.4f} Å")

print(f"\nFile 2: {file2}")
print(f"  C-O Bond (Atom {CO_bond1_atoms[0]+1}-{CO_bond1_atoms[1]+1}): {CO_bond1_file2:.4f} Å")
print(f"  C-O Bond (Atom {CO_bond2_atoms[0]+1}-{CO_bond2_atoms[1]+1}): {CO_bond2_file2:.4f} Å")

if rmsd_value is not None:
    print(f"\nRMSD between {file1} and {file2}: {rmsd_value:.4f} Å")
print("=======================================")

