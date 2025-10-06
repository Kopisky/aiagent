import os

def get_files_info(working_directory, directory="."):
    working_path = os.path.abspath(working_directory)
    full_path = os.path.abspath(os.path.join(working_directory, directory))

    if not full_path.startswith(working_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'
    
    try:
        lis = []
        for file in os.listdir(full_path):
            filepath = os.path.join(full_path, file)
            is_dir = os.path.isdir(filepath)
            size = os.path.getsize(filepath)
            text = f"{file}: file_size={size} bytes, is_dir={is_dir}"
            lis.append(text)
        return "\n".join(lis)
    except Exception as e:
        return f"Error: {e}"

