

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .permission_ruleset import PermissionRuleset
from .session_revert import SessionRevert
from .session_share import SessionShare
from .session_summary import SessionSummary
from .session_time import SessionTime


class Session(UniversalBaseModel):
    id: str
    slug: str
    project_id: typing_extensions.Annotated[str, FieldMetadata(alias="projectID"), pydantic.Field(alias="projectID")]
    directory: str
    parent_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="parentID"), pydantic.Field(alias="parentID")
    ] = None
    summary: typing.Optional[SessionSummary] = None
    share: typing.Optional[SessionShare] = None
    title: str
    version: str
    time: SessionTime
    permission: typing.Optional[PermissionRuleset] = None
    revert: typing.Optional[SessionRevert] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
