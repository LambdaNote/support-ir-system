import argparse
import csv


N_FEATURES = 136


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("svmlight")
    parser.add_argument("--output", "-o", default="out.csv")
    args = parser.parse_args()

    with open(args.svmlight) as svmlight_fp, open(args.output, "w") as out_fp:
        reader = csv.reader(svmlight_fp, delimiter=" ")
        writer = csv.writer(out_fp, delimiter=",")

        header = ["label", "qid"] + [f"f_{i}" for i in range(1, N_FEATURES + 1)]
        writer.writerow(header)

        for elems in reader:
            label = int(elems[0])
            qid = int(elems[1].split(":")[1])
            features = [float(e.split(":")[1]) for e in elems[2:-1]]
            writer.writerow([label, qid] + features)
