

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .safe_literal_discovery_value_kind import SafeLiteralDiscoveryValueKind


class SafeLiteralDiscoveryValue(UniversalBaseModel):
    """
    Non-sensitive metadata that is safe to send to the frontend.
    """

    kind: SafeLiteralDiscoveryValueKind
    value: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
