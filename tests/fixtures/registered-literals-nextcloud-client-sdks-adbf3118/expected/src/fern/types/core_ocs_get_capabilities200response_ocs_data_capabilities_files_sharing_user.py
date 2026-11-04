

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_user_expire_date import (
    CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingUserExpireDate,
)


class CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingUser(UniversalBaseModel):
    send_mail: bool
    expire_date: typing.Optional[CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingUserExpireDate] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
