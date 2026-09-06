

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class GlobalResourcesSharedModelsTranslationSetString(UniversalBaseModel):
    """
    The resulting translation in a translation set.  is the  to which the string will be translated.
    """

    language_id: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="LanguageID"),
        pydantic.Field(alias="LanguageID", description="The ID of the language into which to translate the string"),
    ]
    """
    The ID of the language into which to translate the string
    """

    string_id: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="StringID"),
        pydantic.Field(alias="StringID", description="The Id of the string translation that has been requested"),
    ]
    """
    The Id of the string translation that has been requested
    """

    string_value: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StringValue"),
        pydantic.Field(alias="StringValue", description="The string value returned from the translator"),
    ] = None
    """
    The string value returned from the translator
    """

    translation_set_id: typing_extensions.Annotated[
        int,
        FieldMetadata(alias="TranslationSetId"),
        pydantic.Field(alias="TranslationSetId", description="The id of the TranslationSet"),
    ]
    """
    The id of the TranslationSet
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
