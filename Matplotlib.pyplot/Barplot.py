import matplotlib.pyplot as plt


def main():
    language = ["c","c++","java" , "python"]
    students = [30,40,35,30]
    
    plt.bar(
        language ,                        #value of X axis
        students,                         #value of Y axis
        width = 0.6,                      #width of bar
        edgecolor= "black",               #border of bar
        linewidth = 2,                    #width of bar border
        alpha = 0.8,                      #transperance 0.0 to 1.0
        label = "students"                #lagend text
        
    )
    
    plt.title("Marvellous Bar plot")
    plt.xlabel("language")
    plt.ylabel("students")
    plt.legend()
    plt.show()
    


if __name__ == "__main__":
    main()