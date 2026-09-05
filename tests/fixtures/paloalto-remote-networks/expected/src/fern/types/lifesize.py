

import typing

from .lifesize_gb import LifesizeGb
from .lifesize_kb import LifesizeKb
from .lifesize_mb import LifesizeMb
from .lifesize_tb import LifesizeTb

Lifesize = typing.Union[LifesizeKb, LifesizeMb, LifesizeGb, LifesizeTb]
