

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .conf_response_component_type import ConfResponseComponentType
from .conf_response_type import ConfResponseType
from .conf_response_unified_columns import ConfResponseUnifiedColumns


class ConfResponse(UniversalBaseModel):
    reviewed: typing.Optional[str] = pydantic.Field(default=None)
    """
    shows reviewed by name
    """

    footer: typing.Optional[str] = pydantic.Field(default=None)
    """
    footer value
    """

    report_rel: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="reportRel"),
        pydantic.Field(alias="reportRel", description="release date"),
    ] = None
    """
    release date
    """

    community: typing.Optional[str] = pydantic.Field(default=None)
    """
    shows community name
    """

    component: typing.Optional[str] = pydantic.Field(default=None)
    """
    shows component name
    """

    version: typing.Optional[str] = pydantic.Field(default=None)
    """
    shows version
    """

    release_date: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="releaseDate"),
        pydantic.Field(alias="releaseDate", description="shows version"),
    ] = None
    """
    shows version
    """

    sw360link: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="sw360Link"),
        pydantic.Field(alias="sw360Link", description="shows sw360Link"),
    ] = None
    """
    shows sw360Link
    """

    component_type: typing_extensions.Annotated[
        typing.Optional[ConfResponseComponentType],
        FieldMetadata(alias="componentType"),
        pydantic.Field(alias="componentType", description="shows component type"),
    ] = None
    """
    shows component type
    """

    component_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="componentId"),
        pydantic.Field(alias="componentId", description="shows component id"),
    ] = None
    """
    shows component id
    """

    general_assesment: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="generalAssesment"),
        pydantic.Field(alias="generalAssesment", description="shows assesment test"),
    ] = None
    """
    shows assesment test
    """

    ga_additional: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="gaAdditional"),
        pydantic.Field(alias="gaAdditional", description="shows additional info"),
    ] = None
    """
    shows additional info
    """

    ga_risk: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="gaRisk"),
        pydantic.Field(alias="gaRisk", description="shows risk info"),
    ] = None
    """
    shows risk info
    """

    ga_checkbox: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="gaCheckbox"),
        pydantic.Field(alias="gaCheckbox", description="shows checkbox status"),
    ] = None
    """
    shows checkbox status
    """

    spdx_selection: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="spdxSelection"),
        pydantic.Field(alias="spdxSelection", description="shows checkbox status for spdx"),
    ] = None
    """
    shows checkbox status for spdx
    """

    excluded_obligations: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="excludedObligations"),
        pydantic.Field(alias="excludedObligations", description="shows excluded obligations"),
    ] = None
    """
    shows excluded obligations
    """

    department: typing.Optional[str] = pydantic.Field(default=None)
    """
    shows department
    """

    dep_notes: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="depNotes"),
        pydantic.Field(alias="depNotes", description="shows department notes"),
    ] = None
    """
    shows department notes
    """

    export_notes: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="exportNotes"),
        pydantic.Field(alias="exportNotes", description="shows export notes"),
    ] = None
    """
    shows export notes
    """

    copyright_notes: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="copyrightNotes"),
        pydantic.Field(alias="copyrightNotes", description="shows copyright notes"),
    ] = None
    """
    shows copyright notes
    """

    unified_columns: typing_extensions.Annotated[
        typing.Optional[ConfResponseUnifiedColumns],
        FieldMetadata(alias="unifiedColumns"),
        pydantic.Field(alias="unifiedColumns", description="unified columns value"),
    ] = None
    """
    unified columns value
    """

    global_decision: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="globalDecision"),
        pydantic.Field(alias="globalDecision", description="shows copyright notes"),
    ] = None
    """
    shows copyright notes
    """

    type: typing.Optional[ConfResponseType] = pydantic.Field(default=None)
    """
    Denotes if info was created on error
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
