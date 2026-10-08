

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ConsumerCapabilities(UniversalBaseModel):
    """
    Per-consumer access capabilities for a session connection.

        - editor: `{edit: True, interact: True}`
        - interactor: `{edit: False, interact: True}` (default for a secondary
          connection: drives UI state but cannot edit the notebook)
        - read-only viewer: `{edit: False, interact: False}` (opt-in, set by a
          deployment's capability provider)

        The server enforces these: control requests are gated against the issuing
        consumer's stored capabilities at the control-request chokepoint (the
        authority) and mirrored as an advisory HTTP 403 at the request handlers.
        Commands classified as `read` in `marimo._session.capabilities` (such as
        completions and previews) are always permitted.
    """

    edit: bool
    interact: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
