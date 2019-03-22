import pandas

def read_csv(filename):
    df = pandas.read_csv(filename)
    return df


def unique(df):
    a = []
    print(a)
    # print(df.iloc[0][1])
    for ix in 2731:
        for jx in length(a):
            if (df.iloc[ix][1] == a[jk]):
                print(df.iloc[ix][1])
                pass
            else:
                len = len(a) + 1
                a[len] = df.iloc[ix][1]
                print(df.iloc[ix][1])


df = read_csv('../csv/all/newall.csv')
unique(df)