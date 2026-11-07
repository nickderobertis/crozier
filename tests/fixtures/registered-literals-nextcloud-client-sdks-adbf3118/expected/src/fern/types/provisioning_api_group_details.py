

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .provisioning_api_group_details_usercount import ProvisioningApiGroupDetailsUsercount


class ProvisioningApiGroupDetails(UniversalBaseModel):
    id: str
    displayname: str
    usercount: ProvisioningApiGroupDetailsUsercount
    disabled: ProvisioningApiGroupDetailsUsercount
    can_add: typing_extensions.Annotated[bool, FieldMetadata(alias="canAdd"), pydantic.Field(alias="canAdd")]
    can_remove: typing_extensions.Annotated[bool, FieldMetadata(alias="canRemove"), pydantic.Field(alias="canRemove")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
