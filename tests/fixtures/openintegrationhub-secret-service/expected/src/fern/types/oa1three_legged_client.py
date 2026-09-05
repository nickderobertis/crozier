

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from ..core.serialization import FieldMetadata
from .mutable_oa1three_legged_client import MutableOa1ThreeLeggedClient


class Oa1ThreeLeggedClient(MutableOa1ThreeLeggedClient):
    id: typing_extensions.Annotated[str, FieldMetadata(alias="_id"), pydantic.Field(alias="_id")]
    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="Client creation time"),
    ]
    """
    Client creation time
    """

    updated_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime],
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="Client update time"),
    ] = None
    """
    Client update time
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
