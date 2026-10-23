

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class DeleteWebhooksIdResponse(UniversalBaseModel):
    ok: typing.Optional[bool] = None
    paused_watchers: typing_extensions.Annotated[
        typing.Optional[int], FieldMetadata(alias="pausedWatchers"), pydantic.Field(alias="pausedWatchers")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
