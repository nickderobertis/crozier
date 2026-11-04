

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .nsd_flavor import NsdFlavor


class Nsd(UniversalBaseModel):
    """
    A NSD
    """

    id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="_id"),
        pydantic.Field(alias="_id", description="The id on the SM Database"),
    ] = None
    """
    The id on the SM Database
    """

    nfvo_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the NFVO where the NSD is onboarded
    """

    nsd_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    The id of the NSD as it is stored in the NFVO
    """

    nsd_name: typing.Optional[str] = pydantic.Field(default=None)
    """
    The name of the NSD as it is stored in the NFVO
    """

    vnfd_list: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    The list of VNFDs in the NSD
    """

    flavor: typing.Optional[NsdFlavor] = pydantic.Field(default=None)
    """
    Total resource requirements for the NSD Deployment
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
