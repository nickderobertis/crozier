

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ReadListDto(UniversalBaseModel):
    book_ids: typing_extensions.Annotated[
        typing.List[str], FieldMetadata(alias="bookIds"), pydantic.Field(alias="bookIds")
    ]
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
    summary: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
