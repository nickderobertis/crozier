

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V2WorkflowGetJobResponseError(UniversalBaseModel):
    """
    Present once status is ``failed``.
    """

    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Stable error code (``internal_error`` when unmapped).
    """

    message: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
