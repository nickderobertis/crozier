

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ItemAuthorDto(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Author's name
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of a site owned by the author
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
