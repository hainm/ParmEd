def load_maestro(fname, index=0):
    """
    Require Schrodinger suite.

    Parameters
    ----------
    fname : str
        Maestro filename
    index : int
        Index of the structure in `fname`
    """
    from schrodinger.structure import StructureReader
    from parmed import Structure, Atom

    cts = StructureReader(fname)
    start = 0
    ct = None
    while start <= index:
        ct = next(cts)
        start += 1

    struct = Structure()
    for atom in ct.atom:
        p_atom = Atom(name=atom.pdbname.strip(), atomic_number=atom.atomic_number)
        struct.add_atom(p_atom, atom.pdbres.strip(), atom.resnum, chain=atom.chain)
    struct.coordinates = ct.getXYZ()
    return struct
