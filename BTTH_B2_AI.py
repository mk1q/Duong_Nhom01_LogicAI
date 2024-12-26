import itertools
from sympy import symbols, sympify

def parse_expression(expr_str, variables):
    expr_str = expr_str.replace("∨", "|").replace("∧", "&").replace("¬", "~")
    
    expr = sympify(expr_str)
    return expr

def evaluate_expression(expr, variables, values):
    val_dict = {var: values[i] for i, var in enumerate(variables)}
    return expr.subs(val_dict)

def generate_truth_table(expr_str):
    variables = sorted(set(filter(str.isalpha, expr_str)))
    
    expr = parse_expression(expr_str, variables)
    
    truth_values = list(itertools.product([True, False], repeat=len(variables)))
    
    print("  ".join(variables) + "  Kết quả")
    print("-" * (len(variables) * 3 + 10))
    
    for values in truth_values:
        result = evaluate_expression(expr, variables, values)
        result_val = 'T' if result else 'F'
        
        row = "  ".join('T' if v else 'F' for v in values)
        print(f"{row}  {result_val}")

if __name__ == "__main__":
    expr_str = input("Nhập biểu thức logic: ")
    
    generate_truth_table(expr_str)
