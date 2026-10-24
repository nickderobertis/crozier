

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class JsonWebKey(UniversalBaseModel):
    alg: typing.Optional[str] = None
    crv: typing.Optional[str] = None
    d: typing.Optional[str] = None
    dp: typing.Optional[str] = None
    dq: typing.Optional[str] = None
    e: typing.Optional[str] = None
    k: typing.Optional[str] = None
    key_ops: typing.Optional[typing.List[str]] = None
    kid: typing.Optional[str] = None
    kty: typing.Optional[str] = None
    n: typing.Optional[str] = None
    oth: typing.Optional[typing.List[str]] = None
    p: typing.Optional[str] = None
    q: typing.Optional[str] = None
    qi: typing.Optional[str] = None
    use: typing.Optional[str] = None
    x: typing.Optional[str] = None
    x5c: typing.Optional[typing.List[str]] = None
    x5t: typing.Optional[str] = None
    x5t_s256: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="x5t#S256"), pydantic.Field(alias="x5t#S256")
    ] = None
    x5u: typing.Optional[str] = None
    y: typing.Optional[str] = None
    pub: typing.Optional[str] = None
    priv: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
