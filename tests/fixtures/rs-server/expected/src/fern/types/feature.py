

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .asset import Asset
from .feature_bbox_item import FeatureBboxItem
from .links import Links


class Feature(UniversalBaseModel):
    """
    Custom model for a STAC (SpatioTemporal Asset Catalog) feature.

    This model defines a STAC feature without restrictions on the bounding box (`bbox`)
    and links. It is designed to store geographic and metadata information about a
    specific feature.

    Attributes:
        type (str): The type of the feature (e.g., "Feature").
        geometry (Optional[dict]): The geometry of the feature, represented as a
            dictionary (e.g., GeoJSON). Defaults to None.
        properties (Dict[str, str]): A dictionary of feature properties, where keys
            represent property names and values are the corresponding values.
        bbox (Optional[List[Union[int, float]]]): A bounding box defining the feature's
            spatial extent. It supports both integer and float values. Defaults to None.
        id (str): The unique identifier for the feature.
        stac_version (str): The version of the STAC specification used.
        assets (Dict[str, Asset]): A dictionary of assets associated with the feature.
            Keys are asset names, and values are `Asset` objects.
        links (Optional[Links]): A list of links related to the feature. Defaults to None.
        stac_extensions (List[str]): A list of STAC extension URIs used in this feature.
    """

    type: str
    geometry: typing.Optional[typing.Dict[str, typing.Any]] = None
    properties: typing.Dict[str, typing.Any]
    bbox: typing.Optional[typing.List[FeatureBboxItem]] = None
    id: str
    stac_version: str
    assets: typing.Dict[str, Asset]
    links: typing.Optional[Links] = None
    stac_extensions: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
