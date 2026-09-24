

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .entry_point_http_method import EntryPointHttpMethod
from .entry_point_parameter import EntryPointParameter


class EntryPoint(UniversalBaseModel):
    content_types: typing.List[str] = pydantic.Field()
    """
    The supported MIME type(s) for an EntryPoint response.
    """

    description: str = pydantic.Field()
    """
    A short description of the action. Optional - may be null.
    """

    encoding_types: typing.List[str] = pydantic.Field()
    """
    The supported MIME type(s) for an EntryPoint request. Null if not applicable.
    """

    http_method: EntryPointHttpMethod = pydantic.Field()
    """
    The HTTP method used by the EntryPoint.
    """

    name: str = pydantic.Field()
    """
    A word or short phrase to be used as the action's display name. Optional - may be null.
    """

    parameters: typing.List[EntryPointParameter] = pydantic.Field()
    """
    Descriptions of the EntryPoint parameters. Null if not applicable.
    """

    url: str = pydantic.Field()
    """
    The EntryPoint URL. It will be non-null if url_template is null.
    """

    url_template: str = pydantic.Field()
    """
    The EntryPoint's URL template. Only required if the entry point URL is parameterized. Property 'url' will be null if url_template is non-null.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
