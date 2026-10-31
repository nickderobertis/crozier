

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetMvRomBurnPrecentResponse(UniversalBaseModel):
    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The current state of the update process, where "0" typically indicates that the update is in progress and "1" indicates that the update is complete.
    """

    progress: typing.Optional[str] = pydantic.Field(default=None)
    """
    The progress of the update process as a percentage, ranging from "0" to "100".
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
