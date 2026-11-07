

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .key_view import KeyView


class SubscriptionView(UniversalBaseModel):
    action: str
    callback_on_modify: typing_extensions.Annotated[
        bool, FieldMetadata(alias="callbackOnModify"), pydantic.Field(alias="callbackOnModify")
    ]
    callback_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="callbackUrl"), pydantic.Field(alias="callbackUrl")
    ] = None
    commenced: dt.datetime
    created: typing.Optional[dt.datetime] = None
    custom: typing.Optional[typing.Any] = None
    frequency: str
    keys: typing.Optional[typing.List[KeyView]] = None
    name: typing.Optional[str] = None
    updated: typing.Optional[dt.datetime] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
