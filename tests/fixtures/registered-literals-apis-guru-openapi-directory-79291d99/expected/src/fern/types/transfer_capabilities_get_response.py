

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .institution_supported_networks import InstitutionSupportedNetworks
from .request_id import RequestId


class TransferCapabilitiesGetResponse(UniversalBaseModel):
    """
    Defines the response schema for `/transfer/capabilities/get`
    """

    institution_supported_networks: InstitutionSupportedNetworks
    request_id: RequestId

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
