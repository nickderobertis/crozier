

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class CollectionDto(UniversalBaseModel):
    created_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdDate"), pydantic.Field(alias="createdDate")
    ]
    filtered: bool
    id: str
    last_modified_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastModifiedDate"), pydantic.Field(alias="lastModifiedDate")
    ]
    name: str
    ordered: bool
    series_ids: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="seriesIds"), pydantic.Field(alias="seriesIds")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
