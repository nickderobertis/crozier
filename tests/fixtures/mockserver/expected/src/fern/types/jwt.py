

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .string_or_json_schema import StringOrJsonSchema


class Jwt(UniversalBaseModel):
    """
    JSON Web Token (JWT) request matcher — decodes the token carried in a request header (no signature verification) and matches its claims
    """

    header: typing.Optional[str] = pydantic.Field(default=None)
    """
    name of the request header carrying the JWT (default 'authorization')
    """

    scheme: typing.Optional[str] = pydantic.Field(default=None)
    """
    authentication scheme prefix stripped from the header value before decoding (default 'Bearer')
    """

    claims: typing.Optional[typing.Dict[str, StringOrJsonSchema]] = pydantic.Field(default=None)
    """
    claim-value criteria; each value may be an exact string, regex or '!'-negated form
    """

    issuer: typing.Optional[StringOrJsonSchema] = None
    audience: typing.Optional[StringOrJsonSchema] = None
    algorithm: typing.Optional[StringOrJsonSchema] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(Jwt)
