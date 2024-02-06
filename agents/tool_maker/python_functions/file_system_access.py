
import os
import json

def file_system_access(action, path, content=None, recursive=False):
    """
    A tool to access, read, write, and manage files on the user's file system.
    
    Parameters:
        action (str): The action to perform. Options: 'read', 'write', 'delete', 'list'.
        path (str): The path to the file or directory.
        content (str, optional): The content to write to the file. Required if action is 'write'.
        recursive (bool, optional): Flag to perform the action recursively. Relevant for 'list' or 'delete'.

    Returns:
        dict: A dictionary with the outcome of the action performed, can contain 'content', 'files', 'error'.
    """
    try:
        if action == 'read':
            if os.path.isfile(path):
                with open(path, 'r') as file:
                    content = file.read()
                return {'content': content}
            else:
                raise FileNotFoundError(f"No such file: {path}")
            
        elif action == 'write':
            if content is None:
                raise ValueError("Content must be provided for write action")
            with open(path, 'w') as file:
                file.write(content)
            return {'message': f"Content written to {path}"}
            
        elif action == 'delete':
            if os.path.isdir(path) and recursive:
                os.rmdir(path)
            elif os.path.isfile(path):
                os.remove(path)
            else:
                raise FileNotFoundError(f"No such file or directory: {path}")
            return {'message': f"{path} has been deleted"}
        
        elif action == 'list':
            if os.path.isdir(path):
                files = os.listdir(path) if not recursive else [os.path.join(dp, f) for dp, dn, filenames in os.walk(path) for f in filenames]
                return {'files': files}
            else:
                raise FileNotFoundError(f"No such directory: {path}")
        
        else:
            raise ValueError("Invalid action specified")
            
    except Exception as e:
        return {'error': str(e)}

