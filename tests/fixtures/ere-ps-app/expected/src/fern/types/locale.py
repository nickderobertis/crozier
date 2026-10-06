

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Locale(UniversalBaseModel):
    language: typing.Optional[str] = None
    script: typing.Optional[str] = None
    country: typing.Optional[str] = None
    variant: typing.Optional[str] = None
    extension_keys: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="extensionKeys"), pydantic.Field(alias="extensionKeys")
    ] = None
    unicode_locale_attributes: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="unicodeLocaleAttributes"),
        pydantic.Field(alias="unicodeLocaleAttributes"),
    ] = None
    unicode_locale_keys: typing_extensions.Annotated[
        typing.Optional[typing.List[str]],
        FieldMetadata(alias="unicodeLocaleKeys"),
        pydantic.Field(alias="unicodeLocaleKeys"),
    ] = None
    i_so3language: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="iSO3Language"), pydantic.Field(alias="iSO3Language")
    ] = None
    i_so3country: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="iSO3Country"), pydantic.Field(alias="iSO3Country")
    ] = None
    display_language: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayLanguage"), pydantic.Field(alias="displayLanguage")
    ] = None
    display_script: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayScript"), pydantic.Field(alias="displayScript")
    ] = None
    display_country: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayCountry"), pydantic.Field(alias="displayCountry")
    ] = None
    display_variant: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayVariant"), pydantic.Field(alias="displayVariant")
    ] = None
    display_name: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="displayName"), pydantic.Field(alias="displayName")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
