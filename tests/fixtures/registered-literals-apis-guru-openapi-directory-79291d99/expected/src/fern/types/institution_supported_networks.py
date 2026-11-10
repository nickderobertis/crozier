

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .transfer_capabilities_get_rtp import TransferCapabilitiesGetRtp


class InstitutionSupportedNetworks(UniversalBaseModel):
    """
    Contains the RTP network and types supported by the linked Item's institution.
    """

    rtp: TransferCapabilitiesGetRtp

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
