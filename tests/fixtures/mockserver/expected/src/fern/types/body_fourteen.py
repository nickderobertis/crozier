

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .body_fourteen_match_type import BodyFourteenMatchType
from .body_fourteen_type import BodyFourteenType


class BodyFourteen(UniversalBaseModel):
    """
    json body matcher
    """

    not_: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="not"), pydantic.Field(alias="not")
    ] = None
    optional: typing.Optional[bool] = None
    type: typing.Optional[BodyFourteenType] = None
    json_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="json"), pydantic.Field(alias="json")
    ] = None
    content_type: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="contentType"), pydantic.Field(alias="contentType")
    ] = None
    match_type: typing_extensions.Annotated[
        typing.Optional[BodyFourteenMatchType], FieldMetadata(alias="matchType"), pydantic.Field(alias="matchType")
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
