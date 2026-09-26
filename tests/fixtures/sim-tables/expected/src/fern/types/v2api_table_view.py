

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .v2table_view_config import V2TableViewConfig


class V2ApiTableView(UniversalBaseModel):
    """
    A named saved presentation of table rows and columns.
    """

    id: str = pydantic.Field()
    """
    Unique saved-view identifier.
    """

    table_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="tableId"),
        pydantic.Field(alias="tableId", description="Table to which the view belongs."),
    ]
    """
    Table to which the view belongs.
    """

    name: str = pydantic.Field()
    """
    Saved-view display name.
    """

    config: V2TableViewConfig = pydantic.Field()
    """
    Saved filter, sort, and column-layout configuration.
    """

    is_default: typing_extensions.Annotated[
        bool,
        FieldMetadata(alias="isDefault"),
        pydantic.Field(alias="isDefault", description="Whether this is the table default view."),
    ]
    """
    Whether this is the table default view.
    """

    created_by_email: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="createdByEmail"),
        pydantic.Field(alias="createdByEmail", description="Current author email, or null when removed."),
    ] = None
    """
    Current author email, or null when removed.
    """

    created_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="createdAt"),
        pydantic.Field(alias="createdAt", description="ISO 8601 timestamp when the view was created."),
    ]
    """
    ISO 8601 timestamp when the view was created.
    """

    updated_at: typing_extensions.Annotated[
        dt.datetime,
        FieldMetadata(alias="updatedAt"),
        pydantic.Field(alias="updatedAt", description="ISO 8601 timestamp when the view was last modified."),
    ]
    """
    ISO 8601 timestamp when the view was last modified.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
