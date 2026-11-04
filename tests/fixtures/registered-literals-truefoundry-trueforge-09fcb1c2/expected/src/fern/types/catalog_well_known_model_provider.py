

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .catalog_model import CatalogModel
from .catalog_well_known_model_provider_type import CatalogWellKnownModelProviderType


class CatalogWellKnownModelProvider(UniversalBaseModel):
    logo: typing.Optional[str] = pydantic.Field(default=None)
    """
    URL of the provider logo asset
    """

    models: typing.List[CatalogModel] = pydantic.Field()
    """
    Preset models
    """

    type: CatalogWellKnownModelProviderType

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
