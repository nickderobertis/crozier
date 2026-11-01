

from __future__ import annotations

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel, update_forward_refs


class CloudError(UniversalBaseModel):
    """
    The error information object.
    """

    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error code string.
    """

    details: typing.Optional[typing.List["CloudError"]] = pydantic.Field(default=None)
    """
    More detailed error information.
    """

    message: typing.Optional[str] = pydantic.Field(default=None)
    """
    Descriptive error information.
    """

    target: typing.Optional[str] = pydantic.Field(default=None)
    """
    Error target
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


update_forward_refs(CloudError)
