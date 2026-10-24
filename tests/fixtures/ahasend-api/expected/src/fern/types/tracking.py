

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Tracking(UniversalBaseModel):
    open: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to track opens
    """

    click: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether to track clicks
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
