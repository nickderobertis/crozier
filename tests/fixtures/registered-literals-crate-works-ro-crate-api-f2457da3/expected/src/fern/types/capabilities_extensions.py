

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .segments_capability import SegmentsCapability


class CapabilitiesExtensions(UniversalBaseModel):
    """
    The registered extensions this implementation provides, as a map of extension identifier to a details object describing how the extension is provided. Presence of a key means the extension is implemented; the value is an empty object when the extension has no extra details to communicate.

    Unregistered experimental extensions use an `x-` prefixed identifier and are outside the scope of this specification.
    """

    segments: typing.Optional[SegmentsCapability] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
