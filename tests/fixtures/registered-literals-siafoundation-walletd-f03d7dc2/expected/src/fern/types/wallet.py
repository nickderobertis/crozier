

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Wallet(UniversalBaseModel):
    id: int
    name: str
    description: str
    date_created: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="dateCreated"), pydantic.Field(alias="dateCreated")
    ]
    last_updated: typing_extensions.Annotated[
        dt.datetime, FieldMetadata(alias="lastUpdated"), pydantic.Field(alias="lastUpdated")
    ]
    metadata: typing.Optional[typing.Dict[str, typing.Any]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
