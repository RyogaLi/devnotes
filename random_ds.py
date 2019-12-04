# to run this script
# python random_sample.py -input /path/to/fastq.gz
# - all the files in the input directory have to be gzipped
# - the script output down sampled fastq files in the same directory as the original fastq files
# to move them to a new dir you can run `mv *_ds.fastq /new_dir/`
# output fastq files are NOT gzipped, you will need to zip them inorder to run song's script


import pandas as pd
import os
import random
import argparse


def random_lines(input_file, n):
    """
    get n random records from input file 
    output to file *_ds.fastq
    """
    record_number = 0

    base = os.path.basename(input_file)
    output_file = input_file.replace(".fastq", "_ds.fastq")
    
    with open(input_file, "r") as i:
        n_lines = sum([1 for line in i])
    
    total_records = int(n_lines/4)

    if n > total_records:
        os.system("cp "+input_file+ " "+output_file)
        return None
    else:
        records_to_keep = set(random.sample(xrange(total_records + 1), n))

    with open(input_file, "r") as i:
        with open(output_file, "w") as o:
            for line1 in i:
                line2 = i.next()
                line3 = i.next()
                line4 = i.next()
                if record_number in records_to_keep:
                    o.write(line1)
                    o.write(line2)
                    o.write(line3)
                    o.write(line4)
                record_number +=1

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-input", help="")
    
    args = parser.parse_args()
    
    n = 30000

    for f in os.listdir(args.input):
        if f.endswith(".fastq.gz"):
            
            full_path = os.path.join(args.input, f)
            
            os.system("gunzip "+full_path)
            
            f = full_path.replace(".fastq.gz", ".fastq")
            random_lines(f, n)


    #os.system("gzip "+args.input+"*.fastq")

