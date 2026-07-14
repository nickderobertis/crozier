

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .get_consumers_response_data_item import GetConsumersResponseDataItem
from .links import Links
from .meta import Meta


class GetConsumersResponse(UniversalBaseModel):
    data: typing.List[GetConsumersResponseDataItem]
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
