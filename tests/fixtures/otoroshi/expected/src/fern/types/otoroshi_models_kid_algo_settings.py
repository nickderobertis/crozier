

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .otoroshi_models_kid_algo_settings_type import OtoroshiModelsKidAlgoSettingsType


class OtoroshiModelsKidAlgoSettings(UniversalBaseModel):
    """
    Settings to find keypair based on header kid for verification
    """

    type: typing.Optional[OtoroshiModelsKidAlgoSettingsType] = pydantic.Field(default=None)
    """
    the kind of algosettings
    """

    only_exposed_certs: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="onlyExposedCerts"),
        pydantic.Field(alias="onlyExposedCerts", description="Use only exposed certs"),
    ] = None
    """
    Use only exposed certs
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
