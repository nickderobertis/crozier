

import enum
import typing

T_Result = typing.TypeVar("T_Result")


class PowerPortTypeLabel(str, enum.Enum):
    C6 = "C6"
    C8 = "C8"
    C14 = "C14"
    C16 = "C16"
    C20 = "C20"
    C22 = "C22"
    PNE4H = "P+N+E 4H"
    PNE6H = "P+N+E 6H"
    PNE9H = "P+N+E 9H"
    TWO_PE4H = "2P+E 4H"
    TWO_PE6H = "2P+E 6H"
    TWO_PE9H = "2P+E 9H"
    THREE_PE4H = "3P+E 4H"
    THREE_PE6H = "3P+E 6H"
    THREE_PE9H = "3P+E 9H"
    THREE_PNE4H = "3P+N+E 4H"
    THREE_PNE6H = "3P+N+E 6H"
    THREE_PNE9H = "3P+N+E 9H"
    NEMA115P = "NEMA 1-15P"
    NEMA515P = "NEMA 5-15P"
    NEMA520P = "NEMA 5-20P"
    NEMA530P = "NEMA 5-30P"
    NEMA550P = "NEMA 5-50P"
    NEMA615P = "NEMA 6-15P"
    NEMA620P = "NEMA 6-20P"
    NEMA630P = "NEMA 6-30P"
    NEMA650P = "NEMA 6-50P"
    NEMA1030P = "NEMA 10-30P"
    NEMA1050P = "NEMA 10-50P"
    NEMA1420P = "NEMA 14-20P"
    NEMA1430P = "NEMA 14-30P"
    NEMA1450P = "NEMA 14-50P"
    NEMA1460P = "NEMA 14-60P"
    NEMA1515P = "NEMA 15-15P"
    NEMA1520P = "NEMA 15-20P"
    NEMA1530P = "NEMA 15-30P"
    NEMA1550P = "NEMA 15-50P"
    NEMA1560P = "NEMA 15-60P"
    NEMA_L115P = "NEMA L1-15P"
    NEMA_L515P = "NEMA L5-15P"
    NEMA_L520P = "NEMA L5-20P"
    NEMA_L530P = "NEMA L5-30P"
    NEMA_L550P = "NEMA L5-50P"
    NEMA_L615P = "NEMA L6-15P"
    NEMA_L620P = "NEMA L6-20P"
    NEMA_L630P = "NEMA L6-30P"
    NEMA_L650P = "NEMA L6-50P"
    NEMA_L1030P = "NEMA L10-30P"
    NEMA_L1420P = "NEMA L14-20P"
    NEMA_L1430P = "NEMA L14-30P"
    NEMA_L1450P = "NEMA L14-50P"
    NEMA_L1460P = "NEMA L14-60P"
    NEMA_L1520P = "NEMA L15-20P"
    NEMA_L1530P = "NEMA L15-30P"
    NEMA_L1550P = "NEMA L15-50P"
    NEMA_L1560P = "NEMA L15-60P"
    NEMA_L2120P = "NEMA L21-20P"
    NEMA_L2130P = "NEMA L21-30P"
    NEMA_L2230P = "NEMA L22-30P"
    CS6361C = "CS6361C"
    CS6365C = "CS6365C"
    CS8165C = "CS8165C"
    CS8265C = "CS8265C"
    CS8365C = "CS8365C"
    CS8465C = "CS8465C"
    ITA_TYPE_C_CEE716 = "ITA Type C (CEE 7/16)"
    ITA_TYPE_E_CEE76 = "ITA Type E (CEE 7/6)"
    ITA_TYPE_F_CEE74 = "ITA Type F (CEE 7/4)"
    ITA_TYPE_EF_CEE77 = "ITA Type E/F (CEE 7/7)"
    ITA_TYPE_G_BS1363 = "ITA Type G (BS 1363)"
    ITA_TYPE_H = "ITA Type H"
    ITA_TYPE_I = "ITA Type I"
    ITA_TYPE_J = "ITA Type J"
    ITA_TYPE_K = "ITA Type K"
    ITA_TYPE_L_CEI2350 = "ITA Type L (CEI 23-50)"
    ITA_TYPE_M_BS546 = "ITA Type M (BS 546)"
    ITA_TYPE_N = "ITA Type N"
    ITA_TYPE_O = "ITA Type O"
    USB_TYPE_A = "USB Type A"
    USB_TYPE_B = "USB Type B"
    USB_TYPE_C = "USB Type C"
    USB_MINI_A = "USB Mini A"
    USB_MINI_B = "USB Mini B"
    USB_MICRO_A = "USB Micro A"
    USB_MICRO_B = "USB Micro B"
    USB_MICRO_AB = "USB Micro AB"
    USB30TYPE_B = "USB 3.0 Type B"
    USB30MICRO_B = "USB 3.0 Micro B"
    DC_TERMINAL = "DC Terminal"
    SAF_D_GRID = "Saf-D-Grid"
    NEUTRIK_POWER_CON20A = "Neutrik powerCON (20A)"
    NEUTRIK_POWER_CON32A = "Neutrik powerCON (32A)"
    NEUTRIK_POWER_CON_TRUE1 = "Neutrik powerCON TRUE1"
    NEUTRIK_POWER_CON_TRUE1TOP = "Neutrik powerCON TRUE1 TOP"
    UBIQUITI_SMART_POWER = "Ubiquiti SmartPower"
    HARDWIRED = "Hardwired"
    OTHER = "Other"

    def visit(
        self,
        c6: typing.Callable[[], T_Result],
        c8: typing.Callable[[], T_Result],
        c14: typing.Callable[[], T_Result],
        c16: typing.Callable[[], T_Result],
        c20: typing.Callable[[], T_Result],
        c22: typing.Callable[[], T_Result],
        pne4h: typing.Callable[[], T_Result],
        pne6h: typing.Callable[[], T_Result],
        pne9h: typing.Callable[[], T_Result],
        two_pe4h: typing.Callable[[], T_Result],
        two_pe6h: typing.Callable[[], T_Result],
        two_pe9h: typing.Callable[[], T_Result],
        three_pe4h: typing.Callable[[], T_Result],
        three_pe6h: typing.Callable[[], T_Result],
        three_pe9h: typing.Callable[[], T_Result],
        three_pne4h: typing.Callable[[], T_Result],
        three_pne6h: typing.Callable[[], T_Result],
        three_pne9h: typing.Callable[[], T_Result],
        nema115p: typing.Callable[[], T_Result],
        nema515p: typing.Callable[[], T_Result],
        nema520p: typing.Callable[[], T_Result],
        nema530p: typing.Callable[[], T_Result],
        nema550p: typing.Callable[[], T_Result],
        nema615p: typing.Callable[[], T_Result],
        nema620p: typing.Callable[[], T_Result],
        nema630p: typing.Callable[[], T_Result],
        nema650p: typing.Callable[[], T_Result],
        nema1030p: typing.Callable[[], T_Result],
        nema1050p: typing.Callable[[], T_Result],
        nema1420p: typing.Callable[[], T_Result],
        nema1430p: typing.Callable[[], T_Result],
        nema1450p: typing.Callable[[], T_Result],
        nema1460p: typing.Callable[[], T_Result],
        nema1515p: typing.Callable[[], T_Result],
        nema1520p: typing.Callable[[], T_Result],
        nema1530p: typing.Callable[[], T_Result],
        nema1550p: typing.Callable[[], T_Result],
        nema1560p: typing.Callable[[], T_Result],
        nema_l115p: typing.Callable[[], T_Result],
        nema_l515p: typing.Callable[[], T_Result],
        nema_l520p: typing.Callable[[], T_Result],
        nema_l530p: typing.Callable[[], T_Result],
        nema_l550p: typing.Callable[[], T_Result],
        nema_l615p: typing.Callable[[], T_Result],
        nema_l620p: typing.Callable[[], T_Result],
        nema_l630p: typing.Callable[[], T_Result],
        nema_l650p: typing.Callable[[], T_Result],
        nema_l1030p: typing.Callable[[], T_Result],
        nema_l1420p: typing.Callable[[], T_Result],
        nema_l1430p: typing.Callable[[], T_Result],
        nema_l1450p: typing.Callable[[], T_Result],
        nema_l1460p: typing.Callable[[], T_Result],
        nema_l1520p: typing.Callable[[], T_Result],
        nema_l1530p: typing.Callable[[], T_Result],
        nema_l1550p: typing.Callable[[], T_Result],
        nema_l1560p: typing.Callable[[], T_Result],
        nema_l2120p: typing.Callable[[], T_Result],
        nema_l2130p: typing.Callable[[], T_Result],
        nema_l2230p: typing.Callable[[], T_Result],
        cs6361c: typing.Callable[[], T_Result],
        cs6365c: typing.Callable[[], T_Result],
        cs8165c: typing.Callable[[], T_Result],
        cs8265c: typing.Callable[[], T_Result],
        cs8365c: typing.Callable[[], T_Result],
        cs8465c: typing.Callable[[], T_Result],
        ita_type_c_cee716: typing.Callable[[], T_Result],
        ita_type_e_cee76: typing.Callable[[], T_Result],
        ita_type_f_cee74: typing.Callable[[], T_Result],
        ita_type_ef_cee77: typing.Callable[[], T_Result],
        ita_type_g_bs1363: typing.Callable[[], T_Result],
        ita_type_h: typing.Callable[[], T_Result],
        ita_type_i: typing.Callable[[], T_Result],
        ita_type_j: typing.Callable[[], T_Result],
        ita_type_k: typing.Callable[[], T_Result],
        ita_type_l_cei2350: typing.Callable[[], T_Result],
        ita_type_m_bs546: typing.Callable[[], T_Result],
        ita_type_n: typing.Callable[[], T_Result],
        ita_type_o: typing.Callable[[], T_Result],
        usb_type_a: typing.Callable[[], T_Result],
        usb_type_b: typing.Callable[[], T_Result],
        usb_type_c: typing.Callable[[], T_Result],
        usb_mini_a: typing.Callable[[], T_Result],
        usb_mini_b: typing.Callable[[], T_Result],
        usb_micro_a: typing.Callable[[], T_Result],
        usb_micro_b: typing.Callable[[], T_Result],
        usb_micro_ab: typing.Callable[[], T_Result],
        usb30type_b: typing.Callable[[], T_Result],
        usb30micro_b: typing.Callable[[], T_Result],
        dc_terminal: typing.Callable[[], T_Result],
        saf_d_grid: typing.Callable[[], T_Result],
        neutrik_power_con20a: typing.Callable[[], T_Result],
        neutrik_power_con32a: typing.Callable[[], T_Result],
        neutrik_power_con_true1: typing.Callable[[], T_Result],
        neutrik_power_con_true1top: typing.Callable[[], T_Result],
        ubiquiti_smart_power: typing.Callable[[], T_Result],
        hardwired: typing.Callable[[], T_Result],
        other: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is PowerPortTypeLabel.C6:
            return c6()
        if self is PowerPortTypeLabel.C8:
            return c8()
        if self is PowerPortTypeLabel.C14:
            return c14()
        if self is PowerPortTypeLabel.C16:
            return c16()
        if self is PowerPortTypeLabel.C20:
            return c20()
        if self is PowerPortTypeLabel.C22:
            return c22()
        if self is PowerPortTypeLabel.PNE4H:
            return pne4h()
        if self is PowerPortTypeLabel.PNE6H:
            return pne6h()
        if self is PowerPortTypeLabel.PNE9H:
            return pne9h()
        if self is PowerPortTypeLabel.TWO_PE4H:
            return two_pe4h()
        if self is PowerPortTypeLabel.TWO_PE6H:
            return two_pe6h()
        if self is PowerPortTypeLabel.TWO_PE9H:
            return two_pe9h()
        if self is PowerPortTypeLabel.THREE_PE4H:
            return three_pe4h()
        if self is PowerPortTypeLabel.THREE_PE6H:
            return three_pe6h()
        if self is PowerPortTypeLabel.THREE_PE9H:
            return three_pe9h()
        if self is PowerPortTypeLabel.THREE_PNE4H:
            return three_pne4h()
        if self is PowerPortTypeLabel.THREE_PNE6H:
            return three_pne6h()
        if self is PowerPortTypeLabel.THREE_PNE9H:
            return three_pne9h()
        if self is PowerPortTypeLabel.NEMA115P:
            return nema115p()
        if self is PowerPortTypeLabel.NEMA515P:
            return nema515p()
        if self is PowerPortTypeLabel.NEMA520P:
            return nema520p()
        if self is PowerPortTypeLabel.NEMA530P:
            return nema530p()
        if self is PowerPortTypeLabel.NEMA550P:
            return nema550p()
        if self is PowerPortTypeLabel.NEMA615P:
            return nema615p()
        if self is PowerPortTypeLabel.NEMA620P:
            return nema620p()
        if self is PowerPortTypeLabel.NEMA630P:
            return nema630p()
        if self is PowerPortTypeLabel.NEMA650P:
            return nema650p()
        if self is PowerPortTypeLabel.NEMA1030P:
            return nema1030p()
        if self is PowerPortTypeLabel.NEMA1050P:
            return nema1050p()
        if self is PowerPortTypeLabel.NEMA1420P:
            return nema1420p()
        if self is PowerPortTypeLabel.NEMA1430P:
            return nema1430p()
        if self is PowerPortTypeLabel.NEMA1450P:
            return nema1450p()
        if self is PowerPortTypeLabel.NEMA1460P:
            return nema1460p()
        if self is PowerPortTypeLabel.NEMA1515P:
            return nema1515p()
        if self is PowerPortTypeLabel.NEMA1520P:
            return nema1520p()
        if self is PowerPortTypeLabel.NEMA1530P:
            return nema1530p()
        if self is PowerPortTypeLabel.NEMA1550P:
            return nema1550p()
        if self is PowerPortTypeLabel.NEMA1560P:
            return nema1560p()
        if self is PowerPortTypeLabel.NEMA_L115P:
            return nema_l115p()
        if self is PowerPortTypeLabel.NEMA_L515P:
            return nema_l515p()
        if self is PowerPortTypeLabel.NEMA_L520P:
            return nema_l520p()
        if self is PowerPortTypeLabel.NEMA_L530P:
            return nema_l530p()
        if self is PowerPortTypeLabel.NEMA_L550P:
            return nema_l550p()
        if self is PowerPortTypeLabel.NEMA_L615P:
            return nema_l615p()
        if self is PowerPortTypeLabel.NEMA_L620P:
            return nema_l620p()
        if self is PowerPortTypeLabel.NEMA_L630P:
            return nema_l630p()
        if self is PowerPortTypeLabel.NEMA_L650P:
            return nema_l650p()
        if self is PowerPortTypeLabel.NEMA_L1030P:
            return nema_l1030p()
        if self is PowerPortTypeLabel.NEMA_L1420P:
            return nema_l1420p()
        if self is PowerPortTypeLabel.NEMA_L1430P:
            return nema_l1430p()
        if self is PowerPortTypeLabel.NEMA_L1450P:
            return nema_l1450p()
        if self is PowerPortTypeLabel.NEMA_L1460P:
            return nema_l1460p()
        if self is PowerPortTypeLabel.NEMA_L1520P:
            return nema_l1520p()
        if self is PowerPortTypeLabel.NEMA_L1530P:
            return nema_l1530p()
        if self is PowerPortTypeLabel.NEMA_L1550P:
            return nema_l1550p()
        if self is PowerPortTypeLabel.NEMA_L1560P:
            return nema_l1560p()
        if self is PowerPortTypeLabel.NEMA_L2120P:
            return nema_l2120p()
        if self is PowerPortTypeLabel.NEMA_L2130P:
            return nema_l2130p()
        if self is PowerPortTypeLabel.NEMA_L2230P:
            return nema_l2230p()
        if self is PowerPortTypeLabel.CS6361C:
            return cs6361c()
        if self is PowerPortTypeLabel.CS6365C:
            return cs6365c()
        if self is PowerPortTypeLabel.CS8165C:
            return cs8165c()
        if self is PowerPortTypeLabel.CS8265C:
            return cs8265c()
        if self is PowerPortTypeLabel.CS8365C:
            return cs8365c()
        if self is PowerPortTypeLabel.CS8465C:
            return cs8465c()
        if self is PowerPortTypeLabel.ITA_TYPE_C_CEE716:
            return ita_type_c_cee716()
        if self is PowerPortTypeLabel.ITA_TYPE_E_CEE76:
            return ita_type_e_cee76()
        if self is PowerPortTypeLabel.ITA_TYPE_F_CEE74:
            return ita_type_f_cee74()
        if self is PowerPortTypeLabel.ITA_TYPE_EF_CEE77:
            return ita_type_ef_cee77()
        if self is PowerPortTypeLabel.ITA_TYPE_G_BS1363:
            return ita_type_g_bs1363()
        if self is PowerPortTypeLabel.ITA_TYPE_H:
            return ita_type_h()
        if self is PowerPortTypeLabel.ITA_TYPE_I:
            return ita_type_i()
        if self is PowerPortTypeLabel.ITA_TYPE_J:
            return ita_type_j()
        if self is PowerPortTypeLabel.ITA_TYPE_K:
            return ita_type_k()
        if self is PowerPortTypeLabel.ITA_TYPE_L_CEI2350:
            return ita_type_l_cei2350()
        if self is PowerPortTypeLabel.ITA_TYPE_M_BS546:
            return ita_type_m_bs546()
        if self is PowerPortTypeLabel.ITA_TYPE_N:
            return ita_type_n()
        if self is PowerPortTypeLabel.ITA_TYPE_O:
            return ita_type_o()
        if self is PowerPortTypeLabel.USB_TYPE_A:
            return usb_type_a()
        if self is PowerPortTypeLabel.USB_TYPE_B:
            return usb_type_b()
        if self is PowerPortTypeLabel.USB_TYPE_C:
            return usb_type_c()
        if self is PowerPortTypeLabel.USB_MINI_A:
            return usb_mini_a()
        if self is PowerPortTypeLabel.USB_MINI_B:
            return usb_mini_b()
        if self is PowerPortTypeLabel.USB_MICRO_A:
            return usb_micro_a()
        if self is PowerPortTypeLabel.USB_MICRO_B:
            return usb_micro_b()
        if self is PowerPortTypeLabel.USB_MICRO_AB:
            return usb_micro_ab()
        if self is PowerPortTypeLabel.USB30TYPE_B:
            return usb30type_b()
        if self is PowerPortTypeLabel.USB30MICRO_B:
            return usb30micro_b()
        if self is PowerPortTypeLabel.DC_TERMINAL:
            return dc_terminal()
        if self is PowerPortTypeLabel.SAF_D_GRID:
            return saf_d_grid()
        if self is PowerPortTypeLabel.NEUTRIK_POWER_CON20A:
            return neutrik_power_con20a()
        if self is PowerPortTypeLabel.NEUTRIK_POWER_CON32A:
            return neutrik_power_con32a()
        if self is PowerPortTypeLabel.NEUTRIK_POWER_CON_TRUE1:
            return neutrik_power_con_true1()
        if self is PowerPortTypeLabel.NEUTRIK_POWER_CON_TRUE1TOP:
            return neutrik_power_con_true1top()
        if self is PowerPortTypeLabel.UBIQUITI_SMART_POWER:
            return ubiquiti_smart_power()
        if self is PowerPortTypeLabel.HARDWIRED:
            return hardwired()
        if self is PowerPortTypeLabel.OTHER:
            return other()
