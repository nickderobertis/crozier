

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .filter_crs import FilterCrs


class FilterCrsFilter(UniversalBaseModel):
    filter_crs: typing_extensions.Annotated[
        typing.Optional[FilterCrs], FieldMetadata(alias="filterCrs"), pydantic.Field(alias="filterCrs")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
