

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .global_resources_shared_models_string_translation_state import GlobalResourcesSharedModelsStringTranslationState


class GlobalResourcesSharedModelsStringTranslation(UniversalBaseModel):
    """
    A translation of a string in a specific language
    """

    author_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="AuthorId"),
        pydantic.Field(alias="AuthorId", description="The id of the user to last edit thie translation"),
    ] = None
    """
    The id of the user to last edit thie translation
    """

    language_id: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="LanguageId"),
        pydantic.Field(alias="LanguageId", description="The id of the language of the translation"),
    ] = None
    """
    The id of the language of the translation
    """

    state: typing_extensions.Annotated[
        typing.Optional[GlobalResourcesSharedModelsStringTranslationState],
        FieldMetadata(alias="State"),
        pydantic.Field(alias="State", description="The state of the translation"),
    ] = None
    """
    The state of the translation
    """

    string_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="StringId"),
        pydantic.Field(alias="StringId", description="The id of the string that is translated"),
    ] = None
    """
    The id of the string that is translated
    """

    string_value: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="StringValue"),
        pydantic.Field(alias="StringValue", description="The translated string"),
    ]
    """
    The translated string
    """

    timestamp: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Timestamp"),
        pydantic.Field(
            alias="Timestamp", description="A value indicating the last modification of this translation. Read Only."
        ),
    ] = None
    """
    A value indicating the last modification of this translation. Read Only.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
