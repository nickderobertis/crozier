

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class Pass(UniversalBaseModel):
    """
    The keys to a session, not the session itself. The access token is short-lived and travels in Authorization on every request. The refresh token is long-lived and buys a fresh pair once the access token dies; it is the one worth stealing, and belongs where scripts cannot reach it.
    Both lifetimes are counted from the moment this answer arrives rather than named as instants. Their holder acts on them, and naming an instant would send it to its own clock — the one thing here not worth trusting. A phone kept off the network drifts by minutes, and an access token lives fifteen.
    """

    access_token: str
    access_expires_in: int = pydantic.Field()
    """
    Seconds the access token will be accepted for.
    """

    refresh_token: str
    refresh_expires_in: int = pydantic.Field()
    """
    Seconds the refresh token will be accepted for. Starts over with every refresh: a session dies from disuse, not from age.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
