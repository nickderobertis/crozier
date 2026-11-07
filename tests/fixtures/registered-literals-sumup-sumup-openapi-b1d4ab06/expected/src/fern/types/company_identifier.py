

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class CompanyIdentifier(UniversalBaseModel):
    ref: str = pydantic.Field()
    """
    The unique reference for the company identifier type as defined in the country SDK.
    """

    value: str = pydantic.Field()
    """
    The company identifier value.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
