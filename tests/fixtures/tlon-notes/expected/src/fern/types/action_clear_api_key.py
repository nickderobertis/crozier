

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ActionClearApiKey(UniversalBaseModel):
    """
    Erase the stored `X-Api-Key`. Disables the bypass entirely —
    afterward only eyre-cookie-authenticated requests pass the v1
    dispatch gate. Re-mint via `regenerate-api-key`.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
