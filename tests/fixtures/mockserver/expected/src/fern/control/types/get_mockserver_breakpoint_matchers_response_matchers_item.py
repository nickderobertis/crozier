

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetMockserverBreakpointMatchersResponseMatchersItem(UniversalBaseModel):
    id: typing.Optional[str] = None
    http_request: typing_extensions.Annotated[
        typing.Optional[typing.Dict[str, typing.Any]],
        FieldMetadata(alias="httpRequest"),
        pydantic.Field(alias="httpRequest"),
    ] = None
    phases: typing.Optional[typing.List[str]] = None
    client_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="clientId"),
        pydantic.Field(
            alias="clientId", description="callback WebSocket client id that owns this matcher (always present)"
        ),
    ] = None
    """
    callback WebSocket client id that owns this matcher (always present)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
