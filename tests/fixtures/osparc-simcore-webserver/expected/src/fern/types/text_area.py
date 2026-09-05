

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class TextArea(UniversalBaseModel):
    min_height: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="minHeight"),
        pydantic.Field(alias="minHeight", description="minimum Height of the textarea"),
    ]
    """
    minimum Height of the textarea
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
