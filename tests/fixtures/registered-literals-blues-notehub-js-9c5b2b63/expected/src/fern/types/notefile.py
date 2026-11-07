

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .note import Note


class Notefile(UniversalBaseModel):
    id: str = pydantic.Field()
    """
    Notefile id (e.g., "test.qi", "config.db").
    """

    notes: typing.List[Note]
    template: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
