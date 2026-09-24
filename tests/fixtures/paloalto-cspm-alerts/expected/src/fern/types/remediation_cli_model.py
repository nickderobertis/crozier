

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RemediationCliModel(UniversalBaseModel):
    """
    Model for Remediation Command
    """

    alert_id_vs_cli_script: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, str]],
        FieldMetadata(alias="alertIdVsCliScript"),
        pydantic.Field(alias="alertIdVsCliScript", description="Map of alert ID to CLI script"),
    ] = None
    """
    Map of alert ID to CLI script
    """

    cli_description: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="cliDescription"),
        pydantic.Field(alias="cliDescription", description="CLI script description"),
    ] = None
    """
    CLI script description
    """

    cli_script: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="cliScript"),
        pydantic.Field(alias="cliScript", description="CLI script to resolve an alert"),
    ] = None
    """
    CLI script to resolve an alert
    """

    script_impact: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="scriptImpact"),
        pydantic.Field(alias="scriptImpact", description="CLI script impact"),
    ] = None
    """
    CLI script impact
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
