

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Auth_Oauth(UniversalBaseModel):
    type: typing.Literal["oauth"] = "oauth"
    refresh: str
    access: str
    expires: float
    account_id: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="accountId"), pydantic.Field(alias="accountId")
    ] = None
    enterprise_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="enterpriseUrl"), pydantic.Field(alias="enterpriseUrl")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Auth_Api(UniversalBaseModel):
    type: typing.Literal["api"] = "api"
    key: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class Auth_Wellknown(UniversalBaseModel):
    type: typing.Literal["wellknown"] = "wellknown"
    key: str
    token: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


Auth = typing_extensions.Annotated[
    typing.Union[Auth_Oauth, Auth_Api, Auth_Wellknown], pydantic.Field(discriminator="type")
]
