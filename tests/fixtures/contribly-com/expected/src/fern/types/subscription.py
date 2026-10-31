

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata


class Subscription(UniversalBaseModel):
    assignment: typing.Optional[str] = None
    email: typing.Optional[str] = None
    id: str
    include_body: typing_extensions.Annotated[
        bool, FieldMetadata(alias="includeBody"), pydantic.Field(alias="includeBody")
    ]
    include_thumbenail: typing_extensions.Annotated[
        typing.Optional[bool], FieldMetadata(alias="includeThumbenail"), pydantic.Field(alias="includeThumbenail")
    ] = None
    slack_channel: typing_extensions.Annotated[
        typing.Optional[str], FieldMetadata(alias="slackChannel"), pydantic.Field(alias="slackChannel")
    ] = None
    token: str
    types: typing.List[str]
    user: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
