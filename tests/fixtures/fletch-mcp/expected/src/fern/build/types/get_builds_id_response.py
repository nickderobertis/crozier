

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_builds_id_response_build import GetBuildsIdResponseBuild
from .get_builds_id_response_contracts_item import GetBuildsIdResponseContractsItem


class GetBuildsIdResponse(UniversalBaseModel):
    build: typing.Optional[GetBuildsIdResponseBuild] = None
    preview_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="previewUrl"), pydantic.Field(alias="previewUrl")
    ] = None
    contracts: typing.Optional[typing.List[GetBuildsIdResponseContractsItem]] = None
    template_version: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="templateVersion"),
        pydantic.Field(
            alias="templateVersion",
            description="Sandbox frontend template version recorded for this build. Null when unknown, including legacy builds.",
        ),
    ] = None
    """
    Sandbox frontend template version recorded for this build. Null when unknown, including legacy builds.
    """

    compile: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    forge build --json result, or null if not yet compiled.
    """

    tests: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    forge test --json result, or null if not yet run.
    """

    analysis: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(default=None)
    """
    Recorded Slither result, including whether the tool ran.
    """

    artifacts: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
