

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .items_model import ItemsModel


class InputModel(UniversalBaseModel):
    """
    Model for input data.

    This model encapsulates the input information, including a collection of features,
    metadata.

    Attributes:
        collection (CollectionModel): The collection of metadata for the input.
        items (FeatureCollectionModel or link): A collection of features (or a link) related to the input.
        asset_names (set[str]): An optional set to keep only selected asset names.
                                If not provided, all assets are staged.
    """

    collection: str
    items: ItemsModel
    asset_names: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
