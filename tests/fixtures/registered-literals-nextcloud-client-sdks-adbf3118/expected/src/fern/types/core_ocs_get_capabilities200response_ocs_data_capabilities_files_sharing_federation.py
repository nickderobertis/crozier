

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_user_expire_date import (
    CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingUserExpireDate,
)


class CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingFederation(UniversalBaseModel):
    outgoing: bool
    incoming: bool
    expire_date: CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingUserExpireDate
    expire_date_supported: CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingUserExpireDate

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
