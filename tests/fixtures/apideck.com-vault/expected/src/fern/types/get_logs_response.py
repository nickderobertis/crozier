

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .links import Links
from .log import Log
from .meta import Meta


class GetLogsResponse(UniversalBaseModel):
    data: typing.List[Log]
    links: typing.Optional[Links] = None
    meta: typing.Optional[Meta] = None
    status: str = pydantic.Field()
    """
    HTTP Response Status
    """

    status_code: int = pydantic.Field()
    """
    HTTP Response Status Code
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
