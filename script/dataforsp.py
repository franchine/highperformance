import pandas
import numpy as np

def read_csv(filename):
    df = pandas.read_csv(filename)
    return df


def get_col(df):
    count = 0
    # total_cols = len(df.columns)
    df_bw = df['bw_level']
    export_bw = df_bw.to_csv(r'../csv/mg/bw.csv', index=None, header=True)
    df_node = df['node_count']
    export_node = df_node.to_csv(r'../csv/mg/node.csv', index=None, header=True)
    df_pcap = df['power_cap']
    export_pcap = df_pcap.to_csv (r'../csv/mg/pcap.csv', index = None, header=True)
    df_run = df['runtime']
    export_run = df_run.to_csv(r'../csv/mg/run.csv', index=None, header=True)
    df_thr = df['thread_count']
    export_thr = df_thr.to_csv(r'../csv/mg/thr.csv', index=None, header=True)
    df_app = df['app']
    export_app = df_app.to_csv(r'../csv/mg/apps.csv', index=None, header=True)
    df_alg = df['algorithm']
    export_alg = df_alg.to_csv(r'../csv/mg/alg.csv', index=None, header=True)


def add_grpnode(df):
    df['axis'] = 'node_count'
    df['group'] = 'mg'
    # print(df['group'])
    export_node = df.to_csv(r'../csv/mg/n_n.csv', index=None, header=True)

def add_grpbw(df):
    df['axis'] = 'bw_level'
    df['description'] = ' '
    df['group'] = 'mg'
    export_node = df.to_csv(r'../csv/mg/bw_bw.csv', index=None, header=True)

def add_grppcap(df):
    df['axis'] = 'power_cap'
    df['group'] = 'mg'
    export_node = df.to_csv(r'../csv/mg/p_p.csv', index=None, header=True)
    

def add_grprun(df):
    df['axis'] = 'runtime'
    df['group'] = 'mg'
    export_node = df.to_csv(r'../csv/mg/r_r.csv', index=None, header=True)


def add_grpthr(df):
    df['axis'] = 'thread_count'
    df['group'] = 'mg'
    export_node = df.to_csv(r'../csv/mg/t_t.csv', index=None, header=True)

def add_grpalg(df):
    df['axis'] = 'alg'
    df['group'] = 'mg'
    export_node = df.to_csv(r'../csv/mg/alal.csv', index=None, header=True)
    

def change_vals(df, uni):
    print(uni)

    # power and thr
    new = df.replace([uni[0], uni[1], uni[2]], [1, 2, 3])
    export_node = new.to_csv(r'../csv/mg/a_val.csv', index=None, header=True)
    # print new
    # print df

    # node
    # new = df.replace([uni[0], uni[1], uni[2], uni[3]], [1, 2, 3, 4])
    # export_node = new.to_csv(r'../csv/mg/n_val.csv', index=None, header=True)
    # # print new
    # # print df

    # alg
    # new = df.replace([uni[0], uni[1], uni[2]], [1, 2, 3])
    # export_node = new.to_csv(r'../csv/mg/alg_val.csv', index=None, header=True)
    # # print   df.replace([uni[0],uni[1], uni[2]], [1,2,3])



def concatapp(app, df):
    df = pandas.concat([app, df], axis=1, join='inner')
    df.set_index('group', inplace=True)

    df.to_csv('../csv/mg/tt.csv')

def rearrage_cols(df):
    cols = list(df.columns.values)
    print cols
    df = df[['group', 'axis', 'value', 'description']]
    export_node = df.to_csv(r'../csv/mg/ttt.csv', index=None, header=True)



# getting data
df = read_csv('../../data/mg.csv')
# get_col(df)
alg = read_csv('../csv/mg/alg.csv')
# app = read_csv('../csv/mg/apps.csv')
b = read_csv('../csv/mg/bw.csv')
n = read_csv('../csv/mg/node.csv')
p = read_csv('../csv/mg/pcap.csv')
r = read_csv('../csv/mg/run.csv')
t = read_csv('../csv/mg/thr.csv')
# alg_u = alg['algorithm'].unique()
# # b_u = b['bw_level'].unique()
# n_u = n['node_count'].unique()
# p_u = p['power_cap'].unique()
# # print(r['runtime'].unique())
# t_u = t['thread_count'].unique()
# # change_vals(alg, alg_u)

# nn = read_csv('../csv/mg/n_n.csv')
# nval = read_csv('../csv/mg/n_val.csv')

# pp = read_csv('..')

# pval = read_csv('../csv/mg/p_val.csv')
# pp = read_csv('../csv/mg/p_p.csv')
# tval = read_csv('../csv/mg/t_val.csv')
# tt = read_csv('../csv/mg/t_t.csv')
# algval = read_csv('../csv/mg/alg_val.csv')
# alal = read_csv('../csv/mg/alal.csv')


# new = new[['group', 'axis', 'value', 'description']]
# print(new)


# add_grpbw(b)
# add_grpnode(n)
# add_grpnode(n)
# add_grppcap(p)
# add_grprun(r)
# add_grpthr(t)
# add_grpalg(alg)

# concatapp(tt, tval)
# rearrage_cols(new)

a = read_csv('../csv/mg/a_val.csv')
b = read_csv('../csv/mg/bw.csv')
n = read_csv('../csv/mg/n_val.csv')
p = read_csv('../csv/mg/p_val.csv')
t = read_csv('../csv/mg/t_val.csv')
r = read_csv('../csv/mg/r_val.csv')

# out = a.append(b)
# out = out.append(n)
# out = out.append(p)
# out = out.append(t)
# out.to_csv(r'../csv/mg/kspider.csv', index=None, header=True)
# cols =  ['bw_level','node_count','power_cap','runtime','thread_count']

# r['runtime'] = r['runtime'] / 10
# r.to_csv(r'../csv/mg/r_val.csv', index=None, header=True)
print a.loc[:, "value"].mean()
print b.loc[:, "value"].mean()
print n.loc[:, "value"].mean()
print p.loc[:, "value"].mean()
print r.loc[:, "value"].mean()
print t.loc[:,"value"].mean()