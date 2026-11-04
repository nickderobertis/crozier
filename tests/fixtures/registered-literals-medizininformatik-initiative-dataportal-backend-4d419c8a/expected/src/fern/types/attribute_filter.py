

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .term_code import TermCode


class AttributeFilter(UniversalBaseModel):
    """
    An AttributeFilter requires different properties, depending on the type. Please refer to the JSON Schema for this.
    """

    attribute_code: typing_extensions.Annotated[
        typing.Optional[TermCode], FieldMetadata(alias="attributeCode"), pydantic.Field(alias="attributeCode")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
