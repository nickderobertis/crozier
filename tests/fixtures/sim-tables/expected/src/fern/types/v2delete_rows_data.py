

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V2DeleteRowsData(UniversalBaseModel):
    """
    Result of a bulk row deletion.
    """

    deleted_count: typing_extensions.Annotated[
        float,
        FieldMetadata(alias="deletedCount"),
        pydantic.Field(alias="deletedCount", description="Number of deleted rows."),
    ]
    """
    Number of deleted rows.
    """

    deleted_row_ids: typing_extensions.Annotated[
        typing.List[str],
        FieldMetadata(alias="deletedRowIds"),
        pydantic.Field(alias="deletedRowIds", description="Identifiers of deleted rows."),
    ]
    """
    Identifiers of deleted rows.
    """

    requested_count: typing_extensions.Annotated[
        typing.Optional[float],
        FieldMetadata(alias="requestedCount"),
        pydantic.Field(alias="requestedCount", description="Number of row identifiers requested."),
    ] = None
    """
    Number of row identifiers requested.
    """

    missing_row_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="missingRowIds"),
        pydantic.Field(alias="missingRowIds", description="Requested row identifiers not found."),
    ] = None
    """
    Requested row identifiers not found.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
