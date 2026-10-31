

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class StoreProbeCheck_Failed(UniversalBaseModel):
    """
    The result of one contract check.
    """

    outcome: typing.Literal["failed"] = "failed"
    message: str
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StoreProbeCheck_Passed(UniversalBaseModel):
    """
    The result of one contract check.
    """

    outcome: typing.Literal["passed"] = "passed"
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class StoreProbeCheck_Unsupported(UniversalBaseModel):
    """
    The result of one contract check.
    """

    outcome: typing.Literal["unsupported"] = "unsupported"
    name: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


StoreProbeCheck = typing_extensions.Annotated[
    typing.Union[StoreProbeCheck_Failed, StoreProbeCheck_Passed, StoreProbeCheck_Unsupported],
    pydantic.Field(discriminator="outcome"),
]
