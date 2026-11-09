

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .affiliate_attribution_source_type import AffiliateAttributionSourceType


class AffiliateAttributionSource(UniversalBaseModel):
    """
    Context about where the attribution originated.
    """

    type: AffiliateAttributionSourceType = pydantic.Field()
    """
    The type of attribution source.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    Canonical content URL when type is 'url'.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
