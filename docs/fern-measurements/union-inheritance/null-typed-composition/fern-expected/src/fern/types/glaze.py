

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs
from .glaze_recipe_value import GlazeRecipeValue


class Glaze(UniversalBaseModel):
    name: str
    finish: "GlazeFinish"
    recipe: typing.Dict[str, typing.Optional[GlazeRecipeValue]]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


from .glaze_finish import GlazeFinish

update_forward_refs(Glaze, GlazeFinish=GlazeFinish)
