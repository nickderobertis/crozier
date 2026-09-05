

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Viewer(UniversalBaseModel):
    """
    API model for a viewer resource

    A viewer is a service with an associated filetype.
    You can think of it as a tuple (filetype, service)

    The service could consume other filetypes BUT at this
    interface this is represented in yet another viewer resource

    For instance, the same service can be in two different viewer resources
      - viewer1=(JPEG, RawGraph service)
      - viewer2=(CSV, RawGraph service)

    A viewer can be dispatched using the view_url and appending the
    """

    title: str = pydantic.Field()
    """
    Short formatted label with name and version of the viewer
    """

    file_type: str = pydantic.Field()
    """
    Identifier for the file type
    """

    view_url: str = pydantic.Field()
    """
    Base url to execute viewer. Needs appending file_size,[file_name] and download_link as query parameters
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
