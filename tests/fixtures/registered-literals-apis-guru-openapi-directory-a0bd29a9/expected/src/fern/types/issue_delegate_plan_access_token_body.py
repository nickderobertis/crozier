

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .delegate_identity import DelegateIdentity


class IssueDelegatePlanAccessTokenBody(UniversalBaseModel):
    environment_ids: typing_extensions.Annotated[
        typing.Optional[typing.List[str]], FieldMetadata(alias="environmentIds"), pydantic.Field(alias="environmentIds")
    ] = None
    expiration: typing.Optional[dt.datetime] = None
    identity: typing.Optional[DelegateIdentity] = None
    port_numbers: typing_extensions.Annotated[
        typing.Optional[typing.List[int]], FieldMetadata(alias="portNumbers"), pydantic.Field(alias="portNumbers")
    ] = None
    scope: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
