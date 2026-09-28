

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class V2QueryRowsCountData(UniversalBaseModel):
    """
    Total number of table rows matching a predicate.
    """

    total_count: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="totalCount"),
        pydantic.Field(
            alias="totalCount", description="Number of rows matching the predicate across the entire table."
        ),
    ]
    """
    Number of rows matching the predicate across the entire table.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
