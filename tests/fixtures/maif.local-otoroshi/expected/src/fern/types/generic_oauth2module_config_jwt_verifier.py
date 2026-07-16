

import typing

from .es_algo_settings import EsAlgoSettings
from .hs_algo_settings import HsAlgoSettings
from .jwks_algo_settings import JwksAlgoSettings
from .rs_algo_settings import RsAlgoSettings

GenericOauth2ModuleConfigJwtVerifier = typing.Union[HsAlgoSettings, RsAlgoSettings, EsAlgoSettings, JwksAlgoSettings]
