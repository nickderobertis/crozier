

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class GlitchtipUser(UniversalBaseModel):
    """
    Desired state for a single Glitchtip organization user.
    """

    email: str = pydantic.Field()
    """
    User email address
    """

    role: typing.Optional[str] = pydantic.Field(default=None)
    """
    Organization role
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
