import pandas as pd
import os
import argparse


def sort_files(mut2func, fastq_list, folder_list):
    """
    read sample ID from mut2func and select corresponding fastq files
    move all the fastq files into corresponding folders
    """
    df = pd.read_csv(mut2func)
    all_samples = df.loc[:, df.columns != 'tiles'].values.tolist()
    all_samples = [str(item) for sublist in all_samples for item in sublist]
    row_names = df["tiles"].tolist()
    print(all_samples)
    for f in os.listdir(fastq_path):
        if f.endswith(".fastq.gz"):
            i = f.split("_")[0]
            if i in all_samples:
                cmd = "cp " + os.path.join(fastq_path, f) + " " +output_path
                os.system(cmd)

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--o", help="output path")
    parser.add_argument("--f", help="fastq path")
    parser.add_argument("--mut", help="mut2funcc file")
    args = parser.parse_args()

    mut2func = args.mut
    output_path = args.o
    fastq_path = args.f

    sort_files(mut2func, fastq_path, output_path)


    
