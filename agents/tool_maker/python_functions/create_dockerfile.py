
def create_dockerfile(project_path, base_image, install_commands, cmd, expose_port=8000, copy_commands=None, workdir=None):
    """
    Create a Dockerfile for a project with port 8000 exposed.

    :param project_path: The path where the project is located.
    :param base_image: The base image to use in the Dockerfile.
    :param install_commands: A list of shell commands to run to set up the project.
    :param cmd: The command that runs the application.
    :param expose_port: The port to expose from the container. Defaults to 8000.
    :param copy_commands: Optional. A list of shell commands to copy files into the image.
    :param workdir: Optional. The working directory inside the image.
    """

    dockerfile_content = f"FROM {base_image}\n"

    if workdir:
        dockerfile_content += f"WORKDIR {workdir}\n"

    # Assume copy_commands are formatted as "source destination".
    if copy_commands:
        for command in copy_commands:
            dockerfile_content += f"COPY {command}\n"

    for command in install_commands:
        dockerfile_content += f"RUN {command}\n"

    dockerfile_content += f"EXPOSE {expose_port}\n"
    dockerfile_content += f"CMD {cmd}\n"

    # Assumes that there is write permission at the project_path.
    with open(f"{project_path}/Dockerfile", 'w') as f:
        f.write(dockerfile_content)

    return f"Dockerfile created at {project_path}/Dockerfile."
