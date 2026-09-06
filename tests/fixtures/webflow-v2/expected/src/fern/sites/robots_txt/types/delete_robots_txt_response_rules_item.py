

import typing

import pydantic
import typing_extensions
from ....core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ....core.serialization import FieldMetadata


class DeleteRobotsTxtResponseRulesItem(UniversalBaseModel):
    user_agent: typing_extensions.Annotated[
        str,
        FieldMetadata(alias="userAgent"),
        pydantic.Field(alias="userAgent", description="The user agent the rules apply to."),
    ]
    """
    The user agent the rules apply to.
    """

    allows: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of paths allowed for this user agent.
    """

    disallows: typing.Optional[typing.List[str]] = pydantic.Field(default=None)
    """
    List of paths disallowed for this user agent.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
