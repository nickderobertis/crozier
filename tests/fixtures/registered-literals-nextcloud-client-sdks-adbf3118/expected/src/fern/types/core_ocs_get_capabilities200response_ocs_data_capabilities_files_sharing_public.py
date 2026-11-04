

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_public_expire_date import (
    CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingPublicExpireDate,
)
from .core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_public_password import (
    CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingPublicPassword,
)


class CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingPublic(UniversalBaseModel):
    enabled: bool
    password: typing.Optional[CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingPublicPassword] = None
    multiple_links: typing.Optional[bool] = None
    expire_date: typing.Optional[CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingPublicExpireDate] = (
        None
    )
    expire_date_internal: typing.Optional[
        CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingPublicExpireDate
    ] = None
    expire_date_remote: typing.Optional[
        CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingPublicExpireDate
    ] = None
    send_mail: typing.Optional[bool] = None
    upload: typing.Optional[bool] = None
    upload_files_drop: typing.Optional[bool] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
