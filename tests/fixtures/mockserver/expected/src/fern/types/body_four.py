

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .body_four_type import BodyFourType


class BodyFour(UniversalBaseModel):
    """
    JSON path body matcher
    """

    not_: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="not"), pydantic.Field(alias="not")
    ] = None
    type: typing.Optional[BodyFourType] = None
    json_path: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="jsonPath"), pydantic.Field(alias="jsonPath")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
