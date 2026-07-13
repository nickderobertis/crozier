

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ExportStatementCardCsvRead(UniversalBaseModel):
    card_id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The card for which this statement was created.
    """

    created: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the statement model's creation.
    """

    date_end: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date until which statement shows transactions.
    """

    date_start: typing.Optional[str] = pydantic.Field(default=None)
    """
    The date from when this statement shows transactions.
    """

    id: typing.Optional[int] = pydantic.Field(default=None)
    """
    The id of the customer statement model.
    """

    regional_format: typing.Optional[str] = pydantic.Field(default=None)
    """
    The regional format of a CSV statement.
    """

    status: typing.Optional[str] = pydantic.Field(default=None)
    """
    The status of the export.
    """

    updated: typing.Optional[str] = pydantic.Field(default=None)
    """
    The timestamp of the statement model's last update.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
