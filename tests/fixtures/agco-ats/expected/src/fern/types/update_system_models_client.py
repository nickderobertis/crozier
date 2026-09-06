

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class UpdateSystemModelsClient(UniversalBaseModel):
    client_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="ClientID"),
        pydantic.Field(alias="ClientID", description="Read Only. The id of the client"),
    ] = None
    """
    Read Only. The id of the client
    """

    last_checkin: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="LastCheckin"),
        pydantic.Field(
            alias="LastCheckin", description="Read Only. The time of the client's last checkin with the server."
        ),
    ] = None
    """
    Read Only. The time of the client's last checkin with the server.
    """

    tag: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Tag"),
        pydantic.Field(alias="Tag", description="A description of the client that can be used for easy reference"),
    ] = None
    """
    A description of the client that can be used for easy reference
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
