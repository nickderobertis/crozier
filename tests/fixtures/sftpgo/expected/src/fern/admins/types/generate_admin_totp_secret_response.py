

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GenerateAdminTotpSecretResponse(UniversalBaseModel):
    config_name: typing.Optional[str] = None
    issuer: typing.Optional[str] = None
    secret: typing.Optional[str] = None
    url: typing.Optional[str] = None
    qr_code: typing.Optional[str] = pydantic.Field(default=None)
    """
    QR code png encoded as BASE64
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
