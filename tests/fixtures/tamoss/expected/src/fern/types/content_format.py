

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class ContentFormat(enum.StrEnum):
    """
    Identifies the content format for a Flow or Source using a URN string
    """

    URN_X_NMOS_FORMAT_VIDEO = "urn:x-nmos:format:video"
    URN_X_TAM_FORMAT_IMAGE = "urn:x-tam:format:image"
    URN_X_NMOS_FORMAT_AUDIO = "urn:x-nmos:format:audio"
    URN_X_NMOS_FORMAT_DATA = "urn:x-nmos:format:data"
    URN_X_NMOS_FORMAT_MULTI = "urn:x-nmos:format:multi"

    def visit(
        self,
        urn_x_nmos_format_video: typing.Callable[[], T_Result],
        urn_x_tam_format_image: typing.Callable[[], T_Result],
        urn_x_nmos_format_audio: typing.Callable[[], T_Result],
        urn_x_nmos_format_data: typing.Callable[[], T_Result],
        urn_x_nmos_format_multi: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is ContentFormat.URN_X_NMOS_FORMAT_VIDEO:
            return urn_x_nmos_format_video()
        if self is ContentFormat.URN_X_TAM_FORMAT_IMAGE:
            return urn_x_tam_format_image()
        if self is ContentFormat.URN_X_NMOS_FORMAT_AUDIO:
            return urn_x_nmos_format_audio()
        if self is ContentFormat.URN_X_NMOS_FORMAT_DATA:
            return urn_x_nmos_format_data()
        if self is ContentFormat.URN_X_NMOS_FORMAT_MULTI:
            return urn_x_nmos_format_multi()
