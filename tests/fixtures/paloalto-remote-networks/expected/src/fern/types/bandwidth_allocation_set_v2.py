

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .bandwidth_allocation_v2 import BandwidthAllocationV2
from .uuid_response import UuidResponse


class BandwidthAllocationSetV2(UniversalBaseModel):
    bandwidth_allocations: typing.Optional[typing.List[BandwidthAllocationV2]] = pydantic.Field(default=None)
    """
    bandwidth allocations
    """

    uuid_: typing_extensions.Annotated[
        typing.Optional[UuidResponse], FieldMetadata(alias="uuid"), pydantic.Field(alias="uuid")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
