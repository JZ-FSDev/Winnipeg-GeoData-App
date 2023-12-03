input_file_path = 'Neighbourhood_street.sql'
output_file_path = 'modified_sql_script.sql'

with open(input_file_path, 'r') as input_file, open(output_file_path, 'w') as output_file:
    for line in input_file:
        # Replace 'INSERT INTO NeighBourhood_Street' with 'INSERT INTO Neighbourhood_Street'
        modified_line = line.replace('INSERT INTO NeighBourhood_Street', 'INSERT INTO Neighbourhood_Street')
        output_file.write(modified_line)
