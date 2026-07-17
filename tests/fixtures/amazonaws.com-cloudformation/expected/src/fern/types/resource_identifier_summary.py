

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .logical_resource_id import LogicalResourceId
from .resource_identifier_property_key import ResourceIdentifierPropertyKey


class ResourceIdentifierSummary(UniversalBaseModel):
    """
    Describes the target resources of a specific type in your import template (for example, all <code>AWS::S3::Bucket</code> resources) and the properties you can provide during the import to identify resources of that type.
    """

    resource_type: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ResourceType"),
        pydantic.Field(
            alias="ResourceType",
            description="The template resource type of the target resources, such as <code>AWS::S3::Bucket</code>.",
        ),
    ] = None
    """
    The template resource type of the target resources, such as <code>AWS::S3::Bucket</code>.
    """

    logical_resource_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[LogicalResourceId]],
        FieldMetadata(alias="LogicalResourceIds"),
        pydantic.Field(
            alias="LogicalResourceIds",
            description="The logical IDs of the target resources of the specified <code>ResourceType</code>, as defined in the import template.",
        ),
    ] = None
    """
    The logical IDs of the target resources of the specified <code>ResourceType</code>, as defined in the import template.
    """

    resource_identifiers: typing_extensions.Annotated[
        typing.Optional[typing.List[ResourceIdentifierPropertyKey]],
        FieldMetadata(alias="ResourceIdentifiers"),
        pydantic.Field(
            alias="ResourceIdentifiers",
            description="The resource properties you can provide during the import to identify your target resources. For example, <code>BucketName</code> is a possible identifier property for <code>AWS::S3::Bucket</code> resources.",
        ),
    ] = None
    """
    The resource properties you can provide during the import to identify your target resources. For example, <code>BucketName</code> is a possible identifier property for <code>AWS::S3::Bucket</code> resources.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
