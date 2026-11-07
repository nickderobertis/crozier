

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel


class AwsRoleConfig(UniversalBaseModel):
    """
    Configuration needed to set up an IAM role trust policy for role-based authentication on AWS routes
    """

    aws_account_id: str = pydantic.Field()
    """
    The Blues AWS Account ID to trust in your IAM role's trust policy
    """

    external_id: str = pydantic.Field()
    """
    The External ID to use in your IAM role's trust policy condition
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
