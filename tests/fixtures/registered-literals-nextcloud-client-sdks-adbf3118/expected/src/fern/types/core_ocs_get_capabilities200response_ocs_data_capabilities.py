

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .core_ocs_get_capabilities200response_ocs_data_capabilities_dav import (
    CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesDav,
)
from .core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing import (
    CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharing,
)
from .core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_user_expire_date import (
    CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingUserExpireDate,
)
from .core_ocs_get_capabilities200response_ocs_data_capabilities_ocm import (
    CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesOcm,
)
from .core_ocs_get_capabilities200response_ocs_data_capabilities_provisioning_api import (
    CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesProvisioningApi,
)
from .core_ocs_get_capabilities200response_ocs_data_capabilities_theming import (
    CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesTheming,
)
from .core_ocs_get_capabilities200response_ocs_data_capabilities_user_status import (
    CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesUserStatus,
)


class CoreOcsGetCapabilities200ResponseOcsDataCapabilities(UniversalBaseModel):
    ocm: typing.Optional[CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesOcm] = None
    dav: typing.Optional[CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesDav] = None
    files_sharing: typing.Optional[CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharing] = None
    provisioning_api: typing.Optional[CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesProvisioningApi] = None
    theming: typing.Optional[CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesTheming] = None
    user_status: typing.Optional[CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesUserStatus] = None
    weather_status: typing.Optional[CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingUserExpireDate] = (
        None
    )

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
