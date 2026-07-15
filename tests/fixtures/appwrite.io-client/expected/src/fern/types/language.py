

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Language(UniversalBaseModel):
    """
    Language
    """

    code: str = pydantic.Field()
    """
    Language two-character ISO 639-1 codes.
    """

    name: str = pydantic.Field()
    """
    Language name.
    """

    native_name: typing_extensions.Annotated[str, FieldMetadata(alias="nativeName")] = pydantic.Field()
    """
    Language native name.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
