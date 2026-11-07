

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class AccountSummaryAccountTimeZone(UniversalBaseModel):
    id: str
    source: str
    confirmed: bool
    confirmed_at: typing_extensions.Annotated[
        typing.Optional[dt.datetime], FieldMetadata(alias="confirmedAt"), pydantic.Field(alias="confirmedAt")
    ] = None
    pending: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
