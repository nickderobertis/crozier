

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GetPhpInfoLoadedExtensionsItem(UniversalBaseModel):
    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name of the loaded extension
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    Version of the loaded extension
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
