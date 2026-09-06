

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .secret_status import SecretStatus


class Secret(UniversalBaseModel):
    """
    The secret is encrypted before saving, so to set a new secret you must provide a payload and set the status to "Plain". The encryption key and additional data will be generated automatically. If you set the status to "Redacted" the existing secret will be preserved
    """

    status: typing.Optional[SecretStatus] = pydantic.Field(default=None)
    """
    Set to "Plain" to add or update an existing secret, set to "Redacted" to preserve the existing value
    """

    payload: typing.Optional[str] = None
    key: typing.Optional[str] = None
    additional_data: typing.Optional[str] = None
    mode: typing.Optional[int] = pydantic.Field(default=None)
    """
    1 means encrypted using a master key
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
