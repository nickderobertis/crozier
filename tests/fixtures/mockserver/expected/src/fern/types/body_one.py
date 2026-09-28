

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .body_one_match_type import BodyOneMatchType
from .body_one_type import BodyOneType


class BodyOne(UniversalBaseModel):
    """
    json body matcher
    """

    not_: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="not"), pydantic.Field(alias="not")
    ] = None
    type: typing.Optional[BodyOneType] = None
    json_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="json"), pydantic.Field(alias="json")
    ] = None
    content_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contentType"), pydantic.Field(alias="contentType")
    ] = None
    match_type: typing_extensions.Annotated[
        typing.Optional[BodyOneMatchType], FieldMetadata(alias="matchType"), pydantic.Field(alias="matchType")
    ] = None
    match_numbers_as_strings: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="matchNumbersAsStrings"),
        pydantic.Field(alias="matchNumbersAsStrings"),
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
