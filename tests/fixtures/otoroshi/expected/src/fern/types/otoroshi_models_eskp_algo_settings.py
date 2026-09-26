

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_models_eskp_algo_settings_type import OtoroshiModelsEskpAlgoSettingsType


class OtoroshiModelsEskpAlgoSettings(UniversalBaseModel):
    """
    Settings to use elliptic curve signing algorithm from a certificate keypair
    """

    type: typing.Optional[OtoroshiModelsEskpAlgoSettingsType] = pydantic.Field(default=None)
    """
    the kind of algosettings
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Size of the key
    """

    cert_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="certId"),
        pydantic.Field(alias="certId", description="Certificate id to use the keypair"),
    ] = None
    """
    Certificate id to use the keypair
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
