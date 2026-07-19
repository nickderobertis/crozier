

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .conflict_error_body_item_headers import ConflictErrorBodyItemHeaders


class ConflictErrorBodyItem(UniversalBaseModel):
    """
    Message object
    """

    headers: typing.Optional[ConflictErrorBodyItemHeaders] = pydantic.Field(default=None)
    """
    Metadata describing the control message.
    
    The `control` message returned will be a `must-refetch` message,
    which a client should detect and throw away any local data and
    re-sync from scratch using the new shape handle available in the
    `electric-handle` header of the response.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
