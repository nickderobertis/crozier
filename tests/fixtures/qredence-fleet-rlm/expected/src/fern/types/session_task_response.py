

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class SessionTaskResponse(UniversalBaseModel):
    """
    Authorized read-only projection of the existing Session checkpoint.
    """

    revision: int
    goal: str
    decisions: typing.List[str]
    relevant_paths: typing.List[str]
    source_revisions: typing.Dict[str, str]
    completed_work: typing.List[str]
    pending_work: typing.List[str]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
