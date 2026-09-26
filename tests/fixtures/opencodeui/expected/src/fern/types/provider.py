

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model import Model
from .provider_source import ProviderSource


class Provider(UniversalBaseModel):
    id: str
    name: str
    source: ProviderSource
    env: typing.List[str]
    key: typing.Optional[str] = None
    options: typing.Dict[str, typing.Any]
    models: typing.Dict[str, Model]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
