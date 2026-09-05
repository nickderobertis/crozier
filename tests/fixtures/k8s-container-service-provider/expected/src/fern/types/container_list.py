

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .container import Container


class ContainerList(UniversalBaseModel):
    """
    Paginated list of container instances
    """

    containers: typing.Optional[typing.List[Container]] = None
    next_page_token: typing.Optional[str] = pydantic.Field(default=None)
    """
    Token for retrieving the next page of results
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
