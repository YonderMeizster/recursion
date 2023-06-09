from os import scandir, chdir, getcwd, path


def _get_all_files(curr_dir, files):
    directories = []
    with scandir(curr_dir) as files_and_dirs:
        for i in files_and_dirs:
            if i.is_file():
                files.append(i.name)
                continue
            directories.append(i.name)

    for dir in directories:
        chdir(curr_dir)
        founded_files = []
        files += _get_all_files(path.abspath(dir), founded_files)

    return files


def get_all_files(dir):
    files = []
    backup_cur_dir = getcwd()
    _get_all_files(dir, files)
    chdir(backup_cur_dir)
    return files
