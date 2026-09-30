

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .rel_def_rel_using_postgres_citus_obj_rel_using_choice_postgres_citus_using import (
    RelDefRelUsingPostgresCitusObjRelUsingChoicePostgresCitusUsing,
)


class RelDefRelUsingPostgresCitusObjRelUsingChoicePostgresCitus(UniversalBaseModel):
    comment: typing.Optional[str] = None
    name: str
    using: RelDefRelUsingPostgresCitusObjRelUsingChoicePostgresCitusUsing

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
