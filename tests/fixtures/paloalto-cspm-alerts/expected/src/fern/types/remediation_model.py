

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .remediation_action import RemediationAction


class RemediationModel(UniversalBaseModel):
    """
    Model for Remediation
    """

    actions: typing.Optional[typing.List[RemediationAction]] = pydantic.Field(default=None)
    """
    Policy Action
    """

    cli_script_template: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="cliScriptTemplate"),
        pydantic.Field(alias="cliScriptTemplate", description="CLI Script Template"),
    ] = None
    """
    CLI Script Template
    """

    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
