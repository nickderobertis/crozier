

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class LspRestartResponse(UniversalBaseModel):
    """
    Response from restart operation.
    """

    errors: typing.Optional[typing.Dict[str, str]] = None
    restarted: typing.List[str]
    success: bool

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
