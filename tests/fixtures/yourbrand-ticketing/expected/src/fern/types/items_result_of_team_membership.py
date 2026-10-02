

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .team_membership import TeamMembership


class ItemsResultOfTeamMembership(UniversalBaseModel):
    items: typing.Optional[typing.List[TeamMembership]] = None
    total_items: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="totalItems"), pydantic.Field(alias="totalItems")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
