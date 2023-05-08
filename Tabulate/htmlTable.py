from tabulate import tabulate

table_data = [['Name', 'Age', 'Job'],
               ['Lewis', '29', 'Project Coordinator'],
               ['Lucy', '29', 'Logistics']]

with open ('mytable.html', 'w') as f:
    f.write(tabulate(table_data, headers="firstrow", tablefmt="html"))
