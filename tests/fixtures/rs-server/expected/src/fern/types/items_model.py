

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .items_model_value import ItemsModelValue


class ItemsModel(UniversalBaseModel):
    """
    Model for items containing either a value corresponding to a FeatureCollectionModel or a link
    """

    href: typing.Optional[str] = None
    value: typing.Optional[ItemsModelValue] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
