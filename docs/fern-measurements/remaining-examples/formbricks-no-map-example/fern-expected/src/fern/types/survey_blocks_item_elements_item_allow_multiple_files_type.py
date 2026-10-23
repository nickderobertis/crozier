

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SurveyBlocksItemElementsItemAllowMultipleFilesType(enum.StrEnum):
    FILE_UPLOAD = "fileUpload"

    def visit(self, file_upload: typing.Callable[[], T_Result]) -> T_Result:
        if self is SurveyBlocksItemElementsItemAllowMultipleFilesType.FILE_UPLOAD:
            return file_upload()
