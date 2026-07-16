

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TypeConfigurationDetails(UniversalBaseModel):
    """
    <p>Detailed information concerning the specification of a CloudFormation extension in a given account and region.</p> <p>For more information, see <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry-register.html#registry-set-configuration">Configuring extensions at the account level</a> in the <i>CloudFormation User Guide</i>.</p>
    """

    arn: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Arn")] = pydantic.Field(default=None)
    """
    The Amazon Resource Name (ARN) for the configuration data, in this account and region.
    """

    alias: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Alias")] = pydantic.Field(
        default=None
    )
    """
    The alias specified for this configuration, if one was specified when the configuration was set.
    """

    configuration: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="Configuration")] = (
        pydantic.Field(default=None)
    )
    """
    <p>A JSON string specifying the configuration data for the extension, in this account and region.</p> <p>If a configuration hasn't been set for a specified extension, CloudFormation returns <code>{}</code>.</p>
    """

    last_updated: typing_extensions.Annotated[typing.Optional[dt.datetime], FieldMetadata(alias="LastUpdated")] = (
        pydantic.Field(default=None)
    )
    """
    <p>When the configuration data was last updated for this extension.</p> <p>If a configuration hasn't been set for a specified extension, CloudFormation returns <code>null</code>.</p>
    """

    type_arn: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="TypeArn")] = pydantic.Field(
        default=None
    )
    """
    <p>The Amazon Resource Name (ARN) for the extension, in this account and region.</p> <p>For public extensions, this will be the ARN assigned when you <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html">activate the type</a> in this account and region. For private extensions, this will be the ARN assigned when you <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">register the type</a> in this account and region.</p>
    """

    type_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="TypeName")] = pydantic.Field(
        default=None
    )
    """
    The name of the extension.
    """

    is_default_configuration: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="IsDefaultConfiguration")
    ] = pydantic.Field(default=None)
    """
    Whether this configuration data is the default configuration for the extension.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
