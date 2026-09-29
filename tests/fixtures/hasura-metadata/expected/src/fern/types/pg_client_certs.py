

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .cert_var import CertVar
from .ssl_mode import SslMode


class PgClientCerts(UniversalBaseModel):
    """
    https://hasura.io/docs/latest/graphql/core/api-reference/syntax-defs.html#pgcertsettings
    """

    sslcert: typing.Optional[CertVar] = None
    sslkey: typing.Optional[CertVar] = None
    sslmode: SslMode
    sslpassword: typing.Optional[CertVar] = None
    sslrootcert: typing.Optional[CertVar] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
