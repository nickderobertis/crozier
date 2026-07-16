

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .change_set_hook_resource_target_details_resource_action import ChangeSetHookResourceTargetDetailsResourceAction


class ChangeSetHookResourceTargetDetails(UniversalBaseModel):
    """
    Specifies <code>RESOURCE</code> type target details for activated hooks.
    """

    logical_resource_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="LogicalResourceId")] = (
        pydantic.Field(default=None)
    )
    """
    The resource's logical ID, which is defined in the stack's template.
    """

    resource_type: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ResourceType")] = (
        pydantic.Field(default=None)
    )
    """
    The type of CloudFormation resource, such as <code>AWS::S3::Bucket</code>.
    """

    resource_action: typing_extensions.Annotated[
        typing.Optional[ChangeSetHookResourceTargetDetailsResourceAction], FieldMetadata(alias="ResourceAction")
    ] = pydantic.Field(default=None)
    """
    Specifies the action of the resource.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
