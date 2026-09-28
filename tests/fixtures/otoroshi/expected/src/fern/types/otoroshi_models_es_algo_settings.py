

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_models_es_algo_settings_private_key import OtoroshiModelsEsAlgoSettingsPrivateKey
from .otoroshi_models_es_algo_settings_type import OtoroshiModelsEsAlgoSettingsType


class OtoroshiModelsEsAlgoSettings(UniversalBaseModel):
    """
    Settings to use elliptic curve signing algorithm
    """

    type: typing.Optional[OtoroshiModelsEsAlgoSettingsType] = pydantic.Field(default=None)
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
        pydantic.Field(alias="publicKey", description="The EC private key. If used for signing, can be null"),
    ] = None
    """
    The EC private key. If used for signing, can be null
    """

    private_key: typing_extensions.Annotated[
        typing.Optional[OtoroshiModelsEsAlgoSettingsPrivateKey],
        FieldMetadata(alias="privateKey"),
        pydantic.Field(alias="privateKey", description="The EC private key. If used for verification, can be null"),
    ] = None
    """
    The EC private key. If used for verification, can be null
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
