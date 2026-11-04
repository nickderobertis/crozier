

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .nsi_ns_list_item_nsd_info_flavor import NsiNsListItemNsdInfoFlavor


class NsiNsListItemNsdInfo(UniversalBaseModel):
    """
    Information about the NS Descriptor
    """

    id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="_id"), pydantic.Field(alias="_id")] = (
        None
    )
    id: typing.Optional[str] = None
    vnfd_list: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The list of VNFDs in the NSD
    """

    flavor: typing.Optional[NsiNsListItemNsdInfoFlavor] = pydantic.Field(default=None)
    """
    The NS requirements
    """

    nfvo_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nfvo-id"), pydantic.Field(alias="nfvo-id")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
