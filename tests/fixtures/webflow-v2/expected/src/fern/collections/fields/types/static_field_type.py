

import typing

from ....core import enum

T_Result = typing.TypeVar("T_Result")


class StaticFieldType(enum.StrEnum):
    """
    Choose these appropriate field type for your collection data
    """

    COLOR = "Color"
    DATE_TIME = "DateTime"
    EMAIL = "Email"
    FILE = "File"
    IMAGE = "Image"
    LINK = "Link"
    MULTI_IMAGE = "MultiImage"
    NUMBER = "Number"
    PHONE = "Phone"
    PLAIN_TEXT = "PlainText"
    RICH_TEXT = "RichText"
    SWITCH = "Switch"
    VIDEO_LINK = "VideoLink"

    def visit(
        self,
        color: typing.Callable[[], T_Result],
        date_time: typing.Callable[[], T_Result],
        email: typing.Callable[[], T_Result],
        file: typing.Callable[[], T_Result],
        image: typing.Callable[[], T_Result],
        link: typing.Callable[[], T_Result],
        multi_image: typing.Callable[[], T_Result],
        number: typing.Callable[[], T_Result],
        phone: typing.Callable[[], T_Result],
        plain_text: typing.Callable[[], T_Result],
        rich_text: typing.Callable[[], T_Result],
        switch: typing.Callable[[], T_Result],
        video_link: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is StaticFieldType.COLOR:
            return color()
        if self is StaticFieldType.DATE_TIME:
            return date_time()
        if self is StaticFieldType.EMAIL:
            return email()
        if self is StaticFieldType.FILE:
            return file()
        if self is StaticFieldType.IMAGE:
            return image()
        if self is StaticFieldType.LINK:
            return link()
        if self is StaticFieldType.MULTI_IMAGE:
            return multi_image()
        if self is StaticFieldType.NUMBER:
            return number()
        if self is StaticFieldType.PHONE:
            return phone()
        if self is StaticFieldType.PLAIN_TEXT:
            return plain_text()
        if self is StaticFieldType.RICH_TEXT:
            return rich_text()
        if self is StaticFieldType.SWITCH:
            return switch()
        if self is StaticFieldType.VIDEO_LINK:
            return video_link()
