

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class InvitationStateErrorResponse(UniversalBaseModel):
    """
    410-gone envelope emitted by writeInvitationStateError. `error`
    is always the literal "gone"; `reason` discriminates the cause
    (`expired` / `revoked` / `accepted` / `unknown`) for the
    frontend refusal matrix. `unknown` is the safe default for
    ErrInvitationNotFound — uniform 410 defends against token
    existence enumeration.
    """

    error: str
    reason: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
