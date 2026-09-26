

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2workflow_group_data_columns_item_options_item import V2WorkflowGroupDataColumnsItemOptionsItem
from .v2workflow_group_data_columns_item_type import V2WorkflowGroupDataColumnsItemType


class V2WorkflowGroupDataColumnsItem(UniversalBaseModel):
    """
    A typed column in a table schema.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Stable server-assigned column identifier.
    """

    name: str = pydantic.Field()
    """
    Column name used as the public row-data key.
    """

    type: V2WorkflowGroupDataColumnsItemType = pydantic.Field()
    """
    Data type of values stored in the column.
    """

    required: bool = pydantic.Field()
    """
    Whether inserts require a value for this column.
    """

    unique: bool = pydantic.Field()
    """
    Whether values must be unique across table rows.
    """

    workflow_group_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="workflowGroupId"),
        pydantic.Field(alias="workflowGroupId", description="Workflow group whose output populates this column."),
    ] = None
    """
    Workflow group whose output populates this column.
    """

    options: typing.Optional[typing.List[V2WorkflowGroupDataColumnsItemOptionsItem]] = pydantic.Field(default=None)
    """
    Options declared for a select column.
    """

    multiple: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Whether a select column accepts multiple options.
    """

    currency_code: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="currencyCode"),
        pydantic.Field(
            alias="currencyCode", description="ISO 4217 code for a currency column, normalized to uppercase."
        ),
    ] = None
    """
    ISO 4217 code for a currency column, normalized to uppercase.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
