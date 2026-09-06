

import typing

import pydantic
import typing_extensions
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...core.serialization import FieldMetadata


class GetFeedsFromOpmlTextResponseFeedsItem(UniversalBaseModel):
    title: typing.Optional[str] = None
    feed_url: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="feedUrl"), pydantic.Field(alias="feedUrl")
    ] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
