

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class SourceStripeConfigApiVersion(enum.StrEnum):
    TWO_THOUSAND_TWENTY_SIX0325DAHLIA = "2026-03-25.dahlia"
    TWO_THOUSAND_TWENTY_SIX0225CLOVER = "2026-02-25.clover"
    TWO_THOUSAND_TWENTY_SIX0128CLOVER = "2026-01-28.clover"
    TWO_THOUSAND_TWENTY_FIVE1215CLOVER = "2025-12-15.clover"
    TWO_THOUSAND_TWENTY_FIVE1117CLOVER = "2025-11-17.clover"
    TWO_THOUSAND_TWENTY_FIVE1029CLOVER = "2025-10-29.clover"
    TWO_THOUSAND_TWENTY_FIVE0930CLOVER = "2025-09-30.clover"
    TWO_THOUSAND_TWENTY_FIVE0827BASIL = "2025-08-27.basil"
    TWO_THOUSAND_TWENTY_FIVE0730BASIL = "2025-07-30.basil"
    TWO_THOUSAND_TWENTY_FIVE0630BASIL = "2025-06-30.basil"
    TWO_THOUSAND_TWENTY_FIVE0528BASIL = "2025-05-28.basil"
    TWO_THOUSAND_TWENTY_FIVE0430BASIL = "2025-04-30.basil"
    TWO_THOUSAND_TWENTY_FIVE0331BASIL = "2025-03-31.basil"
    TWO_THOUSAND_TWENTY_FIVE0224ACACIA = "2025-02-24.acacia"
    TWO_THOUSAND_TWENTY_FIVE0127ACACIA = "2025-01-27.acacia"
    TWO_THOUSAND_TWENTY_FOUR1218ACACIA = "2024-12-18.acacia"
    TWO_THOUSAND_TWENTY_FOUR1120ACACIA = "2024-11-20.acacia"
    TWO_THOUSAND_TWENTY_FOUR1028ACACIA = "2024-10-28.acacia"
    TWO_THOUSAND_TWENTY_FOUR0930ACACIA = "2024-09-30.acacia"
    TWO_THOUSAND_TWENTY_FOUR0620 = "2024-06-20"
    TWO_THOUSAND_TWENTY_FOUR0410 = "2024-04-10"
    TWO_THOUSAND_TWENTY_FOUR0403 = "2024-04-03"
    TWO_THOUSAND_TWENTY_THREE1016 = "2023-10-16"
    TWO_THOUSAND_TWENTY_THREE0816 = "2023-08-16"
    TWO_THOUSAND_TWENTY_TWO1115 = "2022-11-15"
    TWO_THOUSAND_TWENTY_TWO0801 = "2022-08-01"
    TWO_THOUSAND_TWENTY0827 = "2020-08-27"
    TWO_THOUSAND_TWENTY0302 = "2020-03-02"
    TWO_THOUSAND_NINETEEN1203 = "2019-12-03"
    TWO_THOUSAND_NINETEEN1105 = "2019-11-05"
    TWO_THOUSAND_NINETEEN1017 = "2019-10-17"
    TWO_THOUSAND_NINETEEN1008 = "2019-10-08"
    TWO_THOUSAND_NINETEEN0909 = "2019-09-09"
    TWO_THOUSAND_NINETEEN0814 = "2019-08-14"
    TWO_THOUSAND_NINETEEN0516 = "2019-05-16"
    TWO_THOUSAND_NINETEEN0314 = "2019-03-14"
    TWO_THOUSAND_NINETEEN0219 = "2019-02-19"
    TWO_THOUSAND_NINETEEN0211 = "2019-02-11"
    TWO_THOUSAND_EIGHTEEN1108 = "2018-11-08"
    TWO_THOUSAND_EIGHTEEN1031 = "2018-10-31"
    TWO_THOUSAND_EIGHTEEN0924 = "2018-09-24"
    TWO_THOUSAND_EIGHTEEN0906 = "2018-09-06"
    TWO_THOUSAND_EIGHTEEN0823 = "2018-08-23"
    TWO_THOUSAND_EIGHTEEN0727 = "2018-07-27"
    TWO_THOUSAND_EIGHTEEN0521 = "2018-05-21"
    TWO_THOUSAND_EIGHTEEN0228 = "2018-02-28"
    TWO_THOUSAND_EIGHTEEN0206 = "2018-02-06"
    TWO_THOUSAND_EIGHTEEN0205 = "2018-02-05"
    TWO_THOUSAND_EIGHTEEN0123 = "2018-01-23"
    TWO_THOUSAND_SEVENTEEN1214 = "2017-12-14"
    TWO_THOUSAND_SEVENTEEN0815 = "2017-08-15"

    def visit(
        self,
        two_thousand_twenty_six0325dahlia: typing.Callable[[], T_Result],
        two_thousand_twenty_six0225clover: typing.Callable[[], T_Result],
        two_thousand_twenty_six0128clover: typing.Callable[[], T_Result],
        two_thousand_twenty_five1215clover: typing.Callable[[], T_Result],
        two_thousand_twenty_five1117clover: typing.Callable[[], T_Result],
        two_thousand_twenty_five1029clover: typing.Callable[[], T_Result],
        two_thousand_twenty_five0930clover: typing.Callable[[], T_Result],
        two_thousand_twenty_five0827basil: typing.Callable[[], T_Result],
        two_thousand_twenty_five0730basil: typing.Callable[[], T_Result],
        two_thousand_twenty_five0630basil: typing.Callable[[], T_Result],
        two_thousand_twenty_five0528basil: typing.Callable[[], T_Result],
        two_thousand_twenty_five0430basil: typing.Callable[[], T_Result],
        two_thousand_twenty_five0331basil: typing.Callable[[], T_Result],
        two_thousand_twenty_five0224acacia: typing.Callable[[], T_Result],
        two_thousand_twenty_five0127acacia: typing.Callable[[], T_Result],
        two_thousand_twenty_four1218acacia: typing.Callable[[], T_Result],
        two_thousand_twenty_four1120acacia: typing.Callable[[], T_Result],
        two_thousand_twenty_four1028acacia: typing.Callable[[], T_Result],
        two_thousand_twenty_four0930acacia: typing.Callable[[], T_Result],
        two_thousand_twenty_four0620: typing.Callable[[], T_Result],
        two_thousand_twenty_four0410: typing.Callable[[], T_Result],
        two_thousand_twenty_four0403: typing.Callable[[], T_Result],
        two_thousand_twenty_three1016: typing.Callable[[], T_Result],
        two_thousand_twenty_three0816: typing.Callable[[], T_Result],
        two_thousand_twenty_two1115: typing.Callable[[], T_Result],
        two_thousand_twenty_two0801: typing.Callable[[], T_Result],
        two_thousand_twenty0827: typing.Callable[[], T_Result],
        two_thousand_twenty0302: typing.Callable[[], T_Result],
        two_thousand_nineteen1203: typing.Callable[[], T_Result],
        two_thousand_nineteen1105: typing.Callable[[], T_Result],
        two_thousand_nineteen1017: typing.Callable[[], T_Result],
        two_thousand_nineteen1008: typing.Callable[[], T_Result],
        two_thousand_nineteen0909: typing.Callable[[], T_Result],
        two_thousand_nineteen0814: typing.Callable[[], T_Result],
        two_thousand_nineteen0516: typing.Callable[[], T_Result],
        two_thousand_nineteen0314: typing.Callable[[], T_Result],
        two_thousand_nineteen0219: typing.Callable[[], T_Result],
        two_thousand_nineteen0211: typing.Callable[[], T_Result],
        two_thousand_eighteen1108: typing.Callable[[], T_Result],
        two_thousand_eighteen1031: typing.Callable[[], T_Result],
        two_thousand_eighteen0924: typing.Callable[[], T_Result],
        two_thousand_eighteen0906: typing.Callable[[], T_Result],
        two_thousand_eighteen0823: typing.Callable[[], T_Result],
        two_thousand_eighteen0727: typing.Callable[[], T_Result],
        two_thousand_eighteen0521: typing.Callable[[], T_Result],
        two_thousand_eighteen0228: typing.Callable[[], T_Result],
        two_thousand_eighteen0206: typing.Callable[[], T_Result],
        two_thousand_eighteen0205: typing.Callable[[], T_Result],
        two_thousand_eighteen0123: typing.Callable[[], T_Result],
        two_thousand_seventeen1214: typing.Callable[[], T_Result],
        two_thousand_seventeen0815: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_SIX0325DAHLIA:
            return two_thousand_twenty_six0325dahlia()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_SIX0225CLOVER:
            return two_thousand_twenty_six0225clover()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_SIX0128CLOVER:
            return two_thousand_twenty_six0128clover()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_FIVE1215CLOVER:
            return two_thousand_twenty_five1215clover()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_FIVE1117CLOVER:
            return two_thousand_twenty_five1117clover()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_FIVE1029CLOVER:
            return two_thousand_twenty_five1029clover()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_FIVE0930CLOVER:
            return two_thousand_twenty_five0930clover()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_FIVE0827BASIL:
            return two_thousand_twenty_five0827basil()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_FIVE0730BASIL:
            return two_thousand_twenty_five0730basil()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_FIVE0630BASIL:
            return two_thousand_twenty_five0630basil()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_FIVE0528BASIL:
            return two_thousand_twenty_five0528basil()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_FIVE0430BASIL:
            return two_thousand_twenty_five0430basil()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_FIVE0331BASIL:
            return two_thousand_twenty_five0331basil()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_FIVE0224ACACIA:
            return two_thousand_twenty_five0224acacia()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_FIVE0127ACACIA:
            return two_thousand_twenty_five0127acacia()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_FOUR1218ACACIA:
            return two_thousand_twenty_four1218acacia()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_FOUR1120ACACIA:
            return two_thousand_twenty_four1120acacia()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_FOUR1028ACACIA:
            return two_thousand_twenty_four1028acacia()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_FOUR0930ACACIA:
            return two_thousand_twenty_four0930acacia()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_FOUR0620:
            return two_thousand_twenty_four0620()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_FOUR0410:
            return two_thousand_twenty_four0410()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_FOUR0403:
            return two_thousand_twenty_four0403()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_THREE1016:
            return two_thousand_twenty_three1016()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_THREE0816:
            return two_thousand_twenty_three0816()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_TWO1115:
            return two_thousand_twenty_two1115()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY_TWO0801:
            return two_thousand_twenty_two0801()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY0827:
            return two_thousand_twenty0827()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_TWENTY0302:
            return two_thousand_twenty0302()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_NINETEEN1203:
            return two_thousand_nineteen1203()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_NINETEEN1105:
            return two_thousand_nineteen1105()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_NINETEEN1017:
            return two_thousand_nineteen1017()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_NINETEEN1008:
            return two_thousand_nineteen1008()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_NINETEEN0909:
            return two_thousand_nineteen0909()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_NINETEEN0814:
            return two_thousand_nineteen0814()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_NINETEEN0516:
            return two_thousand_nineteen0516()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_NINETEEN0314:
            return two_thousand_nineteen0314()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_NINETEEN0219:
            return two_thousand_nineteen0219()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_NINETEEN0211:
            return two_thousand_nineteen0211()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_EIGHTEEN1108:
            return two_thousand_eighteen1108()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_EIGHTEEN1031:
            return two_thousand_eighteen1031()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_EIGHTEEN0924:
            return two_thousand_eighteen0924()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_EIGHTEEN0906:
            return two_thousand_eighteen0906()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_EIGHTEEN0823:
            return two_thousand_eighteen0823()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_EIGHTEEN0727:
            return two_thousand_eighteen0727()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_EIGHTEEN0521:
            return two_thousand_eighteen0521()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_EIGHTEEN0228:
            return two_thousand_eighteen0228()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_EIGHTEEN0206:
            return two_thousand_eighteen0206()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_EIGHTEEN0205:
            return two_thousand_eighteen0205()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_EIGHTEEN0123:
            return two_thousand_eighteen0123()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_SEVENTEEN1214:
            return two_thousand_seventeen1214()
        if self is SourceStripeConfigApiVersion.TWO_THOUSAND_SEVENTEEN0815:
            return two_thousand_seventeen0815()
