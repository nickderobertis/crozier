

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .update_table_column_request_updates_options_item import UpdateTableColumnRequestUpdatesOptionsItem
from .update_table_column_request_updates_type import UpdateTableColumnRequestUpdatesType


class UpdateTableColumnRequestUpdates(UniversalBaseModel):
    """
    Mutable column fields.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Replacement column name.
    """

    type: typing.Optional[UpdateTableColumnRequestUpdatesType] = pydantic.Field(default=None)
    """
    Replacement column data type.
    """

    required: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether inserts must supply a value for this column.
    """

    unique: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether values in the column must be unique.
    """

    options: typing.Optional[typing.List[UpdateTableColumnRequestUpdatesOptionsItem]] = pydantic.Field(default=None)
    """
    Replacement select options for select-type columns.
    """

    multiple: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether a select column accepts multiple values.
    """

    currency_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="currencyCode"),
        pydantic.Field(alias="currencyCode", description="Replacement ISO 4217 code for a currency column."),
    ] = None
    """
    Replacement ISO 4217 code for a currency column.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
