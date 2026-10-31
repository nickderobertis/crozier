

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class MachineHealthIssue(UniversalBaseModel):
    """
    Flags the underlying machine for repair.
    """

    category: str = pydantic.Field()
    """
    Issue category: one of Hardware, Network, Performance or Other.
    """

    summary: str = pydantic.Field()
    """
    Short summary, 2 to 256 characters.
    """

    details: typing.Optional[str] = pydantic.Field(default=None)
    """
    Additional detail, 2 to 256 characters.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
