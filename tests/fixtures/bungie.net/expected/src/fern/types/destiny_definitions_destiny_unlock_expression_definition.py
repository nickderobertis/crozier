

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class DestinyDefinitionsDestinyUnlockExpressionDefinition(UniversalBaseModel):
    """
    Where the sausage gets made. Unlock Expressions are the foundation of the game's gating mechanics and investment-related restrictions. They can test Unlock Flags and Unlock Values for certain states, using a sufficient amount of logical operators such that unlock expressions are effectively Turing complete.
    Use UnlockExpressionParser to evaluate expressions using an IUnlockContext parsed from Babel.
    """

    scope: typing.Optional[int] = pydantic.Field(default=None)
    """
    A shortcut for determining the most restrictive gating that this expression performs. See the DestinyGatingScope enum's documentation for more details.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
