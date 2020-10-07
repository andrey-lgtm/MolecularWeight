#!/usr/bin/python3


open_brackets = ["(", "[", "{"]
close_brackets = ["}", "]", ")"]


def calc_mass(instr):
    elements = {'H': 1.00794, 'He': 4.002602, 'Li': 6.941, 'Be': 9.012182, 'B': 10.811, 'C': 12.0107, 'N': 14.0067,
                'O': 15.9994, 'F': 18.9984032, 'Ne': 20.1797, 'Na': 22.98976928, 'Mg': 24.305, 'Al': 26.9815386,
                'Si': 28.0855, 'P': 30.973762, 'S': 32.065, 'Cl': 35.453, 'Ar': 39.948, 'K': 39.0983, 'Ca': 40.078,
                'Sc': 44.955912, 'Ti': 47.867, 'V': 50.9415, 'Cr': 51.9961, 'Mn': 54.938045,
                'Fe': 55.845, 'Co': 58.933195, 'Ni': 58.6934, 'Cu': 63.546, 'Zn': 65.409, 'Ga': 69.723, 'Ge': 72.64,
                'As': 74.9216, 'Se': 78.96, 'Br': 79.904, 'Kr': 83.798, 'Rb': 85.4678, 'Sr': 87.62, 'Y': 88.90585,
                'Zr': 91.224, 'Nb': 92.90638, 'Mo': 95.94, 'Tc': 98.9063, 'Ru': 101.07, 'Rh': 102.9055, 'Pd': 106.42,
                'Ag': 107.8682, 'Cd': 112.411, 'In': 114.818, 'Sn': 118.71, 'Sb': 121.760, 'Te': 127.6,
                'I': 126.90447, 'Xe': 131.293, 'Cs': 132.9054519, 'Ba': 137.327, 'La': 138.90547, 'Ce': 140.116,
                'Pr': 140.90465, 'Nd': 144.242, 'Pm': 146.9151, 'Sm': 150.36, 'Eu': 151.964, 'Gd': 157.25,
                'Tb': 158.92535, 'Dy': 162.5, 'Ho': 164.93032, 'Er': 167.259, 'Tm': 168.93421, 'Yb': 173.04,
                'Lu': 174.967, 'Hf': 178.49, 'Ta': 180.9479, 'W': 183.84, 'Re': 186.207, 'Os': 190.23, 'Ir': 192.217,
                'Pt': 195.084, 'Au': 196.966569, 'Hg': 200.59, 'Tl': 204.3833, 'Pb': 207.2, 'Bi': 208.9804,
                'Po': 208.9824, 'At': 209.9871, 'Rn': 222.0176, 'Fr': 223.0197, 'Ra': 226.0254, 'Ac': 227.0278,
                'Th': 232.03806, 'Pa': 231.03588, 'U': 238.02891, 'Np': 237.0482, 'Pu': 244.0642, 'Am': 243.0614,
                'Cm': 247.0703, 'Bk': 247.0703, 'Cf': 251.0796, 'Es': 252.0829, 'Fm': 257.0951, 'Md': 258.0951,
                'No': 259.1009, 'Lr': 262, 'Rf': 267, 'Db': 268, 'Sg': 271, 'Bh': 270, 'Hs': 269, 'Mt': 278,
                'Ds': 281, 'Rg': 281, 'Cn': 285, 'Nh': 284, 'Fl': 289, 'Mc': 289, 'Lv': 292, 'Ts': 294, 'Og': 294}
    # checking and arranging for atoms and compounds
    atom = {}
    i = 0

    while (i < len(instr)):
        if (ord(instr[i]) >= 65 and ord(instr[i]) <= 90):
            if (i + 1 < len(instr) and ord(instr[i + 1]) >= 97
                    and ord(instr[i + 1]) <= 122):
                el = instr[i:i + 2]
                i += 1
            else:
                el = instr[i]
        else:
            i += 1
            continue

            # print(el)
        if (el not in elements.keys()):
            print("Element {} not found in dict".format(el))
            exit(1)

        # Find how many of this atom
        j = i + 1
        while (j < len(instr) and ord(instr[j]) <= 57
               and ord(instr[j]) >= 48):
            j += 1

        if (i + 1 == j):
            nel = 1
        else:
            nel = int(instr[i + 1:j])
        i = j - 1

        # Check for surrounding brackets
        brac_level = 0  # bracket depth level
        for l in instr[:i]:
            if (l in open_brackets):
                brac_level += 1
            if (l in close_brackets):
                brac_level -= 1

        # Find the multiplication factor
        multf = 1

        # Esape out of the brackets one level at a time
        for b in range(brac_level, 0, -1):
            b_current = b
            for l in range(i, len(instr)):
                if (instr[l] in open_brackets):
                    b_current += 1
                    break

                if instr[l] in close_brackets:
                    b_current -= 1
                    if (b_current == b - 1):
                        k = l + 1
                        while (k < len(instr) and ord(instr[k]) <= 57
                               and ord(instr[k]) >= 48):
                            k += 1

                        if (k + 1 == l):
                            multf *= 1
                        else:
                            multf *= int(instr[l + 1:k])
                        l = k - 1
                        break

        if (el not in atom):
            atom[el] = multf * nel
        else:
            atom[el] += multf * nel
        i += 1
    # calculating mass for all atom or molecular weight
    mass = 0.0
    for i in atom:
        mass += atom[i] * elements[i]
    return mass


def main():
    # take input as string
    formula = input()
    #printing output without rounding
    print(calc_mass(formula))


if __name__ == "__main__":

    main()