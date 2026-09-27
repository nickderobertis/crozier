

import typing

from ...types.billing_plan import BillingPlan
from ...types.billing_plan_aggregate import BillingPlanAggregate

GetBillingPlansV3Response = typing.Union[typing.List[BillingPlan], typing.List[BillingPlanAggregate]]
