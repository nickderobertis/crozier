

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .v2forbidden_detail_code import V2ForbiddenDetailCode


class V2ActionableForbiddenDetails(UniversalBaseModel):
    """
    Machine-readable cause and optional context for an actionable `403` response.
    """

    code: V2ForbiddenDetailCode

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
