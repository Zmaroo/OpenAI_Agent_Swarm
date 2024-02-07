
def vscode_powershell_terminal(command):
    """
    A tool that executes PowerShell terminal commands in a VS Code-like environment and returns the output.
    
    Parameters:
    command (str): The PowerShell command to be executed.
    
    Returns:
    The output of the executed command.
    """
    
    
    import subprocess
    result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else result.stderr
    
