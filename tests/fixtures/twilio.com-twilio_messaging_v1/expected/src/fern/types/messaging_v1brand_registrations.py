

import datetime as dt
import typing

import pydantic
import typing_extensions
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from ..core.serialization import FieldMetadata
from .brand_registrations_enum_brand_feedback import BrandRegistrationsEnumBrandFeedback
from .brand_registrations_enum_identity_status import BrandRegistrationsEnumIdentityStatus
from .brand_registrations_enum_status import BrandRegistrationsEnumStatus


class MessagingV1BrandRegistrations(UniversalBaseModel):
    a2p_profile_bundle_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    A2P Messaging Profile Bundle BundleSid.
    """

    account_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Brand Registration resource.
    """

    brand_feedback: typing.Optional[typing.List[BrandRegistrationsEnumBrandFeedback]] = pydantic.Field(default=None)
    """
    Feedback on how to improve brand score
    """

    brand_score: typing.Optional[int] = pydantic.Field(default=None)
    """
    The secondary vetting score if it was done. Otherwise, it will be the brand score if it's returned from TCR. It may be null if no score is available.
    """

    brand_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Type of brand. One of: "STANDARD", "SOLE_PROPRIETOR". SOLE_PROPRIETOR is for the low volume, SOLE_PROPRIETOR campaign use case. There can only be one SOLE_PROPRIETOR campaign created per SOLE_PROPRIETOR brand. STANDARD is for all other campaign use cases. Multiple campaign use cases can be created per STANDARD brand.
    """

    customer_profile_bundle_sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    A2P Messaging Profile Bundle BundleSid.
    """

    date_created: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time in GMT when the resource was created specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    date_updated: typing.Optional[dt.datetime] = pydantic.Field(default=None)
    """
    The date and time in GMT when the resource was last updated specified in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format.
    """

    failure_reason: typing.Optional[str] = pydantic.Field(default=None)
    """
    A reason why brand registration has failed. Only applicable when status is FAILED.
    """

    government_entity: typing.Optional[bool] = pydantic.Field(default=None)
    """
    Identified as a government entity
    """

    identity_status: typing.Optional[BrandRegistrationsEnumIdentityStatus] = pydantic.Field(default=None)
    """
    When a brand is registered, TCR will attempt to verify the identity of the brand based on the supplied information.
    """

    links: typing.Optional[typing.Dict[str, typing.Any]] = None
    mock: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A boolean that specifies whether brand should be a mock or not. If true, brand will be registered as a mock brand. Defaults to false if no value is provided.
    """

    russell3000: typing_extensions.Annotated[
        typing.Optional[bool],
        FieldMetadata(alias="russell_3000"),
        pydantic.Field(
            alias="russell_3000", description="Publicly traded company identified in the Russell 3000 Index"
        ),
    ] = None
    """
    Publicly traded company identified in the Russell 3000 Index
    """

    sid: typing.Optional[str] = pydantic.Field(default=None)
    """
    The unique string to identify Brand Registration.
    """

    skip_automatic_sec_vet: typing.Optional[bool] = pydantic.Field(default=None)
    """
    A flag to disable automatic secondary vetting for brands which it would otherwise be done.
    """

    status: typing.Optional[BrandRegistrationsEnumStatus] = pydantic.Field(default=None)
    """
    Brand Registration status. One of "PENDING", "APPROVED", "FAILED", "IN_REVIEW", "DELETED".
    """

    tax_exempt_status: typing.Optional[str] = pydantic.Field(default=None)
    """
    Nonprofit organization tax-exempt status per section 501 of the U.S. tax code.
    """

    tcr_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Campaign Registry (TCR) Brand ID. Assigned only after successful brand registration.
    """

    url: typing.Optional[str] = pydantic.Field(default=None)
    """
    The absolute URL of the Brand Registration resource.
    """

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
