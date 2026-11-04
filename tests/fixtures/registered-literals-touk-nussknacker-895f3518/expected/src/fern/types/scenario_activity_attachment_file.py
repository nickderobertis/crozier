

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ScenarioActivityAttachmentFile_Available(UniversalBaseModel):
    status: typing.Literal["AVAILABLE"] = "AVAILABLE"
    id: int

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class ScenarioActivityAttachmentFile_Deleted(UniversalBaseModel):
    status: typing.Literal["DELETED"] = "DELETED"

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


ScenarioActivityAttachmentFile = typing_extensions.Annotated[
    typing.Union[ScenarioActivityAttachmentFile_Available, ScenarioActivityAttachmentFile_Deleted],
    pydantic.Field(discriminator="status"),
]
