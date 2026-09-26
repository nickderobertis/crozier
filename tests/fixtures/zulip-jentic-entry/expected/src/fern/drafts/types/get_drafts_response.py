

import typing

import pydantic
from ...core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ...types.draft import Draft


class GetDraftsResponse(UniversalBaseModel):
    result: typing.Optional[typing.Any] = None
    msg: typing.Optional[typing.Any] = None
    ignored_parameters_unsupported: typing.Optional[typing.Any] = None
    count: typing.Optional[int] = pydantic.Field(default=None)
    """
    The number of drafts the user currently has. Also the
    number of drafts returned under "drafts".
    """

    drafts: typing.Optional[typing.List[Draft]] = pydantic.Field(default=None)
    """
    Returns all of the current user's drafts, in order of last edit time
    (with the most recently edited draft appearing first).
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
