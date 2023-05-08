from tabulate import tabulate

data = {
    'Name': ['Lucy','Lewis','Zoe'],
    'Age': ['29','30','31'],
    'Job' : ['Logistics','Project Coordinator','Sales']
}
    
print(tabulate(data, headers="keys", tablefmt="fancy_grid", showindex="always")) 