

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class SubscriptionCreateModify(UniversalBaseModel):
    action: str
    callback_on_modify: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="callbackOnModify"), pydantic.Field(alias="callbackOnModify")
    ] = None
    callback_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="callbackUrl"), pydantic.Field(alias="callbackUrl")
    ] = None
    custom: typing.Optional[typing.Any] = None
    frequency: str
    key: typing.Optional[str] = None
    name: typing.Optional[str] = None
    serial: typing.Optional[str] = None
    start_from: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="startFrom"), pydantic.Field(alias="startFrom")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
