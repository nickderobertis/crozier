

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ViewDataSearch(UniversalBaseModel):
    filter: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    tag: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    match: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None
    sort: typing.Optional[typing.List[typing.Optional[typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
