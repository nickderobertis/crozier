

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AppsInclude(UniversalBaseModel):
    assets: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include app assets in the response
    """

    info: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include app information in the response
    """

    links: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include app links in the response
    """

    platforms: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include app platform information in the response
    """

    ratings: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include app ratings in the response
    """

    release: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Include app release information in the response
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
