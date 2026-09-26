

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_models_rs_algo_settings_private_key import OtoroshiModelsRsAlgoSettingsPrivateKey
from .otoroshi_models_rs_algo_settings_type import OtoroshiModelsRsAlgoSettingsType


class OtoroshiModelsRsAlgoSettings(UniversalBaseModel):
    """
    Settings to use RSA signing algorithm
    """

    type: typing.Optional[OtoroshiModelsRsAlgoSettingsType] = pydantic.Field(default=None)
    """
    the kind of algosettings
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    SHA function size
    """

    public_key: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="publicKey"),
        pydantic.Field(alias="publicKey", description="Public key (for verification)"),
    ] = None
    """
    Public key (for verification)
    """

    private_key: typing_extensions.Annotated[
        typing.Optional[OtoroshiModelsRsAlgoSettingsPrivateKey],
        FieldMetadata(alias="privateKey"),
        pydantic.Field(alias="privateKey", description="Private key (for signing)"),
    ] = None
    """
    Private key (for signing)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
