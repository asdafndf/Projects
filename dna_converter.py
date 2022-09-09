# Convert one strand of the DNA to the other strand

def dna_converter(sequence):
    complementers = {
        "A" : "T",
        "T" : "A",
        "G" : "C",
        "C" : "G"
    }
    return "".join([complementers.get(x,"*") for x in sequence.upper()])