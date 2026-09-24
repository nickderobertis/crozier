

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1LabelsCreateLabel(UniversalBaseModel):
    name: str
    emoji: typing.Optional[str] = None
    parent_id: typing.Optional[int] = None
    sequence: typing.Optional[int] = None
    active: typing.Optional[bool] = None
    external_id: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
