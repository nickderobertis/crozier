

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dataset import Dataset


class PaginatedDatasets(UniversalBaseModel):
    datasets: typing.Optional[typing.List[Dataset]] = None
    next_page_cursor: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="nextPageCursor"), pydantic.Field(alias="nextPageCursor")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
