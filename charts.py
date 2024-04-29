import matplotlib.pyplot as plt

def generate_bar(data, group_by, values, x_label, y_label, title, file_name):
    grouped_data = data.groupby(group_by).sum()

    labels = grouped_data.index
    values = grouped_data[values]
    
    plt.bar(labels, values)

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)

    plt.savefig(f'charts_imgs/{file_name}')
    plt.close()