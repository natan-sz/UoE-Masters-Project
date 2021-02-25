#!/usr/bin/python3

from ase import io

output = "h2o.2_MD_stress.out"

atoms = io.read(output)
print("File: " + output + "\n")
print("Positions:\n")
print(atoms.get_positions())
print("\n")
print("Chemical Symbols:\n")
print(len(atoms.get_chemical_symbols()))
print("\n")
print("Cell:\n")
print(atoms.get_cell())
print("\n")
print("Potential Energy:\n")
print(atoms.get_potential_energy())
print("\n")
print("Forces:\n")
print(atoms.get_forces())
print("\n")
print("Stress:\n")
print(atoms.get_stress())
print("\n")
