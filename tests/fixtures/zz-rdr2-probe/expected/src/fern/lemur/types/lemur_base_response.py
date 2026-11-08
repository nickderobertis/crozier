

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .lemur_usage import LemurUsage


class LemurBaseResponse(UniversalBaseModel):
    request_id: str = pydantic.Field()
    """
    The ID of the LeMUR request
    """

    usage: LemurUsage = pydantic.Field()
    """
    The usage numbers for the LeMUR request
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
