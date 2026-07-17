

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .account_limit import AccountLimit


class DescribeAccountLimitsOutput(UniversalBaseModel):
    """
    The output for the <a>DescribeAccountLimits</a> action.
    """

    account_limits: typing_extensions.Annotated[
        typing.Optional[typing.List[AccountLimit]],
        FieldMetadata(alias="AccountLimits"),
        pydantic.Field(
            alias="AccountLimits",
            description="An account limit structure that contain a list of CloudFormation account limits and their values.",
        ),
    ] = None
    """
    An account limit structure that contain a list of CloudFormation account limits and their values.
    """

    next_token: typing_extensions.Annotated[
        typing.Optional[str],
        FieldMetadata(alias="NextToken"),
        pydantic.Field(
            alias="NextToken",
            description="If the output exceeds 1 MB in size, a string that identifies the next page of limits. If no additional page exists, this value is null.",
        ),
    ] = None
    """
    If the output exceeds 1 MB in size, a string that identifies the next page of limits. If no additional page exists, this value is null.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
