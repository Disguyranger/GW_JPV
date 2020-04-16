import os


inputPath = os.path.join("../Resources", "cereal.csv")



with open(inputPath, 'r') as f:
    next(f)
    for row in f:
        row = row.split(',')
        if float(row[7]) >= 5:
            print(row)