

def function(list):
    for i in range(len(list)):
        if list[i] != list[-1]:
            print(list[i] + " ", end="")
        else:
            print("and " +  list[i])

spam = ["Pedro", "ze", "Miguel", "zero"]

function(spam)
