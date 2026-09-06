

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class UpdateFieldsResponseType(enum.StrEnum):
    """
    Choose these appropriate field type for your collection data
    """

    COLOR = "Color"
    DATE_TIME = "DateTime"
    EMAIL = "Email"
    EXT_FILE_REF = "ExtFileRef"
    FILE = "File"
    IMAGE = "Image"
    LINK = "Link"
    MULTI_IMAGE = "MultiImage"
    MULTI_REFERENCE = "MultiReference"
    NUMBER = "Number"
    OPTION = "Option"
    PHONE = "Phone"
    PLAIN_TEXT = "PlainText"
    REFERENCE = "Reference"
    RICH_TEXT = "RichText"
    SWITCH = "Switch"
    VIDEO_LINK = "VideoLink"

    def visit(
        self,
        color: typing.Callable[[], T_Result],
        date_time: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        ext_file_ref: typing.Callable[[], T_Result],
        file: typing.Callable[[], T_Result],
        image: typing.Callable[[], T_Result],
        link: typing.Callable[[], T_Result],
        multi_image: typing.Callable[[], T_Result],
        multi_reference: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        option: typing.Callable[[], T_Result],
        phone: typing.Callable[[], T_Result],
        plain_text: typing.Callable[[], T_Result],
        reference: typing.Callable[[], T_Result],
        rich_text: typing.Callable[[], T_Result],
        switch: typing.Callable[[], T_Result],
        video_link: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is UpdateFieldsResponseType.COLOR:
            return color()
        if self is UpdateFieldsResponseType.DATE_TIME:
            return date_time()
        if self is UpdateFieldsResponseType.EMAIL:
            return email()
        if self is UpdateFieldsResponseType.EXT_FILE_REF:
            return ext_file_ref()
        if self is UpdateFieldsResponseType.FILE:
            return file()
        if self is UpdateFieldsResponseType.IMAGE:
            return image()
        if self is UpdateFieldsResponseType.LINK:
            return link()
        if self is UpdateFieldsResponseType.MULTI_IMAGE:
            return multi_image()
        if self is UpdateFieldsResponseType.MULTI_REFERENCE:
            return multi_reference()
        if self is UpdateFieldsResponseType.NUMBER:
            return number()
        if self is UpdateFieldsResponseType.OPTION:
            return option()
        if self is UpdateFieldsResponseType.PHONE:
            return phone()
        if self is UpdateFieldsResponseType.PLAIN_TEXT:
            return plain_text()
        if self is UpdateFieldsResponseType.REFERENCE:
            return reference()
        if self is UpdateFieldsResponseType.RICH_TEXT:
            return rich_text()
        if self is UpdateFieldsResponseType.SWITCH:
            return switch()
        if self is UpdateFieldsResponseType.VIDEO_LINK:
            return video_link()
