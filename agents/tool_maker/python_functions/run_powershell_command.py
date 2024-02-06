
import subprocess
import json

def run_powershell_command(command):
    """
    Execute a Powershell command to list Python and JavaScript files in the specified
    directory for AST analysis.

    Args:
    - command (str): The Powershell command to be executed.

    Returns:
    - list[str]: A list of file paths that are Python or JavaScript files.
    """
    try:
        # Run the Powershell command
        result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True, check=True)
        
        # Parse and return the command output, assuming the output is a JSON list of strings
        return json.loads(result.stdout)
    except (subprocess.CalledProcessError, json.JSONDecodeError) as e:
        raise RuntimeError(f"Error executing the command or parsing the output: {e}")
