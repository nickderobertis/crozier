

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .provider import Provider


class ProviderCollection(UniversalBaseModel):
    """
    Collection of providers.

    *New in version 2.1.0*
    """

    providers: typing.Optional[typing.List[Provider]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
