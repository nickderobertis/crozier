

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Container(UniversalBaseModel):
    name: typing.Optional[str] = None
    issn_printed: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="issnPrinted"), pydantic.Field(alias="issnPrinted")
    ] = None
    issn_online: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="issnOnline"), pydantic.Field(alias="issnOnline")
    ] = None
    issn_linking: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="issnLinking"), pydantic.Field(alias="issnLinking")
    ] = None
    ep: typing.Optional[str] = None
    iss: typing.Optional[str] = None
    sp: typing.Optional[str] = None
    vol: typing.Optional[str] = None
    edition: typing.Optional[str] = None
    conference_place: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="conferencePlace"), pydantic.Field(alias="conferencePlace")
    ] = None
    conference_date: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="conferenceDate"), pydantic.Field(alias="conferenceDate")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
