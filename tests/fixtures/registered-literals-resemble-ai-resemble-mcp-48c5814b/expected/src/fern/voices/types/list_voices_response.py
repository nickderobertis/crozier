

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ListVoicesResponse(UniversalBaseModel):
    success: typing.Optional[bool] = None
    page: typing.Optional[int] = None
    num_pages: typing.Optional[int] = None
    page_size: typing.Optional[int] = None
    items: typing.Optional[typing.List[typing.Dict[str, typing.Any]]] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
