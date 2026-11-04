

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .stopword_type_custom_custom import StopwordTypeCustomCustom


class StopwordTypeCustom(UniversalBaseModel):
    """
    Custom stopwords
    """

    custom: typing_extensions.Annotated[
        StopwordTypeCustomCustom,
        FieldMetadata(alias="Custom"),
        pydantic.Field(alias="Custom", description="Custom stopwords"),
    ]
    """
    Custom stopwords
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
