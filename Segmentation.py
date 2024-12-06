import subprocess
import argparse
import os
# Define the commands with their arguments

def get_arguments():

    parser = argparse.ArgumentParser(description="SwinUnetr")

    parser.add_argument("--dataset_dir", type=str, default='example/patches')

    parser.add_argument("--reload_path", type=str,
                        default='weight/best_model.pth')
    parser.add_argument("--output_folder", type=str, default='output')

    return parser

if __name__ == '__main__':

    parser = get_arguments()
    print(parser)
    args = parser.parse_args()


    save_csv= [
        "python", "save_csv.py",
        "--dataset_dir",
        args.dataset_dir,
        "--data_list",
        args.dataset_dir,

    ]

    predicting = [
        "python", "predicting.py",
        "--valset_dir",
        os.path.join(args.dataset_dir, "data_list.csv"),
        "--reload_path",
        args.reload_path,
        "--result_folder",
        args.output_folder,
    ]

    # Run each command in sequence
    subprocess.run(save_csv)
    subprocess.run(predicting)