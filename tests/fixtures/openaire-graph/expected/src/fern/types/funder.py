

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .fundings import Fundings


class Funder(UniversalBaseModel):
    short_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="shortName"), pydantic.Field(alias="shortName")
    ] = None
    name: typing.Optional[str] = None
    jurisdiction: typing.Optional[str] = None
    funding_stream: typing_extensions.Annotated[
        typing.Optional[Fundings], FieldMetadata(alias="fundingStream"), pydantic.Field(alias="fundingStream")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
