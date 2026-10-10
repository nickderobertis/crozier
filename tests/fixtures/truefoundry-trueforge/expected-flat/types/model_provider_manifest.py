

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .configured_model import ConfiguredModel
from .model_provider_auth import ModelProviderAuth
from .resource_name import ResourceName


class ModelProviderManifest_Alibaba(UniversalBaseModel):
    type: typing.Literal["alibaba"] = "alibaba"
    auth: ModelProviderAuth
    base_url: typing.Optional[str] = None
    models: typing.List[ConfiguredModel]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelProviderManifest_Anthropic(UniversalBaseModel):
    type: typing.Literal["anthropic"] = "anthropic"
    auth: ModelProviderAuth
    base_url: typing.Optional[str] = None
    models: typing.List[ConfiguredModel]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelProviderManifest_Custom(UniversalBaseModel):
    type: typing.Literal["custom"] = "custom"
    auth: typing.Optional[ModelProviderAuth] = None
    base_url: str
    models: typing.List[ConfiguredModel]
    name: ResourceName

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelProviderManifest_Fireworks(UniversalBaseModel):
    type: typing.Literal["fireworks"] = "fireworks"
    auth: ModelProviderAuth
    base_url: typing.Optional[str] = None
    models: typing.List[ConfiguredModel]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelProviderManifest_GoogleGemini(UniversalBaseModel):
    type: typing.Literal["google-gemini"] = "google-gemini"
    auth: ModelProviderAuth
    base_url: typing.Optional[str] = None
    models: typing.List[ConfiguredModel]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelProviderManifest_Moonshot(UniversalBaseModel):
    type: typing.Literal["moonshot"] = "moonshot"
    auth: ModelProviderAuth
    base_url: typing.Optional[str] = None
    models: typing.List[ConfiguredModel]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelProviderManifest_Openai(UniversalBaseModel):
    type: typing.Literal["openai"] = "openai"
    auth: ModelProviderAuth
    base_url: typing.Optional[str] = None
    models: typing.List[ConfiguredModel]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelProviderManifest_Together(UniversalBaseModel):
    type: typing.Literal["together"] = "together"
    auth: ModelProviderAuth
    base_url: typing.Optional[str] = None
    models: typing.List[ConfiguredModel]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelProviderManifest_Truefoundry(UniversalBaseModel):
    type: typing.Literal["truefoundry"] = "truefoundry"
    auth: typing.Optional[ModelProviderAuth] = None
    base_url: str
    models: typing.List[ConfiguredModel]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ModelProviderManifest_Zai(UniversalBaseModel):
    type: typing.Literal["zai"] = "zai"
    auth: ModelProviderAuth
    base_url: typing.Optional[str] = None
    models: typing.List[ConfiguredModel]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ModelProviderManifest = typing_extensions.Annotated[
    typing.Union[
        ModelProviderManifest_Alibaba,
        ModelProviderManifest_Anthropic,
        ModelProviderManifest_Custom,
        ModelProviderManifest_Fireworks,
        ModelProviderManifest_GoogleGemini,
        ModelProviderManifest_Moonshot,
        ModelProviderManifest_Openai,
        ModelProviderManifest_Together,
        ModelProviderManifest_Truefoundry,
        ModelProviderManifest_Zai,
    ],
    pydantic.Field(discriminator="type"),
]
