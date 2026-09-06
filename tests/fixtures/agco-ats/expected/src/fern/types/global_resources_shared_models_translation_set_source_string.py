

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GlobalResourcesSharedModelsTranslationSetSourceString(UniversalBaseModel):
    """
    Information needed to translate a string in a translation set
    """

    description_for_translator: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="DescriptionForTranslator"),
        pydantic.Field(
            alias="DescriptionForTranslator",
            description="A description of the string to translate. This should contain context and parameter count.",
        ),
    ] = None
    """
    A description of the string to translate. This should contain context and parameter count.
    """

    language_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="LanguageID"),
        pydantic.Field(alias="LanguageID", description="The ID of the language from which to translate the string"),
    ] = None
    """
    The ID of the language from which to translate the string
    """

    string_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StringID"),
        pydantic.Field(alias="StringID", description="The ID of the string to translate"),
    ] = None
    """
    The ID of the string to translate
    """

    string_value: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StringValue"),
        pydantic.Field(alias="StringValue", description="The string to translate"),
    ] = None
    """
    The string to translate
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
