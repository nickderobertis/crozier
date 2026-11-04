

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Metadata(UniversalBaseModel):
    """
    User-defined metadata
    """

    tags: typing.Optional[typing.Dict[str, typing.List[str]]] = None
    properties: typing.Optional[typing.Dict[str, str]] = None
    sensitive: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
