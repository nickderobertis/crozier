

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .tea_server_info import TeaServerInfo
from .uuid_ import Uuid


class DiscoveryInfo(UniversalBaseModel):
    """
    Discovery information for a TEI
    """

    product_release_uuid: typing_extensions.Annotated[
        Uuid,
        FieldMetadata(alias="productReleaseUuid"),
        pydantic.Field(alias="productReleaseUuid", description="UUID of the resolved TEA Product Release"),
    ]
    """
    UUID of the resolved TEA Product Release
    """

    servers: typing.List[TeaServerInfo] = pydantic.Field()
    """
    Array of TEA server information
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
