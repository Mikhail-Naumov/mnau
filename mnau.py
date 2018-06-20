from tqdm import tqdm

def plot_empties(bad_form)
    plt.figure(figsize=(15,15))

    i = 1
    for j in tqdm(bad_form):
        plt.subplot(230+i)
        sns.heatmap(pd.DataFrame(bad_form[j].isnull().sum()/bad_form[j].shape[0]*100),
                    annot=True,cmap=sns.color_palette("cool"),linewidth=1,linecolor="white")
        plt.title(j)
        i+=1

    plt.subplots_adjust(wspace = 1.6)
    return