

import typing

import pydantic
from ..core.pydantic_utilities import IS_PYDANTIC_V2, UniversalBaseModel
from .created_at import CreatedAt
from .created_by import CreatedBy
from .row_version import RowVersion
from .tax_rate_components_item import TaxRateComponentsItem
from .tax_rate_status import TaxRateStatus
from .updated_at import UpdatedAt
from .updated_by import UpdatedBy


class TaxRate(UniversalBaseModel):
    code: typing.Optional[str] = pydantic.Field(default=None)
    """
    Tax code assigned to identify this tax rate.
    """

    components: typing.Optional[typing.List[TaxRateComponentsItem]] = None
    created_at: typing.Optional[CreatedAt] = None
    created_by: typing.Optional[CreatedBy] = None
    description: typing.Optional[str] = pydantic.Field(default=None)
    """
    Description of tax rate
    """

    effective_tax_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    Effective tax rate
    """

    id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID assigned to identify this tax rate.
    """

    name: typing.Optional[str] = pydantic.Field(default=None)
    """
    Name assigned to identify this tax rate.
    """

    original_tax_rate_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    ID of the original tax rate from which the new tax rate is derived. Helps to understand the relationship between corresponding tax rate entities.
    """

    report_tax_type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Report Tax type to aggregate tax collected or paid for reporting purposes
    """

    row_version: typing.Optional[RowVersion] = None
    status: typing.Optional[TaxRateStatus] = pydantic.Field(default=None)
    """
    Tax rate status
    """

    tax_payable_account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the account for tax collected.
    """

    tax_remitted_account_id: typing.Optional[str] = pydantic.Field(default=None)
    """
    Unique identifier for the account for tax remitted.
    """

    total_tax_rate: typing.Optional[float] = pydantic.Field(default=None)
    """
    Not compounded sum of the components of a tax rate
    """

    type: typing.Optional[str] = pydantic.Field(default=None)
    """
    Tax type used to indicate the source of tax collected or paid
    """

    updated_at: typing.Optional[UpdatedAt] = None
    updated_by: typing.Optional[UpdatedBy] = None

    if IS_PYDANTIC_V2:
        model_config: typing.ClassVar[pydantic.ConfigDict] = pydantic.ConfigDict(extra="allow", frozen=True)
    else:

        class Config:
            frozen = True
            smart_union = True
            extra = pydantic.Extra.allow
