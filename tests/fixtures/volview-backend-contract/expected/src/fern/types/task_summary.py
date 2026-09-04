

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class TaskSummary(UniversalBaseModel):
    """
    Advisory display metadata for one task in the picker. Pass-through: the client renders it but validates only id/title; every other field is OPTIONAL advisory display metadata a backend MAY omit, and the client never dispatches on it.
    """

    id: str
    title: str
    description: typing.Optional[str] = None
    category: typing.Optional[typing.List[str]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
