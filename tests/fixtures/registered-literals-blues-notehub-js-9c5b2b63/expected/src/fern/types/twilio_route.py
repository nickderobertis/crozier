

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .filter import Filter


class TwilioRoute(UniversalBaseModel):
    account_sid: typing.Optional[str] = None
    auth_token: typing.Optional[str] = None
    filter: typing.Optional[Filter] = None
    fleets: typing.Optional[typing.List[str]] = None
    from_: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="from"), pydantic.Field(alias="from")
    ] = None
    message: typing.Optional[str] = None
    throttle_ms: typing.Optional[int] = None
    timeout: typing.Optional[int] = None
    to: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
