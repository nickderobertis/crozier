

import typing

from ...types.enrollment_analytics import EnrollmentAnalytics
from ...types.enrollment_monthly import EnrollmentMonthly
from ...types.enrollment_period_analytics import EnrollmentPeriodAnalytics
from ...types.enrollment_trend import EnrollmentTrend

GetEnrollmentsV3Response = typing.Union[
    typing.List[EnrollmentMonthly],
    typing.List[EnrollmentAnalytics],
    typing.List[EnrollmentPeriodAnalytics],
    typing.List[EnrollmentTrend],
]
