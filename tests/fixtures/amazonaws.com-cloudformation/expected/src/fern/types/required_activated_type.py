

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .supported_major_version import SupportedMajorVersion


class RequiredActivatedType(UniversalBaseModel):
    """
    <p>For extensions that are modules, a public third-party extension that must be activated in your account in order for the module itself to be activated.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/modules.html#module-enabling">Activating public modules for use in your account</a> in the <i>CloudFormation User Guide</i>.</p>
    """

    type_name_alias: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="TypeNameAlias"),
        pydantic.Field(
            alias="TypeNameAlias",
            description="An alias assigned to the public extension, in this account and region. If you specify an alias for the extension, CloudFormation treats the alias as the extension type name within this account and region. You must use the alias to refer to the extension in your templates, API calls, and CloudFormation console.",
        ),
    ] = None
    """
    An alias assigned to the public extension, in this account and region. If you specify an alias for the extension, CloudFormation treats the alias as the extension type name within this account and region. You must use the alias to refer to the extension in your templates, API calls, and CloudFormation console.
    """

    original_type_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="OriginalTypeName"),
        pydantic.Field(
            alias="OriginalTypeName",
            description='<p>The type name of the public extension.</p> <p>If you specified a <code>TypeNameAlias</code> when enabling the extension in this account and region, CloudFormation treats that alias as the extension\'s type name within the account and region, not the type name of the public extension. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable-alias">Specifying aliases to refer to extensions</a> in the <i>CloudFormation User Guide</i>.</p>',
        ),
    ] = None
    """
    <p>The type name of the public extension.</p> <p>If you specified a <code>TypeNameAlias</code> when enabling the extension in this account and region, CloudFormation treats that alias as the extension's type name within the account and region, not the type name of the public extension. For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-public.html#registry-public-enable-alias">Specifying aliases to refer to extensions</a> in the <i>CloudFormation User Guide</i>.</p>
    """

    publisher_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="PublisherId"),
        pydantic.Field(alias="PublisherId", description="The publisher ID of the extension publisher."),
    ] = None
    """
    The publisher ID of the extension publisher.
    """

    supported_major_versions: typing_extensions.Annotated[
        typing.Optional[typing.List[SupportedMajorVersion]],
        FieldMetadata(alias="SupportedMajorVersions"),
        pydantic.Field(
            alias="SupportedMajorVersions",
            description="A list of the major versions of the extension type that the macro supports.",
        ),
    ] = None
    """
    A list of the major versions of the extension type that the macro supports.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
