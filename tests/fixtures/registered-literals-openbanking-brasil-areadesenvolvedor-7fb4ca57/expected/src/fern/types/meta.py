

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Meta(UniversalBaseModel):
    """
    Meta informações referente à API requisitada.
    """

    total_records: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalRecords"),
        pydantic.Field(alias="totalRecords", description="Número total de registros no resultado"),
    ]
    """
    Número total de registros no resultado
    """

    total_pages: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalPages"),
        pydantic.Field(alias="totalPages", description="Número total de páginas no resultado"),
    ]
    """
    Número total de páginas no resultado
    """

    request_date_time: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="requestDateTime"),
        pydantic.Field(
            alias="requestDateTime",
            description="Data e hora da consulta, conforme especificação RFC-3339, formato UTC.",
        ),
    ]
    """
    Data e hora da consulta, conforme especificação RFC-3339, formato UTC.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
