

from __future__ import annotations

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class HarborEvent_Opened(UniversalBaseModel):
    kind: typing.Literal["opened"] = "opened"
    opened_harbor_id: typing_extensions.Annotated[
        str, FieldMetadata(alias="harbor_id"), pydantic.Field(alias="harbor_id")
    ]

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


class HarborEvent_Closed(UniversalBaseModel):
    kind: typing.Literal["closed"] = "closed"
    closed_on: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="closedAt"), pydantic.Field(alias="closedAt")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow


HarborEvent = typing_extensions.Annotated[
    typing.Union[HarborEvent_Opened, HarborEvent_Closed], pydantic.Field(discriminator="kind")
]
