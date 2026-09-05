

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class ServiceGet(UniversalBaseModel):
    key: str = pydantic.Field()
    """
    Service key ID
    """

    title: str = pydantic.Field()
    """
    Service name for display
    """

    description: str = pydantic.Field()
    """
    Long description of the service
    """

    thumbnail: str = pydantic.Field()
    """
    Url to service thumbnail
    """

    file_extensions: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    File extensions that this service can process
    """

    view_url: str = pydantic.Field()
    """
    Redirection to open a service in osparc (see /view)
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
