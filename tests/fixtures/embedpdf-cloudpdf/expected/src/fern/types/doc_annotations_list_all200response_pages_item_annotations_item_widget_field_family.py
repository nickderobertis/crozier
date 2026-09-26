

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetFieldFamily(enum.StrEnum):
    TEXT = "text"
    CHECKBOX = "checkbox"
    RADIO = "radio"
    COMBOBOX = "combobox"
    LISTBOX = "listbox"
    PUSHBUTTON = "pushbutton"
    SIGNATURE = "signature"
    UNKNOWN = "unknown"

    def visit(
        self,
        text: typing.Callable[[], T_Result],
        checkbox: typing.Callable[[], T_Result],
        radio: typing.Callable[[], T_Result],
        combobox: typing.Callable[[], T_Result],
        listbox: typing.Callable[[], T_Result],
        pushbutton: typing.Callable[[], T_Result],
        signature: typing.Callable[[], T_Result],
        unknown: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetFieldFamily.TEXT:
            return text()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetFieldFamily.CHECKBOX:
            return checkbox()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetFieldFamily.RADIO:
            return radio()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetFieldFamily.COMBOBOX:
            return combobox()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetFieldFamily.LISTBOX:
            return listbox()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetFieldFamily.PUSHBUTTON:
            return pushbutton()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetFieldFamily.SIGNATURE:
            return signature()
        if self is DocAnnotationsListAll200ResponsePagesItemAnnotationsItemWidgetFieldFamily.UNKNOWN:
            return unknown()
