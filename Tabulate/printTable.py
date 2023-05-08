from tabulate import tabulate

table_data = [['Name', 'Age', 'Job'],
               ['Lewis', '29', 'Project Coordinator'],
               ['Lucy', '29', 'Logistics']]

print(tabulate(table_data, headers="firstrow", tablefmt="fancy_grid")) 