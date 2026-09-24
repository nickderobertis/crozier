

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LedConnection(UniversalBaseModel):
    connected: bool = pydantic.Field()
    """
    Whether the led is connected
    """

    last_connected_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="lastConnectedAt"),
        pydantic.Field(alias="lastConnectedAt", description="The last connected at time of the led"),
    ] = None
    """
    The last connected at time of the led
    """

    error: typing.Optional[str] = pydantic.Field(default=None)
    """
    The error message of the led
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
