

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_federation import (
    CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingFederation,
)
from .core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_group import (
    CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingGroup,
)
from .core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_public import (
    CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingPublic,
)
from .core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_sharee import (
    CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingSharee,
)
from .core_ocs_get_capabilities200response_ocs_data_capabilities_files_sharing_user import (
    CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingUser,
)


class CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharing(UniversalBaseModel):
    api_enabled: bool
    public: CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingPublic
    user: CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingUser
    resharing: bool
    group_sharing: typing.Optional[bool] = None
    group: typing.Optional[CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingGroup] = None
    default_permissions: typing.Optional[int] = None
    federation: CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingFederation
    sharee: CoreOcsGetCapabilities200ResponseOcsDataCapabilitiesFilesSharingSharee

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
