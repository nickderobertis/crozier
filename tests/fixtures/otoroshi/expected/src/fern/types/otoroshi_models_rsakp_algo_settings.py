

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_models_rsakp_algo_settings_type import OtoroshiModelsRsakpAlgoSettingsType


class OtoroshiModelsRsakpAlgoSettings(UniversalBaseModel):
    """
    Settings to use RSA signing algorithm from a certificate keypair
    """

    type: typing.Optional[OtoroshiModelsRsakpAlgoSettingsType] = pydantic.Field(default=None)
    """
    the kind of algosettings
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    SHA function size
    """

    cert_id: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="certId"),
        pydantic.Field(alias="certId", description="Certificate id"),
    ] = None
    """
    Certificate id
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
