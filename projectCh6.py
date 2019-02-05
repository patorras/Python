
tableData = [["apples", "oranges", "cherries", "banana"],
            ["Alice", "Bob", "Carols", "David"],
            ["dogs", "cats", "moose", "goose"]]

def printTable(list):
    colWidths = [0] * len(list)
    col = 0

    for lists in list:
    	for indexes in lists:
    		if len(indexes) > colWidths[col]:
    			colWidths[col] = len(indexes)
    		else:
    			break
    	col = col + 1

    max = 0
    for i in range(len(colWidths)):
        if colWidths[i] > max:
            max = colWidths[i]
        else:
            max = max


    for i in range(len(list)):
        for y in range(len(list)):
            print(list[y][i].rjust(max), end = ' ')

        print("")




printTable(tableData)
