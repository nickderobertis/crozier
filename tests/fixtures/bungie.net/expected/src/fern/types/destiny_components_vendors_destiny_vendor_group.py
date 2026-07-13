

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class DestinyComponentsVendorsDestinyVendorGroup(UniversalBaseModel):
    """
    Represents a specific group of vendors that can be rendered in the recommended order.
    How do we figure out this order? It's a long story, and will likely get more complicated over time.
    """

    vendor_group_hash: typing_extensions.Annotated[typing.Optional[int], FieldMetadata(alias="vendorGroupHash")] = None
    vendor_hashes: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="vendorHashes")
    ] = pydantic.Field(default=None)
    """
    The ordered list of vendors within a particular group.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
