

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .benchling_app_manifest_feature_canvas_locations import BenchlingAppManifestFeatureCanvasLocations
from .benchling_app_manifest_features_item_type import BenchlingAppManifestFeaturesItemType


class BenchlingAppManifestFeaturesItem(UniversalBaseModel):
    """
    A feature allows an App to bidirectionally communicate with users through a Canvas
    """

    id: str = pydantic.Field()
    """
    User-defined identifier of feature. Must be unique within a single app's manifest.
    """

    locations: typing.Optional[typing.List[BenchlingAppManifestFeatureCanvasLocations]] = pydantic.Field(default=None)
    """
    Only supported when feature type is CANVAS. The locations where the canvas feature should be available.
    """

    name: str
    type: BenchlingAppManifestFeaturesItemType = pydantic.Field()
    """
    The feature type controls where in the UI a Canvas associated with this feature is rendered.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
