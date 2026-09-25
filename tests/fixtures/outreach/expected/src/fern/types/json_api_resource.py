

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .json_api_resource_links import JsonApiResourceLinks


class JsonApiResource(UniversalBaseModel):
    type: typing.Optional[str] = None
    id: typing.Optional[int] = None
    attributes: typing.Optional[typing.Dict[str, typing.Any]] = None
    relationships: typing.Optional[typing.Dict[str, typing.Any]] = None
    links: typing.Optional[JsonApiResourceLinks] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
