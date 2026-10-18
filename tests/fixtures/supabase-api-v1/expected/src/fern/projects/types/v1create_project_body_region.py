

import typing

from ...core import enum

T_Result = typing.TypeVar("T_Result")


class V1CreateProjectBodyRegion(enum.StrEnum):
    """
    Region you want your server to reside in. Use region_selection instead.
    """

    US_EAST1 = "us-east-1"
    US_EAST2 = "us-east-2"
    US_WEST1 = "us-west-1"
    US_WEST2 = "us-west-2"
    AP_EAST1 = "ap-east-1"
    AP_SOUTHEAST1 = "ap-southeast-1"
    AP_NORTHEAST1 = "ap-northeast-1"
    AP_NORTHEAST2 = "ap-northeast-2"
    AP_SOUTHEAST2 = "ap-southeast-2"
    EU_WEST1 = "eu-west-1"
    EU_WEST2 = "eu-west-2"
    EU_WEST3 = "eu-west-3"
    EU_NORTH1 = "eu-north-1"
    EU_CENTRAL1 = "eu-central-1"
    EU_CENTRAL2 = "eu-central-2"
    CA_CENTRAL1 = "ca-central-1"
    AP_SOUTH1 = "ap-south-1"
    SA_EAST1 = "sa-east-1"

    def visit(
        self,
        us_east1: typing.Callable[[], T_Result],
        us_east2: typing.Callable[[], T_Result],
        us_west1: typing.Callable[[], T_Result],
        us_west2: typing.Callable[[], T_Result],
        ap_east1: typing.Callable[[], T_Result],
        ap_southeast1: typing.Callable[[], T_Result],
        ap_northeast1: typing.Callable[[], T_Result],
        ap_northeast2: typing.Callable[[], T_Result],
        ap_southeast2: typing.Callable[[], T_Result],
        eu_west1: typing.Callable[[], T_Result],
        eu_west2: typing.Callable[[], T_Result],
        eu_west3: typing.Callable[[], T_Result],
        eu_north1: typing.Callable[[], T_Result],
        eu_central1: typing.Callable[[], T_Result],
        eu_central2: typing.Callable[[], T_Result],
        ca_central1: typing.Callable[[], T_Result],
        ap_south1: typing.Callable[[], T_Result],
        sa_east1: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is V1CreateProjectBodyRegion.US_EAST1:
            return us_east1()
        if self is V1CreateProjectBodyRegion.US_EAST2:
            return us_east2()
        if self is V1CreateProjectBodyRegion.US_WEST1:
            return us_west1()
        if self is V1CreateProjectBodyRegion.US_WEST2:
            return us_west2()
        if self is V1CreateProjectBodyRegion.AP_EAST1:
            return ap_east1()
        if self is V1CreateProjectBodyRegion.AP_SOUTHEAST1:
            return ap_southeast1()
        if self is V1CreateProjectBodyRegion.AP_NORTHEAST1:
            return ap_northeast1()
        if self is V1CreateProjectBodyRegion.AP_NORTHEAST2:
            return ap_northeast2()
        if self is V1CreateProjectBodyRegion.AP_SOUTHEAST2:
            return ap_southeast2()
        if self is V1CreateProjectBodyRegion.EU_WEST1:
            return eu_west1()
        if self is V1CreateProjectBodyRegion.EU_WEST2:
            return eu_west2()
        if self is V1CreateProjectBodyRegion.EU_WEST3:
            return eu_west3()
        if self is V1CreateProjectBodyRegion.EU_NORTH1:
            return eu_north1()
        if self is V1CreateProjectBodyRegion.EU_CENTRAL1:
            return eu_central1()
        if self is V1CreateProjectBodyRegion.EU_CENTRAL2:
            return eu_central2()
        if self is V1CreateProjectBodyRegion.CA_CENTRAL1:
            return ca_central1()
        if self is V1CreateProjectBodyRegion.AP_SOUTH1:
            return ap_south1()
        if self is V1CreateProjectBodyRegion.SA_EAST1:
            return sa_east1()
