

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .ruf_key_on_obj_rel_using_choice_postgres_citus_foreign_key_constraint_on import (
    RufKeyOnObjRelUsingChoicePostgresCitusForeignKeyConstraintOn,
)


class RufKeyOnObjRelUsingChoicePostgresCitus(UniversalBaseModel):
    foreign_key_constraint_on: RufKeyOnObjRelUsingChoicePostgresCitusForeignKeyConstraintOn

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
