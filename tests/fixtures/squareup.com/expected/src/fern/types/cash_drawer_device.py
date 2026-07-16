

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CashDrawerDevice(UniversalBaseModel):
    """ """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The device Square-issued ID
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The device merchant-specified name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
