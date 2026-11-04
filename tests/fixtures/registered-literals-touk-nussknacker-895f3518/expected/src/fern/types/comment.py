

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Comment(UniversalBaseModel):
    id: int
    process_version_id: typing_extensions.Annotated[
        int, FieldMetadata(alias="processVersionId"), pydantic.Field(alias="processVersionId")
    ]
    content: str
    user: str
    create_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createDate"), pydantic.Field(alias="createDate")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
