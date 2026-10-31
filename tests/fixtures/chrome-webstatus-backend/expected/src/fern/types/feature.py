

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .baseline_info import BaselineInfo
from .browser_implementation import BrowserImplementation
from .browser_usage import BrowserUsage
from .feature_developer_signals import FeatureDeveloperSignals
from .feature_discouraged_info import FeatureDiscouragedInfo
from .feature_spec_info import FeatureSpecInfo
from .feature_wpt_snapshots import FeatureWptSnapshots
from .vendor_position import VendorPosition


class Feature(UniversalBaseModel):
    feature_id: str
    system_managed_saved_search_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The ID of the system-managed saved search for this feature.
    """

    name: str = pydantic.Field()
    """
    Short name that is intended to be human friendly. Comes from FeatureData's 'name' field in https://github.com/web-platform-dx/web-features/blob/main/schemas/data.schema.json
    """

    spec: typing.Optional[FeatureSpecInfo] = None
    browser_implementations: typing.Optional[typing.Dict[str, BrowserImplementation]] = pydantic.Field(default=None)
    """
    Describes the implementation status of the feature. The keys for the object come from https://github.com/web-platform-dx/web-features/blob/f630e000a15eaff23f41d6b8c4a44cca64a4a7e4/schemas/data.schema.json#L261-L289
    """

    baseline: typing.Optional[BaselineInfo] = None
    usage: typing.Optional[BrowserUsage] = None
    wpt: typing.Optional[FeatureWptSnapshots] = None
    developer_signals: typing.Optional[FeatureDeveloperSignals] = pydantic.Field(default=None)
    """
    The absence of this object means the feature does not have an active issue in https://github.com/web-platform-dx/developer-signals.
    """

    discouraged: typing.Optional[FeatureDiscouragedInfo] = None
    vendor_positions: typing.Optional[typing.List[VendorPosition]] = pydantic.Field(default=None)
    """
    Contains standards positions from various vendors.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
