

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ab_cd import AbCd
from .abc import Abc
from .e_fg_h import EFgH
from .kl_mn import KlMn
from .mn import Mn
from .pqr import Pqr
from .uvw import Uvw


class Roster(UniversalBaseModel):
    first: typing.Optional[Abc] = None
    second: typing.Optional[Pqr] = None
    third: typing.Optional[Mn] = None
    fourth: typing.Optional[AbCd] = None
    fifth: typing.Optional[EFgH] = None
    sixth: typing.Optional[KlMn] = None
    lamp: typing.Optional[Uvw] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
