

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2
from .journal_problem import JournalProblem


class BadRequestErrorBody(JournalProblem):
    """
    The reservation is already occupied.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
