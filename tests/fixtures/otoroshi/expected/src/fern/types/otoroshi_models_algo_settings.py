

import typing

from .otoroshi_models_es_algo_settings import OtoroshiModelsEsAlgoSettings
from .otoroshi_models_eskp_algo_settings import OtoroshiModelsEskpAlgoSettings
from .otoroshi_models_hs_algo_settings import OtoroshiModelsHsAlgoSettings
from .otoroshi_models_jwks_algo_settings import OtoroshiModelsJwksAlgoSettings
from .otoroshi_models_kid_algo_settings import OtoroshiModelsKidAlgoSettings
from .otoroshi_models_rs_algo_settings import OtoroshiModelsRsAlgoSettings
from .otoroshi_models_rsakp_algo_settings import OtoroshiModelsRsakpAlgoSettings

OtoroshiModelsAlgoSettings = typing.Union[
    OtoroshiModelsEsAlgoSettings,
    OtoroshiModelsEskpAlgoSettings,
    OtoroshiModelsHsAlgoSettings,
    OtoroshiModelsJwksAlgoSettings,
    OtoroshiModelsKidAlgoSettings,
    OtoroshiModelsRsakpAlgoSettings,
    OtoroshiModelsRsAlgoSettings,
]
