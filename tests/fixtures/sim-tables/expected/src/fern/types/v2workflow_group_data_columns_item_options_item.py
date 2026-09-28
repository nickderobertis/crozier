

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V2WorkflowGroupDataColumnsItemOptionsItem(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Stable select-option identifier.
    """

    name: str = pydantic.Field()
    """
    Display name of the select option.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
