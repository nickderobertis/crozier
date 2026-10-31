

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .wpt_feature_data import WptFeatureData


class FeatureWptSnapshots(UniversalBaseModel):
    stable: typing.Optional[typing.Dict[str, WptFeatureData]] = pydantic.Field(default=None)
    """
    Contains snapshot of the stable WPT data. The keys for the object comes from the different cases in https://github.com/web-platform-tests/wpt.fyi/blob/fb5bae7c6d04563864ef1c28a263a0a8d6637c4e/shared/product_spec.go#L71-L104
    """

    experimental: typing.Optional[typing.Dict[str, WptFeatureData]] = pydantic.Field(default=None)
    """
    Contains snapshot of the experimental WPT data. The keys for the object comes from the different cases in https://github.com/web-platform-tests/wpt.fyi/blob/fb5bae7c6d04563864ef1c28a263a0a8d6637c4e/shared/product_spec.go#L71-L104
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
