

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class V1HoursUpdateEventExternalLinksItem(UniversalBaseModel):
    provider_id: str
    provider_type: str
    external_id: str
    data: typing.Optional[typing.Dict[str, typing.Any]] = None
    uri: typing.Optional[str] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
