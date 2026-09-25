

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class UnsubscribeResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    not_removed: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of the names of channels that the user is already unsubscribed
    from, and hence doesn't need to be unsubscribed.
    """

    removed: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    A list of the names of channels which were unsubscribed from as a result
    of the query.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
