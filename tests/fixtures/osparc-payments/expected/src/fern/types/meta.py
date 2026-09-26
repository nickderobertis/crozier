

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Meta(UniversalBaseModel):
    name: str
    version: str
    released: typing.Optional[typing.Dict[str, typing.Optional[str]]] = pydantic.Field(default=None)
    """
    Maps every route's path tag with a released version
    """

    docs_url: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
