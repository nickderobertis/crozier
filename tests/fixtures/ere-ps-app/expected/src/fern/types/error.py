

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .trace import Trace
from .xml_gregorian_calendar import XmlGregorianCalendar


class Error(UniversalBaseModel):
    message_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="messageID"), pydantic.Field(alias="messageID")
    ] = None
    timestamp: typing.Optional[XmlGregorianCalendar] = None
    trace: typing.Optional[typing.List[Trace]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
