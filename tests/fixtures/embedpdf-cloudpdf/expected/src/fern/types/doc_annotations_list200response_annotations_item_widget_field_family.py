

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class DocAnnotationsList200ResponseAnnotationsItemWidgetFieldFamily(enum.StrEnum):
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
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetFieldFamily.TEXT:
            return text()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetFieldFamily.CHECKBOX:
            return checkbox()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetFieldFamily.RADIO:
            return radio()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetFieldFamily.COMBOBOX:
            return combobox()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetFieldFamily.LISTBOX:
            return listbox()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetFieldFamily.PUSHBUTTON:
            return pushbutton()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetFieldFamily.SIGNATURE:
            return signature()
        if self is DocAnnotationsList200ResponseAnnotationsItemWidgetFieldFamily.UNKNOWN:
            return unknown()
