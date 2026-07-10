# tool: file_stem
# description: Returns the filename without its extension
# author: @tmshnko
# example: file_stem "/home/user/photo.tar.gz" -> "photo.tar"


def run(*args) -> str:
    txt = str(args[0])
    last_slash = txt.rfind('/') + 1
    last_dot = txt.rfind('.') if txt.rfind('.') != -1 else None

    if last_slash == last_dot:
        return txt[last_slash:]
    return txt[last_slash:last_dot]
