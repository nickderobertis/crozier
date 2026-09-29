

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ruf_key_on_arr_rel_using_f_key_on_postgres_cockroach_foreign_key_constraint_on import (
    RufKeyOnArrRelUsingFKeyOnPostgresCockroachForeignKeyConstraintOn,
)


class RufKeyOnArrRelUsingFKeyOnPostgresCockroach(UniversalBaseModel):
    foreign_key_constraint_on: RufKeyOnArrRelUsingFKeyOnPostgresCockroachForeignKeyConstraintOn

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
