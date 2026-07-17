

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SetTypeConfigurationOutput(UniversalBaseModel):
    configuration_arn: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ConfigurationArn"),
        pydantic.Field(
            alias="ConfigurationArn",
            description="<p>The Amazon Resource Name (ARN) for the configuration data, in this account and region.</p> <p>Conditional: You must specify <code>ConfigurationArn</code>, or <code>Type</code> and <code>TypeName</code>.</p>",
        ),
    ] = None
    """
    <p>The Amazon Resource Name (ARN) for the configuration data, in this account and region.</p> <p>Conditional: You must specify <code>ConfigurationArn</code>, or <code>Type</code> and <code>TypeName</code>.</p>
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
