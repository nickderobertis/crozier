

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .capability import Capability
from .parameter_declaration import ParameterDeclaration
from .resource_identifier_summary import ResourceIdentifierSummary
from .resource_type import ResourceType
from .transform_name import TransformName


class GetTemplateSummaryOutput(UniversalBaseModel):
    """
    The output for the <a>GetTemplateSummary</a> action.
    """

    parameters: typing_extensions.Annotated[
        typing.Optional[typing.List[ParameterDeclaration]], FieldMetadata(alias="Parameters")
    ] = pydantic.Field(default=None)
    """
    A list of parameter declarations that describe various properties for each parameter.
    """

    description: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Description")] = pydantic.Field(
        default=None
    )
    """
    The value that's defined in the <code>Description</code> property of the template.
    """

    capabilities: typing_extensions.Annotated[
        typing.Optional[typing.List[Capability]], FieldMetadata(alias="Capabilities")
    ] = pydantic.Field(default=None)
    """
    <p>The capabilities found within the template. If your template contains IAM resources, you must specify the <code>CAPABILITY_IAM</code> or <code>CAPABILITY_NAMED_IAM</code> value for this parameter when you use the <a>CreateStack</a> or <a>UpdateStack</a> actions with your template; otherwise, those actions return an <code>InsufficientCapabilities</code> error.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-template.html#capabilities">Acknowledging IAM Resources in CloudFormation Templates</a>.</p>
    """

    capabilities_reason: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="CapabilitiesReason")
    ] = pydantic.Field(default=None)
    """
    The list of resources that generated the values in the <code>Capabilities</code> response element.
    """

    resource_types: typing_extensions.Annotated[
        typing.Optional[typing.List[ResourceType]], FieldMetadata(alias="ResourceTypes")
    ] = pydantic.Field(default=None)
    """
    A list of all the template resource types that are defined in the template, such as <code>AWS::EC2::Instance</code>, <code>AWS::Dynamo::Table</code>, and <code>Custom::MyCustomInstance</code>.
    """

    version: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Version")] = pydantic.Field(
        default=None
    )
    """
    The Amazon Web Services template format version, which identifies the capabilities of the template.
    """

    metadata: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Metadata")] = pydantic.Field(
        default=None
    )
    """
    The value that's defined for the <code>Metadata</code> property of the template.
    """

    declared_transforms: typing_extensions.Annotated[
        typing.Optional[typing.List[TransformName]], FieldMetadata(alias="DeclaredTransforms")
    ] = pydantic.Field(default=None)
    """
    A list of the transforms that are declared in the template.
    """

    resource_identifier_summaries: typing_extensions.Annotated[
        typing.Optional[typing.List[ResourceIdentifierSummary]], FieldMetadata(alias="ResourceIdentifierSummaries")
    ] = pydantic.Field(default=None)
    """
    A list of resource identifier summaries that describe the target resources of an import operation and the properties you can provide during the import to identify the target resources. For example, <code>BucketName</code> is a possible identifier property for an <code>AWS::S3::Bucket</code> resource.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
