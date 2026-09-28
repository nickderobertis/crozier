

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V2TableRowMatch(UniversalBaseModel):
    """
    One matching cell returned by a table row search.
    """

    ordinal: float = pydantic.Field()
    """
    Zero-based row index in the filtered and sorted view.
    """

    row_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="rowId"), pydantic.Field(alias="rowId", description="Identifier of the matching row.")
    ]
    """
    Identifier of the matching row.
    """

    column: str = pydantic.Field()
    """
    Column name containing the match.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
