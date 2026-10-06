import matplotlib.pyplot as plt


def main():
    marks = [45,55,65,60,62,70,72,75,78,80,82,85,90,92]
    
    plt.hist(
        marks,                            #continuous data
        bins = 5,                         #number of groups
        edgecolor = "black",              #border color
        alpha = 0.8,                      #transparency
        rwidth = 0.9                      #relative width of bars
        
    )
    plt.title("marvellous histogram ")
    plt.xlabel = ("marks")
    plt.ylabel("frequency")
    plt.show()
if __name__ == "__main__":
    main()