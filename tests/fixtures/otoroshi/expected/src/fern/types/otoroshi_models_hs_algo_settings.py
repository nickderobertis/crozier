

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .otoroshi_models_hs_algo_settings_type import OtoroshiModelsHsAlgoSettingsType


class OtoroshiModelsHsAlgoSettings(UniversalBaseModel):
    """
    Settings to use HMAC-SHA signing algorithm
    """

    type: typing.Optional[OtoroshiModelsHsAlgoSettingsType] = pydantic.Field(default=None)
    """
    the kind of algosettings
    """

    size: typing.Optional[int] = pydantic.Field(default=None)
    """
    Size for SHA function
    """

    secret: typing.Optional[str] = pydantic.Field(default=None)
    """
    HMAC secret
    """

    base64: typing.Optional[bool] = pydantic.Field(default=None)
    """
    The secret is base64 encoded
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
