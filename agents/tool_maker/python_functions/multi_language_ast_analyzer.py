
import ast
import js2py

def multi_language_ast_analyzer(language, code):
    """
    An enhanced version of the python_ast_analyzer that can analyze 
    both Python and JavaScript code for AST (Abstract Syntax Tree) 
    and other metrics.
    
    Parameters:
        language (str): The programming language of the code. Options: 'python', 'javascript'.
        code (str): The source code to analyze.

    Returns:
        dict: A dictionary with the AST representation of the provided code and other metrics.
    """
    if language == 'python':
        try:
            # Parse the Python code into an AST
            tree = ast.parse(code)
            # Convert the AST into a dictionary
            ast_dict = ast.dump(tree, annotate_fields=True, include_attributes=True)
            # You can add additional Python specific metrics if needed
            return {'ast': ast_dict, 'metrics': {}}
        
        except SyntaxError as e:
            return {'error': f'SyntaxError: {e}'}
        
    elif language == 'javascript':
        try:
            # Parse the JavaScript code into an AST using js2py
            js_tree = js2py.parse_js_ast(code)
            # Serialize the AST to a JSON-like structure
            js_ast_dict = js_tree.to_dict()
            # You can add additional JavaScript specific metrics if needed
            return {'ast': js_ast_dict, 'metrics': {}}
        
        except js2py.base.PyJsException as e:
            return {'error': f'PyJsException: {e}'}
        
    else:
        return {'error': 'Unsupported language.'}
