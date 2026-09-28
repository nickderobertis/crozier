

from __future__ import annotations

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V2CreateTableImportDataZeroTransfer_Put(UniversalBaseModel):
    """
    Signed CSV upload instructions.
    """

    method: typing.Literal["put"] = "put"
    url: str
    headers: typing.Dict[str, str]
    expires_at: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="expiresAt"), pydantic.Field(alias="expiresAt")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class V2CreateTableImportDataZeroTransfer_Multipart(UniversalBaseModel):
    """
    Signed CSV upload instructions.
    """

    method: typing.Literal["multipart"] = "multipart"
    part_size: typing_extensions.Annotated[int, FieldMetadata(alias="partSize"), pydantic.Field(alias="partSize")]
    part_count: typing_extensions.Annotated[int, FieldMetadata(alias="partCount"), pydantic.Field(alias="partCount")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


V2CreateTableImportDataZeroTransfer = typing_extensions.Annotated[
    typing.Union[V2CreateTableImportDataZeroTransfer_Put, V2CreateTableImportDataZeroTransfer_Multipart],
    pydantic.Field(discriminator="method"),
]
