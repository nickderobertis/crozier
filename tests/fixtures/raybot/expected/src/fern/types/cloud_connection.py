

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CloudConnection(UniversalBaseModel):
    connected: bool
    last_connected_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="lastConnectedAt"), pydantic.Field(alias="lastConnectedAt")
    ] = None
    uptime: float = pydantic.Field()
    """
    The uptime of the cloud connection in seconds
    """

    error: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
