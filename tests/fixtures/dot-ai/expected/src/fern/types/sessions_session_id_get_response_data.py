

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .sessions_session_id_get_response_data_data import SessionsSessionIdGetResponseDataData


class SessionsSessionIdGetResponseData(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Session ID
    """

    data: SessionsSessionIdGetResponseDataData = pydantic.Field()
    """
    Session data
    """

    created_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="Session creation timestamp"),
    ] = None
    """
    Session creation timestamp
    """

    expires_at: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="expiresAt"),
        pydantic.Field(alias="expiresAt", description="Session expiration timestamp"),
    ] = None
    """
    Session expiration timestamp
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
