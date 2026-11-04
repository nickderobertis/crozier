

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .frequentword_type_custom_custom import FrequentwordTypeCustomCustom


class FrequentwordTypeCustom(UniversalBaseModel):
    """
    Custom frequent words
    """

    custom: typing_extensions.Annotated[
        FrequentwordTypeCustomCustom,
        FieldMetadata(alias="Custom"),
        pydantic.Field(alias="Custom", description="Custom frequent words"),
    ]
    """
    Custom frequent words
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
