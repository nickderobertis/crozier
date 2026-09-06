

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .global_resources_shared_models_string_translation import GlobalResourcesSharedModelsStringTranslation


class GlobalResourcesSharedModelsStringDefinition(UniversalBaseModel):
    """
    The definition of a string to be translated
    """

    description_for_translator: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="DescriptionForTranslator"),
        pydantic.Field(alias="DescriptionForTranslator", description="The description of the string to be translated."),
    ]
    """
    The description of the string to be translated.
    """

    do_not_translate: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="DoNotTranslate"),
        pydantic.Field(
            alias="DoNotTranslate", description="True if the string should not be translated. False by default."
        ),
    ] = None
    """
    True if the string should not be translated. False by default.
    """

    id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Id"),
        pydantic.Field(alias="Id", description="The identifier for the string. Read Only."),
    ] = None
    """
    The identifier for the string. Read Only.
    """

    parameter_count: typing_extensions.Annotated[
        typing.Optional[int],
        FieldMetadata(alias="ParameterCount"),
        pydantic.Field(alias="ParameterCount", description="The number of parameters expected for the string."),
    ] = None
    """
    The number of parameters expected for the string.
    """

    timestamp: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="Timestamp"),
        pydantic.Field(
            alias="Timestamp", description="A value indicating the last modification of this string. Read Only."
        ),
    ] = None
    """
    A value indicating the last modification of this string. Read Only.
    """

    translations: typing_extensions.Annotated[
        typing.Optional[typing.List[GlobalResourcesSharedModelsStringTranslation]],
        FieldMetadata(alias="Translations"),
        pydantic.Field(alias="Translations", description="Translations for the string."),
    ] = None
    """
    Translations for the string.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
