

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class PassThroughQuery(UniversalBaseModel):
    example_downstream_property: typing.Optional[str] = pydantic.Field(default=None)
    """
    All passthrough query parameters are passed along to the connector as is (?pass_through[search]=leads becomes ?search=leads)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
