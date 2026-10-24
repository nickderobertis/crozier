

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Retention(UniversalBaseModel):
    metadata: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of days to retain metadata
    """

    data: typing.Optional[int] = pydantic.Field(default=None)
    """
    Number of days to retain data
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
