

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class PostApiV1PlayerReleasesUploadResponseDataSource(enum.StrEnum):
    UPLOAD = "upload"
    GITHUB = "github"

    def visit(self, upload: typing.Callable[[], T_Result], github: typing.Callable[[], T_Result]) -> T_Result:
        if self is PostApiV1PlayerReleasesUploadResponseDataSource.UPLOAD:
            return upload()
        if self is PostApiV1PlayerReleasesUploadResponseDataSource.GITHUB:
            return github()
