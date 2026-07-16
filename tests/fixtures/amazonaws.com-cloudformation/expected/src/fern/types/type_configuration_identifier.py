

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .type_configuration_identifier_type import TypeConfigurationIdentifierType


class TypeConfigurationIdentifier(UniversalBaseModel):
    """
    Identifying information for the configuration of a CloudFormation extension.
    """

    type_arn: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="TypeArn")] = pydantic.Field(
        default=None
    )
    """
    <p>The Amazon Resource Name (ARN) for the extension, in this account and region.</p> <p>For public extensions, this will be the ARN assigned when you <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_ActivateType.html">activate the type</a> in this account and region. For private extensions, this will be the ARN assigned when you <a href="https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_RegisterType.html">register the type</a> in this account and region.</p>
    """

    type_configuration_alias: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="TypeConfigurationAlias")
    ] = pydantic.Field(default=None)
    """
    The alias specified for this configuration, if one was specified when the configuration was set.
    """

    type_configuration_arn: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="TypeConfigurationArn")
    ] = pydantic.Field(default=None)
    """
    The Amazon Resource Name (ARN) for the configuration, in this account and region.
    """

    type: typing_extensions.Annotated[typing.Optional[TypeConfigurationIdentifierType], FieldMetadata(alias="Type")] = (
        pydantic.Field(default=None)
    )
    """
    The type of extension.
    """

    type_name: typing_extensions.Annotated[typing.Optional[str], FieldMetadata(alias="TypeName")] = pydantic.Field(
        default=None
    )
    """
    The name of the extension type to which this configuration applies.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
