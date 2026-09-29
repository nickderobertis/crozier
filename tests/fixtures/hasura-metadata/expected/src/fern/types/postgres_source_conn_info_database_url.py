

import typing

from .from_env import FromEnv
from .url_conf_from_params import UrlConfFromParams

PostgresSourceConnInfoDatabaseUrl = typing.Union[str, FromEnv, UrlConfFromParams]
