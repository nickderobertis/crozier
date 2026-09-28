

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata
from .create_table_request_schema_columns_item_options_item import CreateTableRequestSchemaColumnsItemOptionsItem
from .create_table_request_schema_columns_item_type import CreateTableRequestSchemaColumnsItemType


class CreateTableRequestSchemaColumnsItem(UniversalBaseModel):
    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Optional client-provided column identifier.
    """

    name: str = pydantic.Field()
    """
    Column name.
    """

    type: CreateTableRequestSchemaColumnsItemType = pydantic.Field()
    """
    Column data type.
    """

    required: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether inserts must supply a value for this column.
    """

    unique: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether values in the column must be unique.
    """

    options: typing.Optional[typing.List[CreateTableRequestSchemaColumnsItemOptionsItem]] = pydantic.Field(default=None)
    """
    Select options for select-type columns.
    """

    multiple: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether a select column accepts multiple values.
    """

    currency_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="currencyCode"),
        pydantic.Field(alias="currencyCode", description="ISO 4217 code for currency columns."),
    ] = None
    """
    ISO 4217 code for currency columns.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
