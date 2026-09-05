

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .page_params import PageParams
from .register_phone_next_page_level import RegisterPhoneNextPageLevel


class RegisterPhoneNextPage(UniversalBaseModel):
    name: str = pydantic.Field()
    """
    Code name to the front-end page. Ideally a PageStr
    """

    parameters: typing.Optional[PageParams] = None
    logger: typing.Optional[str] = None
    level: typing.Optional[RegisterPhoneNextPageLevel] = None
    message: str

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
