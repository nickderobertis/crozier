

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .sync_result_report import SyncResultReport


class SyncResult(UniversalBaseModel):
    """
    The result of a synchronisation, split into added, edited, skipped and failed.
    """

    report: typing.Optional[SyncResultReport] = None
    added: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    edited: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    skipped: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    errors: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
