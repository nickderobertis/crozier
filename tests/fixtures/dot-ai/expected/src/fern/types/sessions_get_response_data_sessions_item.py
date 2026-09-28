

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SessionsGetResponseDataSessionsItem(UniversalBaseModel):
    session_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="sessionId"), pydantic.Field(alias="sessionId", description="Session ID")
    ]
    """
    Session ID
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Session status
    """

    issue: typing.Optional[str] = pydantic.Field(default=None)
    """
    Issue being investigated
    """

    mode: typing.Optional[str] = pydantic.Field(default=None)
    """
    Remediation mode (manual/automatic)
    """

    tool_name: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="toolName"),
        pydantic.Field(alias="toolName", description="Tool that created this session"),
    ] = None
    """
    Tool that created this session
    """

    created_at: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="Session creation timestamp"),
    ]
    """
    Session creation timestamp
    """

    updated_at: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="Session last update timestamp"),
    ]
    """
    Session last update timestamp
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
