

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PutListingsSlugRequestLocation(UniversalBaseModel):
    country_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Ex: US
    """

    locality: typing.Optional[str] = pydantic.Field(default=None)
    """
    Ex: Chicago
    """

    region: typing.Optional[str] = pydantic.Field(default=None)
    """
    Ex: IL
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
