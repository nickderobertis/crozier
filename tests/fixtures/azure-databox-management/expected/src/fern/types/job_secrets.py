

import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .dc_access_security_code import DcAccessSecurityCode
from .job_secrets_job_secrets_type import JobSecretsJobSecretsType


class JobSecrets(UniversalBaseModel):
    """
    The base class for the secrets
    """

    dc_access_security_code: typing_extensions.Annotated[
        typing.Optional[DcAccessSecurityCode],
        FieldMetadata(alias="dcAccessSecurityCode"),
        pydantic.Field(
            alias="dcAccessSecurityCode", description="Dc Access Security Code for Customer Managed Shipping"
        ),
    ] = None
    """
    Dc Access Security Code for Customer Managed Shipping
    """

    job_secrets_type: typing_extensions.Annotated[
        JobSecretsJobSecretsType,
        FieldMetadata(alias="jobSecretsType"),
        pydantic.Field(alias="jobSecretsType", description="Used to indicate what type of job secrets object."),
    ]
    """
    Used to indicate what type of job secrets object.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
