
# make reference file (fasta) for alignments
# input: list of genes with sequences
# output: fasta file with >gene_name \n seq

# If padding sequences are provided, add padding sequences to the output fasta file

import pandas as pd
import argparse

def get_seqs(input_df, output_fasta, padding=None):
    """
    REQUIRED columns in input_df: ["gene_name", "ORF_seq"]
    output_fasta: full path to output fasta file
    padding sequences are in a list of the format: [padding_up, padding_dow]
    """

    if padding:
        output_fasta = output_fasta.repalce(".fasta", "_withpad.fasta")

    with open(output_fasta, "w") as ou:
        
        for index, row in input_df.iterrows():        
            name = ">"+row.gene_name
            ou.writeline(name)
            
            if padding:
                seq = padding[0] + row.ORF_seq + padding[1]
            else:
                seq = row.ORF_seq
            ou.writeline(seq)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Write sequences to fasta file')
    parser.add_argument('-input',help='CSV file with ORF name and sequences')
    parser.add_argument('-output', help="full path to output fasta file")
    
    args = parser.parse_args()

    input_df = pd.read_csv(args.input)
    input_df = input_df["gene_name", "ORF_seq"]

    # make ref with original orf sequences 
    get_seqs(input_df, args.output)

    # make ref with orf sequences + padding sequences
    get_seqs(input_df, args.output, padding=[])

