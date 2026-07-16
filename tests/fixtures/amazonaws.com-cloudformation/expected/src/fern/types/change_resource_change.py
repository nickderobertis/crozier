

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .change_resource_change_action import ChangeResourceChangeAction
from .change_resource_change_module_info import ChangeResourceChangeModuleInfo
from .change_resource_change_replacement import ChangeResourceChangeReplacement
from .resource_attribute import ResourceAttribute
from .resource_change_detail import ResourceChangeDetail


class ChangeResourceChange(UniversalBaseModel):
    """
    A <code>ResourceChange</code> structure that describes the resource and action that CloudFormation will perform.
    """

    action: typing_extensions.Annotated[typing.Optional[ChangeResourceChangeAction], FieldMetadata(alias="Action")] = (
        pydantic.Field(default=None)
    )
    """
    The action that CloudFormation takes on the resource, such as <code>Add</code> (adds a new resource), <code>Modify</code> (changes a resource), <code>Remove</code> (deletes a resource), <code>Import</code> (imports a resource), or <code>Dynamic</code> (exact action for the resource can't be determined).
    """

    logical_resource_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="LogicalResourceId")] = (
        pydantic.Field(default=None)
    )
    """
    The resource's logical ID, which is defined in the stack's template.
    """

    physical_resource_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="PhysicalResourceId")
    ] = pydantic.Field(default=None)
    """
    The resource's physical ID (resource name). Resources that you are adding don't have physical IDs because they haven't been created.
    """

    resource_type: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ResourceType")] = (
        pydantic.Field(default=None)
    )
    """
    The type of CloudFormation resource, such as <code>AWS::S3::Bucket</code>.
    """

    replacement: typing_extensions.Annotated[
        typing.Optional[ChangeResourceChangeReplacement], FieldMetadata(alias="Replacement")
    ] = pydantic.Field(default=None)
    """
    <p>For the <code>Modify</code> action, indicates whether CloudFormation will replace the resource by creating a new one and deleting the old one. This value depends on the value of the <code>RequiresRecreation</code> property in the <code>ResourceTargetDefinition</code> structure. For example, if the <code>RequiresRecreation</code> field is <code>Always</code> and the <code>Evaluation</code> field is <code>Static</code>, <code>Replacement</code> is <code>True</code>. If the <code>RequiresRecreation</code> field is <code>Always</code> and the <code>Evaluation</code> field is <code>Dynamic</code>, <code>Replacement</code> is <code>Conditionally</code>.</p> <p>If you have multiple changes with different <code>RequiresRecreation</code> values, the <code>Replacement</code> value depends on the change with the most impact. A <code>RequiresRecreation</code> value of <code>Always</code> has the most impact, followed by <code>Conditionally</code>, and then <code>Never</code>.</p>
    """

    scope: typing_extensions.Annotated[
        typing.Optional[typing.List[ResourceAttribute]], FieldMetadata(alias="Scope")
    ] = pydantic.Field(default=None)
    """
    For the <code>Modify</code> action, indicates which resource attribute is triggering this update, such as a change in the resource attribute's <code>Metadata</code>, <code>Properties</code>, or <code>Tags</code>.
    """

    details: typing_extensions.Annotated[
        typing.Optional[typing.List[ResourceChangeDetail]], FieldMetadata(alias="Details")
    ] = pydantic.Field(default=None)
    """
    For the <code>Modify</code> action, a list of <code>ResourceChangeDetail</code> structures that describes the changes that CloudFormation will make to the resource.
    """

    change_set_id: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="ChangeSetId")] = (
        pydantic.Field(default=None)
    )
    """
    The change set ID of the nested change set.
    """

    module_info: typing_extensions.Annotated[
        typing.Optional[ChangeResourceChangeModuleInfo], FieldMetadata(alias="ModuleInfo")
    ] = pydantic.Field(default=None)
    """
    Contains information about the module from which the resource was created, if the resource was created from a module included in the stack template.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
