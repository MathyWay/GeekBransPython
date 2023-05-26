def print_operation_table(operation, num_rows=6, num_columns=6):
    for a in range(1, num_columns+1):
        print(*[operation(a, x) for x in range(1, num_rows+1)])