

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Instruction(UniversalBaseModel):
    """
    Information about an instruction.
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the instruction
    """

    sequence: int = pydantic.Field()
    """
    Sequence position of the instruction
    """

    description: str = pydantic.Field()
    """
    instruction content
    """

    media_id: str = pydantic.Field()
    """
    mediaID associated to the instruction
    """

    entity_id: str = pydantic.Field()
    """
    entity ID the instruction belongs to
    """

    entity_type: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
