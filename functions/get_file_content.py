import os

def get_file_content(working_directory, file_path):
    working_path = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not full_path.startswith(working_path):
        return f'Cannot read "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    

    try:
        file_size = os.path.getsize(full_path)
        with open(full_path, "r") as f:
            file_content = f.read(10000)
            if file_size > 10000:
                file_content += f"\n...File '{file_path}' truncated at 10000 characters"
            return file_content
    except Exception as e:
        return f"Error: {e}"