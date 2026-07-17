

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .resource_identifier_property_value import ResourceIdentifierPropertyValue


class ResourceToImport(UniversalBaseModel):
    """
    Describes the target resource of an import operation.
    """

    resource_type: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="ResourceType"),
        pydantic.Field(
            alias="ResourceType",
            description='The type of resource to import into your stack, such as <code>AWS::S3::Bucket</code>. For a list of supported resource types, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html">Resources that support import operations</a> in the CloudFormation User Guide.',
        ),
    ]
    """
    The type of resource to import into your stack, such as <code>AWS::S3::Bucket</code>. For a list of supported resource types, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html">Resources that support import operations</a> in the CloudFormation User Guide.
    """

    logical_resource_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="LogicalResourceId"),
        pydantic.Field(
            alias="LogicalResourceId", description="The logical ID of the target resource as specified in the template."
        ),
    ]
    """
    The logical ID of the target resource as specified in the template.
    """

    resource_identifier: typing_extensions.Annotated[
        typing.Dict[str, ResourceIdentifierPropertyValue],
        FieldMetadata(alias="ResourceIdentifier"),
        pydantic.Field(
            alias="ResourceIdentifier",
            description="A key-value pair that identifies the target resource. The key is an identifier property (for example, <code>BucketName</code> for <code>AWS::S3::Bucket</code> resources) and the value is the actual property value (for example, <code>MyS3Bucket</code>).",
        ),
    ]
    """
    A key-value pair that identifies the target resource. The key is an identifier property (for example, <code>BucketName</code> for <code>AWS::S3::Bucket</code> resources) and the value is the actual property value (for example, <code>MyS3Bucket</code>).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
