

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class Permission(enum.StrEnum):
    """
    Permissions:
      * `*` - all permissions are granted
      * `list` - list items is allowed
      * `download` - download files is allowed
      * `upload` - upload files is allowed
      * `overwrite` - overwrite an existing file, while uploading, is allowed. upload permission is required to allow file overwrite
      * `delete` - delete files or directories is allowed
      * `delete_files` - delete files is allowed
      * `delete_dirs` - delete directories is allowed
      * `rename` - rename files or directories is allowed
      * `rename_files` - rename files is allowed
      * `rename_dirs` - rename directories is allowed
      * `create_dirs` - create directories is allowed
      * `create_symlinks` - create links is allowed
      * `chmod` changing file or directory permissions is allowed
      * `chown` changing file or directory owner and group is allowed
      * `chtimes` changing file or directory access and modification time is allowed
      * `copy`, copying files or directories is allowed
    """

    ALL = "*"
    LIST = "list"
    DOWNLOAD = "download"
    UPLOAD = "upload"
    OVERWRITE = "overwrite"
    DELETE = "delete"
    DELETE_FILES = "delete_files"
    DELETE_DIRS = "delete_dirs"
    RENAME = "rename"
    RENAME_FILES = "rename_files"
    RENAME_DIRS = "rename_dirs"
    CREATE_DIRS = "create_dirs"
    CREATE_SYMLINKS = "create_symlinks"
    CHMOD = "chmod"
    CHOWN = "chown"
    CHTIMES = "chtimes"
    COPY = "copy"

    def visit(
        self,
        all_: typing.Callable[[], T_Result],
        list_: typing.Callable[[], T_Result],
        download: typing.Callable[[], T_Result],
        upload: typing.Callable[[], T_Result],
        overwrite: typing.Callable[[], T_Result],
        delete: typing.Callable[[], T_Result],
        delete_files: typing.Callable[[], T_Result],
        delete_dirs: typing.Callable[[], T_Result],
        rename: typing.Callable[[], T_Result],
        rename_files: typing.Callable[[], T_Result],
        rename_dirs: typing.Callable[[], T_Result],
        create_dirs: typing.Callable[[], T_Result],
        create_symlinks: typing.Callable[[], T_Result],
        chmod: typing.Callable[[], T_Result],
        chown: typing.Callable[[], T_Result],
        chtimes: typing.Callable[[], T_Result],
        copy: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is Permission.ALL:
            return all_()
        if self is Permission.LIST:
            return list_()
        if self is Permission.DOWNLOAD:
            return download()
        if self is Permission.UPLOAD:
            return upload()
        if self is Permission.OVERWRITE:
            return overwrite()
        if self is Permission.DELETE:
            return delete()
        if self is Permission.DELETE_FILES:
            return delete_files()
        if self is Permission.DELETE_DIRS:
            return delete_dirs()
        if self is Permission.RENAME:
            return rename()
        if self is Permission.RENAME_FILES:
            return rename_files()
        if self is Permission.RENAME_DIRS:
            return rename_dirs()
        if self is Permission.CREATE_DIRS:
            return create_dirs()
        if self is Permission.CREATE_SYMLINKS:
            return create_symlinks()
        if self is Permission.CHMOD:
            return chmod()
        if self is Permission.CHOWN:
            return chown()
        if self is Permission.CHTIMES:
            return chtimes()
        if self is Permission.COPY:
            return copy()
