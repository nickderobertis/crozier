

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class DocumentsInitRequestUploadPreference(enum.StrEnum):
    AUTO = "auto"
    PRESIGNED = "presigned"
    PROXY = "proxy"

    def visit(
        self,
        auto: typing.Callable[[], T_Result],
        presigned: typing.Callable[[], T_Result],
        proxy: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocumentsInitRequestUploadPreference.AUTO:
            return auto()
        if self is DocumentsInitRequestUploadPreference.PRESIGNED:
            return presigned()
        if self is DocumentsInitRequestUploadPreference.PROXY:
            return proxy()
