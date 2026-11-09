

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .health_incident import HealthIncident
from .product_status import ProductStatus


class InstitutionStatus(UniversalBaseModel):
    """
    The status of an institution is determined by the health of its Item logins, Transactions updates, Investments updates, Liabilities updates, Auth requests, Balance requests, Identity requests, Investments requests, and Liabilities requests. A login attempt is conducted during the initial Item add in Link. If there is not enough traffic to accurately calculate an institution's status, Plaid will return null rather than potentially inaccurate data.

    Institution status is accessible in the Dashboard and via the API using the `/institutions/get_by_id` endpoint with the `include_status` option set to true. Note that institution status is not available in the Sandbox environment.
    """

    auth: typing.Optional[ProductStatus] = None
    health_incidents: typing.Optional[typing.List[HealthIncident]] = pydantic.Field(default=None)
    """
    Details of recent health incidents associated with the institution.
    """

    identity: typing.Optional[ProductStatus] = None
    investments: typing.Optional[ProductStatus] = None
    investments_updates: typing.Optional[ProductStatus] = None
    item_logins: typing.Optional[ProductStatus] = None
    liabilities: typing.Optional[ProductStatus] = None
    liabilities_updates: typing.Optional[ProductStatus] = None
    transactions_updates: typing.Optional[ProductStatus] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
