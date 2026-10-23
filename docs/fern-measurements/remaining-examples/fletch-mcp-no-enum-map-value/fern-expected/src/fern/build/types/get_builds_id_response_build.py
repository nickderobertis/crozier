

import datetime as dt
import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .get_builds_id_response_build_billing_mode import GetBuildsIdResponseBuildBillingMode
from .get_builds_id_response_build_capabilities import GetBuildsIdResponseBuildCapabilities
from .get_builds_id_response_build_custody_mode import GetBuildsIdResponseBuildCustodyMode


class GetBuildsIdResponseBuild(UniversalBaseModel):
    id: typing.Optional[str] = None
    project_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="projectId"), pydantic.Field(alias="projectId")
    ] = None
    prompt: typing.Optional[str] = None
    status: typing.Optional[str] = None
    billing_mode: typing_extensions.Annotated[
        typing.Optional[GetBuildsIdResponseBuildBillingMode],
        FieldMetadata(alias="billingMode"),
        pydantic.Field(
            alias="billingMode",
            description="Immutable queued billing choice. Null means the older record did not capture this choice.",
        ),
    ] = None
    """
    Immutable queued billing choice. Null means the older record did not capture this choice.
    """

    custody_mode: typing_extensions.Annotated[
        typing.Optional[GetBuildsIdResponseBuildCustodyMode],
        FieldMetadata(alias="custodyMode"),
        pydantic.Field(alias="custodyMode"),
    ] = None
    provider: typing.Optional[str] = None
    model: typing.Optional[str] = None
    capabilities: typing.Optional[GetBuildsIdResponseBuildCapabilities] = None
    error: typing.Optional[str] = None
    started_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="startedAt"), pydantic.Field(alias="startedAt")
    ] = None
    finished_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="finishedAt"), pydantic.Field(alias="finishedAt")
    ] = None
    created_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="createdAt"), pydantic.Field(alias="createdAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
