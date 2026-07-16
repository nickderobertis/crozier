

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .change_set_hook_target_details_resource_target_details import ChangeSetHookTargetDetailsResourceTargetDetails
from .change_set_hook_target_details_target_type import ChangeSetHookTargetDetailsTargetType


class ChangeSetHookTargetDetails(UniversalBaseModel):
    """
    Specifies details about the target that the hook will run against.
    """

    target_type: typing_extensions.Annotated[
        typing.Optional[ChangeSetHookTargetDetailsTargetType], FieldMetadata(alias="TargetType")
    ] = pydantic.Field(default=None)
    """
    The name of the type.
    """

    resource_target_details: typing_extensions.Annotated[
        typing.Optional[ChangeSetHookTargetDetailsResourceTargetDetails], FieldMetadata(alias="ResourceTargetDetails")
    ] = pydantic.Field(default=None)
    """
    Required if <code>TargetType</code> is <code>RESOURCE</code>.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
