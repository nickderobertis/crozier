

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PartialCollection(UniversalBaseModel):
    """
    Partial STAC Collection.
    """

    type: typing.Optional[str] = None
    stac_version: typing.Optional[str] = None
    stac_extensions: typing.Optional[typing.List[str]] = None
    id: typing.Optional[str] = None
    title: typing.Optional[str] = None
    description: typing.Optional[str] = None
    links: typing.Optional[typing.Dict[str, typing.Any]] = None
    keywords: typing.Optional[typing.List[str]] = None
    license: typing.Optional[str] = None
    providers: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None
    extent: typing.Optional[typing.Dict[str, typing.Any]] = None
    summaries: typing.Optional[typing.Dict[str, typing.Any]] = None
    assets: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
