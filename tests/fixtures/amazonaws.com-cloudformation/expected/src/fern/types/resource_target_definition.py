

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .resource_target_definition_attribute import ResourceTargetDefinitionAttribute
from .resource_target_definition_requires_recreation import ResourceTargetDefinitionRequiresRecreation


class ResourceTargetDefinition(UniversalBaseModel):
    """
    The field that CloudFormation will change, such as the name of a resource's property, and whether the resource will be recreated.
    """

    attribute: typing_extensions.Annotated[
        typing.Optional[ResourceTargetDefinitionAttribute],
        FieldMetadata(alias="Attribute"),
        pydantic.Field(
            alias="Attribute",
            description="Indicates which resource attribute is triggering this update, such as a change in the resource attribute's <code>Metadata</code>, <code>Properties</code>, or <code>Tags</code>.",
        ),
    ] = None
    """
    Indicates which resource attribute is triggering this update, such as a change in the resource attribute's <code>Metadata</code>, <code>Properties</code>, or <code>Tags</code>.
    """

    name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Name"),
        pydantic.Field(
            alias="Name",
            description="If the <code>Attribute</code> value is <code>Properties</code>, the name of the property. For all other attributes, the value is null.",
        ),
    ] = None
    """
    If the <code>Attribute</code> value is <code>Properties</code>, the name of the property. For all other attributes, the value is null.
    """

    requires_recreation: typing_extensions.Annotated[
        typing.Optional[ResourceTargetDefinitionRequiresRecreation],
        FieldMetadata(alias="RequiresRecreation"),
        pydantic.Field(
            alias="RequiresRecreation",
            description='If the <code>Attribute</code> value is <code>Properties</code>, indicates whether a change to this property causes the resource to be recreated. The value can be <code>Never</code>, <code>Always</code>, or <code>Conditionally</code>. To determine the conditions for a <code>Conditionally</code> recreation, see the update behavior for that <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html">property</a> in the CloudFormation User Guide.',
        ),
    ] = None
    """
    If the <code>Attribute</code> value is <code>Properties</code>, indicates whether a change to this property causes the resource to be recreated. The value can be <code>Never</code>, <code>Always</code>, or <code>Conditionally</code>. To determine the conditions for a <code>Conditionally</code> recreation, see the update behavior for that <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html">property</a> in the CloudFormation User Guide.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
