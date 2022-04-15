import pandas as pd


def fill_missing_time_bins(uniq_cluster_after, df_removed_rare_clusters, min_time_bin, max_time_bin):
    return_df = pd.DataFrame(columns=['time_bin', 'frequency', 'h3_point'])
    print(min_time_bin, max_time_bin)
    for i in uniq_cluster_after:
        print(i)
        new_df = df_removed_rare_clusters[df_removed_rare_clusters['h3_point'] == i]
        new_df = new_df.sort_values(by=['time_bin'])
        min20 = list(new_df['time_bin'].values)
        fre = list(new_df['frequency'].values)
        min_time_20 = []
        frquen = []
        ind = 0
        print(ind)
        for l in range(min_time_bin, max_time_bin + 1, 1):
            print(l)
            min_time_20.append(l)
            if l in min20:
                frquen.append(fre[ind])
                ind = ind + 1
            else:
                frquen.append(0)
        df_new_2 = pd.DataFrame({'time_bin': min_time_20, 'frequency': frquen})
        df_new_2['h3_point'] = i
        return_df = return_df.append(df_new_2, ignore_index=True)
        # print(i)
    return return_df
