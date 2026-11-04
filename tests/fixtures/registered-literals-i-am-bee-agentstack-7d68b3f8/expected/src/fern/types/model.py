

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .model_object import ModelObject
from .model_provider_info import ModelProviderInfo


class Model(UniversalBaseModel):
    id: str
    created: typing.Optional[int] = None
    object: typing.Optional[ModelObject] = None
    owned_by: typing.Optional[str] = None
    provider: ModelProviderInfo
    display_name: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
