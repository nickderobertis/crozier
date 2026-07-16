

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .type_version_summary_type import TypeVersionSummaryType


class TypeVersionSummary(UniversalBaseModel):
    """
    Contains summary information about a specific version of a CloudFormation extension.
    """

    type: typing_extensions.Annotated[
        typing.Optional[TypeVersionSummaryType],
        FieldMetadata(alias="Type"),
        pydantic.Field(alias="Type", description="The kind of extension."),
    ] = None
    """
    The kind of extension.
    """

    type_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TypeName"),
        pydantic.Field(alias="TypeName", description="The name of the extension."),
    ] = None
    """
    The name of the extension.
    """

    version_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="VersionId"),
        pydantic.Field(
            alias="VersionId",
            description="The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it's registered.",
        ),
    ] = None
    """
    The ID of a specific version of the extension. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the extension version when it's registered.
    """

    is_default_version: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="IsDefaultVersion"),
        pydantic.Field(
            alias="IsDefaultVersion",
            description="<p>Whether the specified extension version is set as the default version.</p> <p>This applies only to private extensions you have registered in your account, and extensions published by Amazon. For public third-party extensions, CloudFormation returns <code>null</code>.</p>",
        ),
    ] = None
    """
    <p>Whether the specified extension version is set as the default version.</p> <p>This applies only to private extensions you have registered in your account, and extensions published by Amazon. For public third-party extensions, CloudFormation returns <code>null</code>.</p>
    """

    arn: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Arn"),
        pydantic.Field(alias="Arn", description="The Amazon Resource Name (ARN) of the extension version."),
    ] = None
    """
    The Amazon Resource Name (ARN) of the extension version.
    """

    time_created: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="TimeCreated"),
        pydantic.Field(alias="TimeCreated", description="When the version was registered."),
    ] = None
    """
    When the version was registered.
    """

    description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Description"),
        pydantic.Field(alias="Description", description="The description of the extension version."),
    ] = None
    """
    The description of the extension version.
    """

    public_version_number: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PublicVersionNumber"),
        pydantic.Field(
            alias="PublicVersionNumber",
            description='<p>For public extensions that have been activated for this account and region, the version of the public extension to be used for CloudFormation operations in this account and region. For any extensions other than activated third-arty extensions, CloudFormation returns <code>null</code>.</p> <p>How you specified <code>AutoUpdate</code> when enabling the extension affects whether CloudFormation automatically updates the extension in this account and region when a new version is released. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable-auto">Setting CloudFormation to automatically use new versions of extensions</a> in the <i>CloudFormation User Guide</i>.</p>',
        ),
    ] = None
    """
    <p>For public extensions that have been activated for this account and region, the version of the public extension to be used for CloudFormation operations in this account and region. For any extensions other than activated third-arty extensions, CloudFormation returns <code>null</code>.</p> <p>How you specified <code>AutoUpdate</code> when enabling the extension affects whether CloudFormation automatically updates the extension in this account and region when a new version is released. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable-auto">Setting CloudFormation to automatically use new versions of extensions</a> in the <i>CloudFormation User Guide</i>.</p>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
