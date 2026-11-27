

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class RegistrationOrigin(UniversalBaseModel):
    origin_entry_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="originEntryId"), pydantic.Field(alias="originEntryId")
    ] = None
    registered_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="registeredAt"), pydantic.Field(alias="registeredAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
