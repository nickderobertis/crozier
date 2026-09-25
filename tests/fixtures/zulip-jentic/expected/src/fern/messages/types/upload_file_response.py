

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UploadFileResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    uri: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the uploaded file. Alias of `url`.
    
    **Changes**: Deprecated in Zulip 9.0 (feature level 272). The term
    "URI" is deprecated in [web standards](https://url.spec.whatwg.org/#goals).
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The URL of the uploaded file.
    
    **Changes**: New in Zulip 9.0 (feature level 272). Previously,
    this property was only available under the legacy `uri` name.
    """

    filename: typing.Optional[str] = pydantic.Field(default=None)
    """
    The filename that Zulip stored the upload as. This usually
    differs from the basename of the URL when HTML escaping is
    required to generate a valid URL.
    
    Clients generating a Markdown link to a newly uploaded file
    should do so by combining the `url` and `filename` fields in the
    response as follows: `[{filename}]({url})`, with care taken to
    clean `filename` of `[` and `]` characters that might break
    Markdown rendering.
    
    **Changes**: New in Zulip 10.0 (feature level 285).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
