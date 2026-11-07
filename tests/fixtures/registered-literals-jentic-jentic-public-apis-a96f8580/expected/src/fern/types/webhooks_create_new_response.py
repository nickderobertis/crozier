

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class WebhooksCreateNewResponse(UniversalBaseModel):
    id: typing.Optional[str] = None
    events: typing.Optional[typing.List[str]] = None
    target_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="targetURL"), pydantic.Field(alias="targetURL")
    ] = None
    company: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
