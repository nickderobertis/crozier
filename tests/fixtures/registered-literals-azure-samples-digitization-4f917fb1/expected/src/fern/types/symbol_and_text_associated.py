

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SymbolAndTextAssociated(UniversalBaseModel):
    """
    Class that represents the symbol detected properties and the text associated within the symbol
    """

    top_x: typing_extensions.Annotated[float, FieldMetadata(alias="topX"), pydantic.Field(alias="topX")]
    top_y: typing_extensions.Annotated[float, FieldMetadata(alias="topY"), pydantic.Field(alias="topY")]
    bottom_x: typing_extensions.Annotated[float, FieldMetadata(alias="bottomX"), pydantic.Field(alias="bottomX")]
    bottom_y: typing_extensions.Annotated[float, FieldMetadata(alias="bottomY"), pydantic.Field(alias="bottomY")]
    id: int
    label: str
    score: typing.Optional[float] = None
    text_associated: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
