import os


def get_files_info(working_directory, directory="."):
    output = f"Result for '{'current' if directory == '.' else directory }' directory\n"
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if not os.path.isdir(target_dir):
            raise NotADirectoryError(f'Error: "{directory} is not a directory')

        if not valid_target_dir:
            raise ValueError(
                f"Error: Cannot list \"{directory}\" as it is outside the permitted working directory")

        for filename in os.listdir(target_dir):
            file_path = os.path.join(target_dir, filename)
            output += f"- {filename}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}\n"

    except Exception as e:
        output += f"{e}"
    finally:
        print(output)
