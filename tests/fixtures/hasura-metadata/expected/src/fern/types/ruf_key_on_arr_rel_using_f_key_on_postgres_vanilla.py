

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ruf_key_on_arr_rel_using_f_key_on_postgres_vanilla_foreign_key_constraint_on import (
    RufKeyOnArrRelUsingFKeyOnPostgresVanillaForeignKeyConstraintOn,
)


class RufKeyOnArrRelUsingFKeyOnPostgresVanilla(UniversalBaseModel):
    foreign_key_constraint_on: RufKeyOnArrRelUsingFKeyOnPostgresVanillaForeignKeyConstraintOn

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
