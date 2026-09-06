

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class ApiKeyDto(UniversalBaseModel):
    comment: str
    created_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="createdDate"), pydantic.Field(alias="createdDate")
    ]
    id: str
    key: str
    last_modified_date: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastModifiedDate"), pydantic.Field(alias="lastModifiedDate")
    ]
    user_id: typing_extensions.Annotated[str, FieldMetadata(alias="userId"), pydantic.Field(alias="userId")]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
