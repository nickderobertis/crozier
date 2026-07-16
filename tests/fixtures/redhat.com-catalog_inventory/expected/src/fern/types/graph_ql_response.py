

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GraphQlResponse(UniversalBaseModel):
    data: typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]] = pydantic.Field(default=None)
    """
    Results from the GraphQL query
    """

    errors: typing.Optional[typing.List[typing.Dict[str, typing.Optional[typing.Any]]]] = pydantic.Field(default=None)
    """
    Errors resulting from the GraphQL query
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
