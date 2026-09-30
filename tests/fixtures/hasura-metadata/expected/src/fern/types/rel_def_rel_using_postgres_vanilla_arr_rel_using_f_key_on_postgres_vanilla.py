

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .rel_def_rel_using_postgres_vanilla_arr_rel_using_f_key_on_postgres_vanilla_using import (
    RelDefRelUsingPostgresVanillaArrRelUsingFKeyOnPostgresVanillaUsing,
)


class RelDefRelUsingPostgresVanillaArrRelUsingFKeyOnPostgresVanilla(UniversalBaseModel):
    comment: typing.Optional[str] = None
    name: str
    using: RelDefRelUsingPostgresVanillaArrRelUsingFKeyOnPostgresVanillaUsing

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
