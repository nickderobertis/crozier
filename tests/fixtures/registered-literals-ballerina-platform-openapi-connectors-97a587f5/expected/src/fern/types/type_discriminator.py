

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class TypeDiscriminator(enum.StrEnum):
    """
    Defines the type of an object.
    """

    LIST = "list"
    FINE_TUNE = "fine-tune"
    FILE = "file"
    FINE_TUNE_EVENT = "fine-tune-event"
    MODEL = "model"
    DEPLOYMENT = "deployment"

    def visit(
        self,
        list_: typing.Callable[[], T_Result],
        fine_tune: typing.Callable[[], T_Result],
        file: typing.Callable[[], T_Result],
        fine_tune_event: typing.Callable[[], T_Result],
        model: typing.Callable[[], T_Result],
        deployment: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is TypeDiscriminator.LIST:
            return list_()
        if self is TypeDiscriminator.FINE_TUNE:
            return fine_tune()
        if self is TypeDiscriminator.FILE:
            return file()
        if self is TypeDiscriminator.FINE_TUNE_EVENT:
            return fine_tune_event()
        if self is TypeDiscriminator.MODEL:
            return model()
        if self is TypeDiscriminator.DEPLOYMENT:
            return deployment()
