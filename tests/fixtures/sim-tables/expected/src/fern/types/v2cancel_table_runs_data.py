

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V2CancelTableRunsData(UniversalBaseModel):
    """
    Result of canceling in-flight table cell runs.
    """

    cancelled: float = pydantic.Field()
    """
    Number of cell runs canceled.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
