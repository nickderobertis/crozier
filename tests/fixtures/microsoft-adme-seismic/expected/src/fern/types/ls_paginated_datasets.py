

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class LsPaginatedDatasets(UniversalBaseModel):
    datasets: typing.List[str] = pydantic.Field()
    """
    Array of datasets inside the subproject.
    """

    next_page_cursor: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="nextPageCursor"),
        pydantic.Field(alias="nextPageCursor", description="Next cursor for pagination."),
    ]
    """
    Next cursor for pagination.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
