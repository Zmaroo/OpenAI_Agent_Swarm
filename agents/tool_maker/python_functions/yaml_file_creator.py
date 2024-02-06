
import yaml
import os

def yaml_file_creator(tool_name, description, schema):
    """
    A tool that creates a .yaml file for a specified tool based on provided specifications
    including tool name, description, and JSON schema.
    
    :param tool_name: Name of the tool.
    :type tool_name: str
    :param description: Description of the tool.
    :type description: str
    :param schema: JSON schema of the tool.
    :type schema: dict
    :return: Path to the created .yaml file.
    """
    # Combine the tool name, description, and schema into a dictionary
    tool_info = {
        'tool': {
            'name': tool_name,
            'description': description,
            'schema': schema
        }
    }
    
    # The name of the yaml file to be created
    filename = f'{tool_name.replace(" ", "_").lower()}.yaml'
    filepath = os.path.join('/mnt/data', filename)
    
    # Serializing the dictionary into a YAML string
    yaml_content = yaml.dump(tool_info, default_flow_style=False, sort_keys=False)
    
    # Write the YAML string to a file
    with open(filepath, 'w') as file:
        file.write(yaml_content)
    
    # Return the path to the created YAML file
    return filepath
