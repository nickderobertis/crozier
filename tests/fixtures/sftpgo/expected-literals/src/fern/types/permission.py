

import typing

Permission = typing.Union[
    typing.Literal[
        "*",
        "list",
        "download",
        "upload",
        "overwrite",
        "delete",
        "delete_files",
        "delete_dirs",
        "rename",
        "rename_files",
        "rename_dirs",
        "create_dirs",
        "create_symlinks",
        "chmod",
        "chown",
        "chtimes",
        "copy",
    ],
    typing.Any,
]
