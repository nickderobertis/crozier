

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .catalog_custom_model_provider_type import CatalogCustomModelProviderType
from .reasoning_effort import ReasoningEffort


class CatalogCustomModelProvider(UniversalBaseModel):
    supported_reasoning_efforts: typing.List[ReasoningEffort] = pydantic.Field()
    """
    Supported reasoning-effort values for this provider
    """

    type: CatalogCustomModelProviderType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
