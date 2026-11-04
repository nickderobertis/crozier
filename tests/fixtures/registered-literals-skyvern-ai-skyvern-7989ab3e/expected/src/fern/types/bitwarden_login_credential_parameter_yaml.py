

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class BitwardenLoginCredentialParameterYaml(UniversalBaseModel):
    key: str
    description: typing.Optional[str] = None
    bitwarden_client_id_aws_secret_key: str
    bitwarden_client_secret_aws_secret_key: str
    bitwarden_master_password_aws_secret_key: str
    url_parameter_key: typing.Optional[str] = None
    bitwarden_collection_id: typing.Optional[str] = None
    bitwarden_item_id: typing.Optional[str] = None
    totp_identifier: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
