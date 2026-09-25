

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .history_model_status import HistoryModelStatus


class HistoryModel(UniversalBaseModel):
    """
    Model for History
    """

    reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    Reason
    """

    status: typing.Optional[HistoryModelStatus] = pydantic.Field(default=None)
    """
    Status
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
