

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .form_field import FormField
from .tag import Tag


class Form(UniversalBaseModel):
    call_to_action: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="callToAction"), pydantic.Field(alias="callToAction")
    ] = None
    css_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="cssUrl"), pydantic.Field(alias="cssUrl")
    ] = None
    fields: typing.Optional[typing.List[FormField]] = None
    heading: typing.Optional[str] = None
    id: typing.Optional[str] = None
    name: typing.Optional[str] = None
    no_css: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="noCss"), pydantic.Field(alias="noCss")
    ] = None
    owned_by: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="ownedBy"), pydantic.Field(alias="ownedBy")
    ] = None
    tags: typing.Optional[typing.List[Tag]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
