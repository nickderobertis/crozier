

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class InterfaceRfChannelLabel(enum.StrEnum):
    ONE2412M_HZ = "1 (2412 MHz)"
    TWO2417M_HZ = "2 (2417 MHz)"
    THREE2422M_HZ = "3 (2422 MHz)"
    FOUR2427M_HZ = "4 (2427 MHz)"
    FIVE2432M_HZ = "5 (2432 MHz)"
    SIX2437M_HZ = "6 (2437 MHz)"
    SEVEN2442M_HZ = "7 (2442 MHz)"
    EIGHT2447M_HZ = "8 (2447 MHz)"
    NINE2452M_HZ = "9 (2452 MHz)"
    TEN2457M_HZ = "10 (2457 MHz)"
    ELEVEN2462M_HZ = "11 (2462 MHz)"
    TWELVE2467M_HZ = "12 (2467 MHz)"
    THIRTEEN2472M_HZ = "13 (2472 MHz)"
    THIRTY_TWO516020M_HZ = "32 (5160/20 MHz)"
    THIRTY_FOUR517040M_HZ = "34 (5170/40 MHz)"
    THIRTY_SIX518020M_HZ = "36 (5180/20 MHz)"
    THIRTY_EIGHT519040M_HZ = "38 (5190/40 MHz)"
    FORTY520020M_HZ = "40 (5200/20 MHz)"
    FORTY_TWO521080M_HZ = "42 (5210/80 MHz)"
    FORTY_FOUR522020M_HZ = "44 (5220/20 MHz)"
    FORTY_SIX523040M_HZ = "46 (5230/40 MHz)"
    FORTY_EIGHT524020M_HZ = "48 (5240/20 MHz)"
    FIFTY5250160M_HZ = "50 (5250/160 MHz)"
    FIFTY_TWO526020M_HZ = "52 (5260/20 MHz)"
    FIFTY_FOUR527040M_HZ = "54 (5270/40 MHz)"
    FIFTY_SIX528020M_HZ = "56 (5280/20 MHz)"
    FIFTY_EIGHT529080M_HZ = "58 (5290/80 MHz)"
    SIXTY530020M_HZ = "60 (5300/20 MHz)"
    SIXTY_TWO531040M_HZ = "62 (5310/40 MHz)"
    SIXTY_FOUR532020M_HZ = "64 (5320/20 MHz)"
    ONE_HUNDRED550020M_HZ = "100 (5500/20 MHz)"
    ONE_HUNDRED_TWO551040M_HZ = "102 (5510/40 MHz)"
    ONE_HUNDRED_FOUR552020M_HZ = "104 (5520/20 MHz)"
    ONE_HUNDRED_SIX553080M_HZ = "106 (5530/80 MHz)"
    ONE_HUNDRED_EIGHT554020M_HZ = "108 (5540/20 MHz)"
    ONE_HUNDRED_TEN555040M_HZ = "110 (5550/40 MHz)"
    ONE_HUNDRED_TWELVE556020M_HZ = "112 (5560/20 MHz)"
    ONE_HUNDRED_FOURTEEN5570160M_HZ = "114 (5570/160 MHz)"
    ONE_HUNDRED_SIXTEEN558020M_HZ = "116 (5580/20 MHz)"
    ONE_HUNDRED_EIGHTEEN559040M_HZ = "118 (5590/40 MHz)"
    ONE_HUNDRED_TWENTY560020M_HZ = "120 (5600/20 MHz)"
    ONE_HUNDRED_TWENTY_TWO561080M_HZ = "122 (5610/80 MHz)"
    ONE_HUNDRED_TWENTY_FOUR562020M_HZ = "124 (5620/20 MHz)"
    ONE_HUNDRED_TWENTY_SIX563040M_HZ = "126 (5630/40 MHz)"
    ONE_HUNDRED_TWENTY_EIGHT564020M_HZ = "128 (5640/20 MHz)"
    ONE_HUNDRED_THIRTY_TWO566020M_HZ = "132 (5660/20 MHz)"
    ONE_HUNDRED_THIRTY_FOUR567040M_HZ = "134 (5670/40 MHz)"
    ONE_HUNDRED_THIRTY_SIX568020M_HZ = "136 (5680/20 MHz)"
    ONE_HUNDRED_THIRTY_EIGHT569080M_HZ = "138 (5690/80 MHz)"
    ONE_HUNDRED_FORTY570020M_HZ = "140 (5700/20 MHz)"
    ONE_HUNDRED_FORTY_TWO571040M_HZ = "142 (5710/40 MHz)"
    ONE_HUNDRED_FORTY_FOUR572020M_HZ = "144 (5720/20 MHz)"
    ONE_HUNDRED_FORTY_NINE574520M_HZ = "149 (5745/20 MHz)"
    ONE_HUNDRED_FIFTY_ONE575540M_HZ = "151 (5755/40 MHz)"
    ONE_HUNDRED_FIFTY_THREE576520M_HZ = "153 (5765/20 MHz)"
    ONE_HUNDRED_FIFTY_FIVE577580M_HZ = "155 (5775/80 MHz)"
    ONE_HUNDRED_FIFTY_SEVEN578520M_HZ = "157 (5785/20 MHz)"
    ONE_HUNDRED_FIFTY_NINE579540M_HZ = "159 (5795/40 MHz)"
    ONE_HUNDRED_SIXTY_ONE580520M_HZ = "161 (5805/20 MHz)"
    ONE_HUNDRED_SIXTY_THREE5815160M_HZ = "163 (5815/160 MHz)"
    ONE_HUNDRED_SIXTY_FIVE582520M_HZ = "165 (5825/20 MHz)"
    ONE_HUNDRED_SIXTY_SEVEN583540M_HZ = "167 (5835/40 MHz)"
    ONE_HUNDRED_SIXTY_NINE584520M_HZ = "169 (5845/20 MHz)"
    ONE_HUNDRED_SEVENTY_ONE585580M_HZ = "171 (5855/80 MHz)"
    ONE_HUNDRED_SEVENTY_THREE586520M_HZ = "173 (5865/20 MHz)"
    ONE_HUNDRED_SEVENTY_FIVE587540M_HZ = "175 (5875/40 MHz)"
    ONE_HUNDRED_SEVENTY_SEVEN588520M_HZ = "177 (5885/20 MHz)"
    ONE595520M_HZ = "1 (5955/20 MHz)"
    THREE596540M_HZ = "3 (5965/40 MHz)"
    FIVE597520M_HZ = "5 (5975/20 MHz)"
    SEVEN598580M_HZ = "7 (5985/80 MHz)"
    NINE599520M_HZ = "9 (5995/20 MHz)"
    ELEVEN600540M_HZ = "11 (6005/40 MHz)"
    THIRTEEN601520M_HZ = "13 (6015/20 MHz)"
    FIFTEEN6025160M_HZ = "15 (6025/160 MHz)"
    SEVENTEEN603520M_HZ = "17 (6035/20 MHz)"
    NINETEEN604540M_HZ = "19 (6045/40 MHz)"
    TWENTY_ONE605520M_HZ = "21 (6055/20 MHz)"
    TWENTY_THREE606580M_HZ = "23 (6065/80 MHz)"
    TWENTY_FIVE607520M_HZ = "25 (6075/20 MHz)"
    TWENTY_SEVEN608540M_HZ = "27 (6085/40 MHz)"
    TWENTY_NINE609520M_HZ = "29 (6095/20 MHz)"
    THIRTY_ONE6105320M_HZ = "31 (6105/320 MHz)"
    THIRTY_THREE611520M_HZ = "33 (6115/20 MHz)"
    THIRTY_FIVE612540M_HZ = "35 (6125/40 MHz)"
    THIRTY_SEVEN613520M_HZ = "37 (6135/20 MHz)"
    THIRTY_NINE614580M_HZ = "39 (6145/80 MHz)"
    FORTY_ONE615520M_HZ = "41 (6155/20 MHz)"
    FORTY_THREE616540M_HZ = "43 (6165/40 MHz)"
    FORTY_FIVE617520M_HZ = "45 (6175/20 MHz)"
    FORTY_SEVEN6185160M_HZ = "47 (6185/160 MHz)"
    FORTY_NINE619520M_HZ = "49 (6195/20 MHz)"
    FIFTY_ONE620540M_HZ = "51 (6205/40 MHz)"
    FIFTY_THREE621520M_HZ = "53 (6215/20 MHz)"
    FIFTY_FIVE622580M_HZ = "55 (6225/80 MHz)"
    FIFTY_SEVEN623520M_HZ = "57 (6235/20 MHz)"
    FIFTY_NINE624540M_HZ = "59 (6245/40 MHz)"
    SIXTY_ONE625520M_HZ = "61 (6255/20 MHz)"
    SIXTY_FIVE627520M_HZ = "65 (6275/20 MHz)"
    SIXTY_SEVEN628540M_HZ = "67 (6285/40 MHz)"
    SIXTY_NINE629520M_HZ = "69 (6295/20 MHz)"
    SEVENTY_ONE630580M_HZ = "71 (6305/80 MHz)"
    SEVENTY_THREE631520M_HZ = "73 (6315/20 MHz)"
    SEVENTY_FIVE632540M_HZ = "75 (6325/40 MHz)"
    SEVENTY_SEVEN633520M_HZ = "77 (6335/20 MHz)"
    SEVENTY_NINE6345160M_HZ = "79 (6345/160 MHz)"
    EIGHTY_ONE635520M_HZ = "81 (6355/20 MHz)"
    EIGHTY_THREE636540M_HZ = "83 (6365/40 MHz)"
    EIGHTY_FIVE637520M_HZ = "85 (6375/20 MHz)"
    EIGHTY_SEVEN638580M_HZ = "87 (6385/80 MHz)"
    EIGHTY_NINE639520M_HZ = "89 (6395/20 MHz)"
    NINETY_ONE640540M_HZ = "91 (6405/40 MHz)"
    NINETY_THREE641520M_HZ = "93 (6415/20 MHz)"
    NINETY_FIVE6425320M_HZ = "95 (6425/320 MHz)"
    NINETY_SEVEN643520M_HZ = "97 (6435/20 MHz)"
    NINETY_NINE644540M_HZ = "99 (6445/40 MHz)"
    ONE_HUNDRED_ONE645520M_HZ = "101 (6455/20 MHz)"
    ONE_HUNDRED_THREE646580M_HZ = "103 (6465/80 MHz)"
    ONE_HUNDRED_FIVE647520M_HZ = "105 (6475/20 MHz)"
    ONE_HUNDRED_SEVEN648540M_HZ = "107 (6485/40 MHz)"
    ONE_HUNDRED_NINE649520M_HZ = "109 (6495/20 MHz)"
    ONE_HUNDRED_ELEVEN6505160M_HZ = "111 (6505/160 MHz)"
    ONE_HUNDRED_THIRTEEN651520M_HZ = "113 (6515/20 MHz)"
    ONE_HUNDRED_FIFTEEN652540M_HZ = "115 (6525/40 MHz)"
    ONE_HUNDRED_SEVENTEEN653520M_HZ = "117 (6535/20 MHz)"
    ONE_HUNDRED_NINETEEN654580M_HZ = "119 (6545/80 MHz)"
    ONE_HUNDRED_TWENTY_ONE655520M_HZ = "121 (6555/20 MHz)"
    ONE_HUNDRED_TWENTY_THREE656540M_HZ = "123 (6565/40 MHz)"
    ONE_HUNDRED_TWENTY_FIVE657520M_HZ = "125 (6575/20 MHz)"
    ONE_HUNDRED_TWENTY_NINE659520M_HZ = "129 (6595/20 MHz)"
    ONE_HUNDRED_THIRTY_ONE660540M_HZ = "131 (6605/40 MHz)"
    ONE_HUNDRED_THIRTY_THREE661520M_HZ = "133 (6615/20 MHz)"
    ONE_HUNDRED_THIRTY_FIVE662580M_HZ = "135 (6625/80 MHz)"
    ONE_HUNDRED_THIRTY_SEVEN663520M_HZ = "137 (6635/20 MHz)"
    ONE_HUNDRED_THIRTY_NINE664540M_HZ = "139 (6645/40 MHz)"
    ONE_HUNDRED_FORTY_ONE665520M_HZ = "141 (6655/20 MHz)"
    ONE_HUNDRED_FORTY_THREE6665160M_HZ = "143 (6665/160 MHz)"
    ONE_HUNDRED_FORTY_FIVE667520M_HZ = "145 (6675/20 MHz)"
    ONE_HUNDRED_FORTY_SEVEN668540M_HZ = "147 (6685/40 MHz)"
    ONE_HUNDRED_FORTY_NINE669520M_HZ = "149 (6695/20 MHz)"
    ONE_HUNDRED_FIFTY_ONE670580M_HZ = "151 (6705/80 MHz)"
    ONE_HUNDRED_FIFTY_THREE671520M_HZ = "153 (6715/20 MHz)"
    ONE_HUNDRED_FIFTY_FIVE672540M_HZ = "155 (6725/40 MHz)"
    ONE_HUNDRED_FIFTY_SEVEN673520M_HZ = "157 (6735/20 MHz)"
    ONE_HUNDRED_FIFTY_NINE6745320M_HZ = "159 (6745/320 MHz)"
    ONE_HUNDRED_SIXTY_ONE675520M_HZ = "161 (6755/20 MHz)"
    ONE_HUNDRED_SIXTY_THREE676540M_HZ = "163 (6765/40 MHz)"
    ONE_HUNDRED_SIXTY_FIVE677520M_HZ = "165 (6775/20 MHz)"
    ONE_HUNDRED_SIXTY_SEVEN678580M_HZ = "167 (6785/80 MHz)"
    ONE_HUNDRED_SIXTY_NINE679520M_HZ = "169 (6795/20 MHz)"
    ONE_HUNDRED_SEVENTY_ONE680540M_HZ = "171 (6805/40 MHz)"
    ONE_HUNDRED_SEVENTY_THREE681520M_HZ = "173 (6815/20 MHz)"
    ONE_HUNDRED_SEVENTY_FIVE6825160M_HZ = "175 (6825/160 MHz)"
    ONE_HUNDRED_SEVENTY_SEVEN683520M_HZ = "177 (6835/20 MHz)"
    ONE_HUNDRED_SEVENTY_NINE684540M_HZ = "179 (6845/40 MHz)"
    ONE_HUNDRED_EIGHTY_ONE685520M_HZ = "181 (6855/20 MHz)"
    ONE_HUNDRED_EIGHTY_THREE686580M_HZ = "183 (6865/80 MHz)"
    ONE_HUNDRED_EIGHTY_FIVE687520M_HZ = "185 (6875/20 MHz)"
    ONE_HUNDRED_EIGHTY_SEVEN688540M_HZ = "187 (6885/40 MHz)"
    ONE_HUNDRED_EIGHTY_NINE689520M_HZ = "189 (6895/20 MHz)"
    ONE_HUNDRED_NINETY_THREE691520M_HZ = "193 (6915/20 MHz)"
    ONE_HUNDRED_NINETY_FIVE692540M_HZ = "195 (6925/40 MHz)"
    ONE_HUNDRED_NINETY_SEVEN693520M_HZ = "197 (6935/20 MHz)"
    ONE_HUNDRED_NINETY_NINE694580M_HZ = "199 (6945/80 MHz)"
    TWO_HUNDRED_ONE695520M_HZ = "201 (6955/20 MHz)"
    TWO_HUNDRED_THREE696540M_HZ = "203 (6965/40 MHz)"
    TWO_HUNDRED_FIVE697520M_HZ = "205 (6975/20 MHz)"
    TWO_HUNDRED_SEVEN6985160M_HZ = "207 (6985/160 MHz)"
    TWO_HUNDRED_NINE699520M_HZ = "209 (6995/20 MHz)"
    TWO_HUNDRED_ELEVEN700540M_HZ = "211 (7005/40 MHz)"
    TWO_HUNDRED_THIRTEEN701520M_HZ = "213 (7015/20 MHz)"
    TWO_HUNDRED_FIFTEEN702580M_HZ = "215 (7025/80 MHz)"
    TWO_HUNDRED_SEVENTEEN703520M_HZ = "217 (7035/20 MHz)"
    TWO_HUNDRED_NINETEEN704540M_HZ = "219 (7045/40 MHz)"
    TWO_HUNDRED_TWENTY_ONE705520M_HZ = "221 (7055/20 MHz)"
    TWO_HUNDRED_TWENTY_FIVE707520M_HZ = "225 (7075/20 MHz)"
    TWO_HUNDRED_TWENTY_SEVEN708540M_HZ = "227 (7085/40 MHz)"
    TWO_HUNDRED_TWENTY_NINE709520M_HZ = "229 (7095/20 MHz)"
    TWO_HUNDRED_THIRTY_THREE711520M_HZ = "233 (7115/20 MHz)"
    ONE5832216G_HZ = "1 (58.32/2.16 GHz)"
    TWO6048216G_HZ = "2 (60.48/2.16 GHz)"
    THREE6264216G_HZ = "3 (62.64/2.16 GHz)"
    FOUR6480216G_HZ = "4 (64.80/2.16 GHz)"
    FIVE6696216G_HZ = "5 (66.96/2.16 GHz)"
    SIX6912216G_HZ = "6 (69.12/2.16 GHz)"
    NINE5940432G_HZ = "9 (59.40/4.32 GHz)"
    TEN6156432G_HZ = "10 (61.56/4.32 GHz)"
    ELEVEN6372432G_HZ = "11 (63.72/4.32 GHz)"
    TWELVE6588432G_HZ = "12 (65.88/4.32 GHz)"
    THIRTEEN6804432G_HZ = "13 (68.04/4.32 GHz)"
    SEVENTEEN6048648G_HZ = "17 (60.48/6.48 GHz)"
    EIGHTEEN6264648G_HZ = "18 (62.64/6.48 GHz)"
    NINETEEN6480648G_HZ = "19 (64.80/6.48 GHz)"
    TWENTY6696648G_HZ = "20 (66.96/6.48 GHz)"
    TWENTY_FIVE6156864G_HZ = "25 (61.56/8.64 GHz)"
    TWENTY_SIX6372864G_HZ = "26 (63.72/8.64 GHz)"
    TWENTY_SEVEN6588864G_HZ = "27 (65.88/8.64 GHz)"

    def visit(
        self,
        one2412m_hz: typing.Callable[[], T_Result],
        two2417m_hz: typing.Callable[[], T_Result],
        three2422m_hz: typing.Callable[[], T_Result],
        four2427m_hz: typing.Callable[[], T_Result],
        five2432m_hz: typing.Callable[[], T_Result],
        six2437m_hz: typing.Callable[[], T_Result],
        seven2442m_hz: typing.Callable[[], T_Result],
        eight2447m_hz: typing.Callable[[], T_Result],
        nine2452m_hz: typing.Callable[[], T_Result],
        ten2457m_hz: typing.Callable[[], T_Result],
        eleven2462m_hz: typing.Callable[[], T_Result],
        twelve2467m_hz: typing.Callable[[], T_Result],
        thirteen2472m_hz: typing.Callable[[], T_Result],
        thirty_two516020m_hz: typing.Callable[[], T_Result],
        thirty_four517040m_hz: typing.Callable[[], T_Result],
        thirty_six518020m_hz: typing.Callable[[], T_Result],
        thirty_eight519040m_hz: typing.Callable[[], T_Result],
        forty520020m_hz: typing.Callable[[], T_Result],
        forty_two521080m_hz: typing.Callable[[], T_Result],
        forty_four522020m_hz: typing.Callable[[], T_Result],
        forty_six523040m_hz: typing.Callable[[], T_Result],
        forty_eight524020m_hz: typing.Callable[[], T_Result],
        fifty5250160m_hz: typing.Callable[[], T_Result],
        fifty_two526020m_hz: typing.Callable[[], T_Result],
        fifty_four527040m_hz: typing.Callable[[], T_Result],
        fifty_six528020m_hz: typing.Callable[[], T_Result],
        fifty_eight529080m_hz: typing.Callable[[], T_Result],
        sixty530020m_hz: typing.Callable[[], T_Result],
        sixty_two531040m_hz: typing.Callable[[], T_Result],
        sixty_four532020m_hz: typing.Callable[[], T_Result],
        one_hundred550020m_hz: typing.Callable[[], T_Result],
        one_hundred_two551040m_hz: typing.Callable[[], T_Result],
        one_hundred_four552020m_hz: typing.Callable[[], T_Result],
        one_hundred_six553080m_hz: typing.Callable[[], T_Result],
        one_hundred_eight554020m_hz: typing.Callable[[], T_Result],
        one_hundred_ten555040m_hz: typing.Callable[[], T_Result],
        one_hundred_twelve556020m_hz: typing.Callable[[], T_Result],
        one_hundred_fourteen5570160m_hz: typing.Callable[[], T_Result],
        one_hundred_sixteen558020m_hz: typing.Callable[[], T_Result],
        one_hundred_eighteen559040m_hz: typing.Callable[[], T_Result],
        one_hundred_twenty560020m_hz: typing.Callable[[], T_Result],
        one_hundred_twenty_two561080m_hz: typing.Callable[[], T_Result],
        one_hundred_twenty_four562020m_hz: typing.Callable[[], T_Result],
        one_hundred_twenty_six563040m_hz: typing.Callable[[], T_Result],
        one_hundred_twenty_eight564020m_hz: typing.Callable[[], T_Result],
        one_hundred_thirty_two566020m_hz: typing.Callable[[], T_Result],
        one_hundred_thirty_four567040m_hz: typing.Callable[[], T_Result],
        one_hundred_thirty_six568020m_hz: typing.Callable[[], T_Result],
        one_hundred_thirty_eight569080m_hz: typing.Callable[[], T_Result],
        one_hundred_forty570020m_hz: typing.Callable[[], T_Result],
        one_hundred_forty_two571040m_hz: typing.Callable[[], T_Result],
        one_hundred_forty_four572020m_hz: typing.Callable[[], T_Result],
        one_hundred_forty_nine574520m_hz: typing.Callable[[], T_Result],
        one_hundred_fifty_one575540m_hz: typing.Callable[[], T_Result],
        one_hundred_fifty_three576520m_hz: typing.Callable[[], T_Result],
        one_hundred_fifty_five577580m_hz: typing.Callable[[], T_Result],
        one_hundred_fifty_seven578520m_hz: typing.Callable[[], T_Result],
        one_hundred_fifty_nine579540m_hz: typing.Callable[[], T_Result],
        one_hundred_sixty_one580520m_hz: typing.Callable[[], T_Result],
        one_hundred_sixty_three5815160m_hz: typing.Callable[[], T_Result],
        one_hundred_sixty_five582520m_hz: typing.Callable[[], T_Result],
        one_hundred_sixty_seven583540m_hz: typing.Callable[[], T_Result],
        one_hundred_sixty_nine584520m_hz: typing.Callable[[], T_Result],
        one_hundred_seventy_one585580m_hz: typing.Callable[[], T_Result],
        one_hundred_seventy_three586520m_hz: typing.Callable[[], T_Result],
        one_hundred_seventy_five587540m_hz: typing.Callable[[], T_Result],
        one_hundred_seventy_seven588520m_hz: typing.Callable[[], T_Result],
        one595520m_hz: typing.Callable[[], T_Result],
        three596540m_hz: typing.Callable[[], T_Result],
        five597520m_hz: typing.Callable[[], T_Result],
        seven598580m_hz: typing.Callable[[], T_Result],
        nine599520m_hz: typing.Callable[[], T_Result],
        eleven600540m_hz: typing.Callable[[], T_Result],
        thirteen601520m_hz: typing.Callable[[], T_Result],
        fifteen6025160m_hz: typing.Callable[[], T_Result],
        seventeen603520m_hz: typing.Callable[[], T_Result],
        nineteen604540m_hz: typing.Callable[[], T_Result],
        twenty_one605520m_hz: typing.Callable[[], T_Result],
        twenty_three606580m_hz: typing.Callable[[], T_Result],
        twenty_five607520m_hz: typing.Callable[[], T_Result],
        twenty_seven608540m_hz: typing.Callable[[], T_Result],
        twenty_nine609520m_hz: typing.Callable[[], T_Result],
        thirty_one6105320m_hz: typing.Callable[[], T_Result],
        thirty_three611520m_hz: typing.Callable[[], T_Result],
        thirty_five612540m_hz: typing.Callable[[], T_Result],
        thirty_seven613520m_hz: typing.Callable[[], T_Result],
        thirty_nine614580m_hz: typing.Callable[[], T_Result],
        forty_one615520m_hz: typing.Callable[[], T_Result],
        forty_three616540m_hz: typing.Callable[[], T_Result],
        forty_five617520m_hz: typing.Callable[[], T_Result],
        forty_seven6185160m_hz: typing.Callable[[], T_Result],
        forty_nine619520m_hz: typing.Callable[[], T_Result],
        fifty_one620540m_hz: typing.Callable[[], T_Result],
        fifty_three621520m_hz: typing.Callable[[], T_Result],
        fifty_five622580m_hz: typing.Callable[[], T_Result],
        fifty_seven623520m_hz: typing.Callable[[], T_Result],
        fifty_nine624540m_hz: typing.Callable[[], T_Result],
        sixty_one625520m_hz: typing.Callable[[], T_Result],
        sixty_five627520m_hz: typing.Callable[[], T_Result],
        sixty_seven628540m_hz: typing.Callable[[], T_Result],
        sixty_nine629520m_hz: typing.Callable[[], T_Result],
        seventy_one630580m_hz: typing.Callable[[], T_Result],
        seventy_three631520m_hz: typing.Callable[[], T_Result],
        seventy_five632540m_hz: typing.Callable[[], T_Result],
        seventy_seven633520m_hz: typing.Callable[[], T_Result],
        seventy_nine6345160m_hz: typing.Callable[[], T_Result],
        eighty_one635520m_hz: typing.Callable[[], T_Result],
        eighty_three636540m_hz: typing.Callable[[], T_Result],
        eighty_five637520m_hz: typing.Callable[[], T_Result],
        eighty_seven638580m_hz: typing.Callable[[], T_Result],
        eighty_nine639520m_hz: typing.Callable[[], T_Result],
        ninety_one640540m_hz: typing.Callable[[], T_Result],
        ninety_three641520m_hz: typing.Callable[[], T_Result],
        ninety_five6425320m_hz: typing.Callable[[], T_Result],
        ninety_seven643520m_hz: typing.Callable[[], T_Result],
        ninety_nine644540m_hz: typing.Callable[[], T_Result],
        one_hundred_one645520m_hz: typing.Callable[[], T_Result],
        one_hundred_three646580m_hz: typing.Callable[[], T_Result],
        one_hundred_five647520m_hz: typing.Callable[[], T_Result],
        one_hundred_seven648540m_hz: typing.Callable[[], T_Result],
        one_hundred_nine649520m_hz: typing.Callable[[], T_Result],
        one_hundred_eleven6505160m_hz: typing.Callable[[], T_Result],
        one_hundred_thirteen651520m_hz: typing.Callable[[], T_Result],
        one_hundred_fifteen652540m_hz: typing.Callable[[], T_Result],
        one_hundred_seventeen653520m_hz: typing.Callable[[], T_Result],
        one_hundred_nineteen654580m_hz: typing.Callable[[], T_Result],
        one_hundred_twenty_one655520m_hz: typing.Callable[[], T_Result],
        one_hundred_twenty_three656540m_hz: typing.Callable[[], T_Result],
        one_hundred_twenty_five657520m_hz: typing.Callable[[], T_Result],
        one_hundred_twenty_nine659520m_hz: typing.Callable[[], T_Result],
        one_hundred_thirty_one660540m_hz: typing.Callable[[], T_Result],
        one_hundred_thirty_three661520m_hz: typing.Callable[[], T_Result],
        one_hundred_thirty_five662580m_hz: typing.Callable[[], T_Result],
        one_hundred_thirty_seven663520m_hz: typing.Callable[[], T_Result],
        one_hundred_thirty_nine664540m_hz: typing.Callable[[], T_Result],
        one_hundred_forty_one665520m_hz: typing.Callable[[], T_Result],
        one_hundred_forty_three6665160m_hz: typing.Callable[[], T_Result],
        one_hundred_forty_five667520m_hz: typing.Callable[[], T_Result],
        one_hundred_forty_seven668540m_hz: typing.Callable[[], T_Result],
        one_hundred_forty_nine669520m_hz: typing.Callable[[], T_Result],
        one_hundred_fifty_one670580m_hz: typing.Callable[[], T_Result],
        one_hundred_fifty_three671520m_hz: typing.Callable[[], T_Result],
        one_hundred_fifty_five672540m_hz: typing.Callable[[], T_Result],
        one_hundred_fifty_seven673520m_hz: typing.Callable[[], T_Result],
        one_hundred_fifty_nine6745320m_hz: typing.Callable[[], T_Result],
        one_hundred_sixty_one675520m_hz: typing.Callable[[], T_Result],
        one_hundred_sixty_three676540m_hz: typing.Callable[[], T_Result],
        one_hundred_sixty_five677520m_hz: typing.Callable[[], T_Result],
        one_hundred_sixty_seven678580m_hz: typing.Callable[[], T_Result],
        one_hundred_sixty_nine679520m_hz: typing.Callable[[], T_Result],
        one_hundred_seventy_one680540m_hz: typing.Callable[[], T_Result],
        one_hundred_seventy_three681520m_hz: typing.Callable[[], T_Result],
        one_hundred_seventy_five6825160m_hz: typing.Callable[[], T_Result],
        one_hundred_seventy_seven683520m_hz: typing.Callable[[], T_Result],
        one_hundred_seventy_nine684540m_hz: typing.Callable[[], T_Result],
        one_hundred_eighty_one685520m_hz: typing.Callable[[], T_Result],
        one_hundred_eighty_three686580m_hz: typing.Callable[[], T_Result],
        one_hundred_eighty_five687520m_hz: typing.Callable[[], T_Result],
        one_hundred_eighty_seven688540m_hz: typing.Callable[[], T_Result],
        one_hundred_eighty_nine689520m_hz: typing.Callable[[], T_Result],
        one_hundred_ninety_three691520m_hz: typing.Callable[[], T_Result],
        one_hundred_ninety_five692540m_hz: typing.Callable[[], T_Result],
        one_hundred_ninety_seven693520m_hz: typing.Callable[[], T_Result],
        one_hundred_ninety_nine694580m_hz: typing.Callable[[], T_Result],
        two_hundred_one695520m_hz: typing.Callable[[], T_Result],
        two_hundred_three696540m_hz: typing.Callable[[], T_Result],
        two_hundred_five697520m_hz: typing.Callable[[], T_Result],
        two_hundred_seven6985160m_hz: typing.Callable[[], T_Result],
        two_hundred_nine699520m_hz: typing.Callable[[], T_Result],
        two_hundred_eleven700540m_hz: typing.Callable[[], T_Result],
        two_hundred_thirteen701520m_hz: typing.Callable[[], T_Result],
        two_hundred_fifteen702580m_hz: typing.Callable[[], T_Result],
        two_hundred_seventeen703520m_hz: typing.Callable[[], T_Result],
        two_hundred_nineteen704540m_hz: typing.Callable[[], T_Result],
        two_hundred_twenty_one705520m_hz: typing.Callable[[], T_Result],
        two_hundred_twenty_five707520m_hz: typing.Callable[[], T_Result],
        two_hundred_twenty_seven708540m_hz: typing.Callable[[], T_Result],
        two_hundred_twenty_nine709520m_hz: typing.Callable[[], T_Result],
        two_hundred_thirty_three711520m_hz: typing.Callable[[], T_Result],
        one5832216g_hz: typing.Callable[[], T_Result],
        two6048216g_hz: typing.Callable[[], T_Result],
        three6264216g_hz: typing.Callable[[], T_Result],
        four6480216g_hz: typing.Callable[[], T_Result],
        five6696216g_hz: typing.Callable[[], T_Result],
        six6912216g_hz: typing.Callable[[], T_Result],
        nine5940432g_hz: typing.Callable[[], T_Result],
        ten6156432g_hz: typing.Callable[[], T_Result],
        eleven6372432g_hz: typing.Callable[[], T_Result],
        twelve6588432g_hz: typing.Callable[[], T_Result],
        thirteen6804432g_hz: typing.Callable[[], T_Result],
        seventeen6048648g_hz: typing.Callable[[], T_Result],
        eighteen6264648g_hz: typing.Callable[[], T_Result],
        nineteen6480648g_hz: typing.Callable[[], T_Result],
        twenty6696648g_hz: typing.Callable[[], T_Result],
        twenty_five6156864g_hz: typing.Callable[[], T_Result],
        twenty_six6372864g_hz: typing.Callable[[], T_Result],
        twenty_seven6588864g_hz: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is InterfaceRfChannelLabel.ONE2412M_HZ:
            return one2412m_hz()
        if self is InterfaceRfChannelLabel.TWO2417M_HZ:
            return two2417m_hz()
        if self is InterfaceRfChannelLabel.THREE2422M_HZ:
            return three2422m_hz()
        if self is InterfaceRfChannelLabel.FOUR2427M_HZ:
            return four2427m_hz()
        if self is InterfaceRfChannelLabel.FIVE2432M_HZ:
            return five2432m_hz()
        if self is InterfaceRfChannelLabel.SIX2437M_HZ:
            return six2437m_hz()
        if self is InterfaceRfChannelLabel.SEVEN2442M_HZ:
            return seven2442m_hz()
        if self is InterfaceRfChannelLabel.EIGHT2447M_HZ:
            return eight2447m_hz()
        if self is InterfaceRfChannelLabel.NINE2452M_HZ:
            return nine2452m_hz()
        if self is InterfaceRfChannelLabel.TEN2457M_HZ:
            return ten2457m_hz()
        if self is InterfaceRfChannelLabel.ELEVEN2462M_HZ:
            return eleven2462m_hz()
        if self is InterfaceRfChannelLabel.TWELVE2467M_HZ:
            return twelve2467m_hz()
        if self is InterfaceRfChannelLabel.THIRTEEN2472M_HZ:
            return thirteen2472m_hz()
        if self is InterfaceRfChannelLabel.THIRTY_TWO516020M_HZ:
            return thirty_two516020m_hz()
        if self is InterfaceRfChannelLabel.THIRTY_FOUR517040M_HZ:
            return thirty_four517040m_hz()
        if self is InterfaceRfChannelLabel.THIRTY_SIX518020M_HZ:
            return thirty_six518020m_hz()
        if self is InterfaceRfChannelLabel.THIRTY_EIGHT519040M_HZ:
            return thirty_eight519040m_hz()
        if self is InterfaceRfChannelLabel.FORTY520020M_HZ:
            return forty520020m_hz()
        if self is InterfaceRfChannelLabel.FORTY_TWO521080M_HZ:
            return forty_two521080m_hz()
        if self is InterfaceRfChannelLabel.FORTY_FOUR522020M_HZ:
            return forty_four522020m_hz()
        if self is InterfaceRfChannelLabel.FORTY_SIX523040M_HZ:
            return forty_six523040m_hz()
        if self is InterfaceRfChannelLabel.FORTY_EIGHT524020M_HZ:
            return forty_eight524020m_hz()
        if self is InterfaceRfChannelLabel.FIFTY5250160M_HZ:
            return fifty5250160m_hz()
        if self is InterfaceRfChannelLabel.FIFTY_TWO526020M_HZ:
            return fifty_two526020m_hz()
        if self is InterfaceRfChannelLabel.FIFTY_FOUR527040M_HZ:
            return fifty_four527040m_hz()
        if self is InterfaceRfChannelLabel.FIFTY_SIX528020M_HZ:
            return fifty_six528020m_hz()
        if self is InterfaceRfChannelLabel.FIFTY_EIGHT529080M_HZ:
            return fifty_eight529080m_hz()
        if self is InterfaceRfChannelLabel.SIXTY530020M_HZ:
            return sixty530020m_hz()
        if self is InterfaceRfChannelLabel.SIXTY_TWO531040M_HZ:
            return sixty_two531040m_hz()
        if self is InterfaceRfChannelLabel.SIXTY_FOUR532020M_HZ:
            return sixty_four532020m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED550020M_HZ:
            return one_hundred550020m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_TWO551040M_HZ:
            return one_hundred_two551040m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_FOUR552020M_HZ:
            return one_hundred_four552020m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_SIX553080M_HZ:
            return one_hundred_six553080m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_EIGHT554020M_HZ:
            return one_hundred_eight554020m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_TEN555040M_HZ:
            return one_hundred_ten555040m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_TWELVE556020M_HZ:
            return one_hundred_twelve556020m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_FOURTEEN5570160M_HZ:
            return one_hundred_fourteen5570160m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_SIXTEEN558020M_HZ:
            return one_hundred_sixteen558020m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_EIGHTEEN559040M_HZ:
            return one_hundred_eighteen559040m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_TWENTY560020M_HZ:
            return one_hundred_twenty560020m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_TWENTY_TWO561080M_HZ:
            return one_hundred_twenty_two561080m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_TWENTY_FOUR562020M_HZ:
            return one_hundred_twenty_four562020m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_TWENTY_SIX563040M_HZ:
            return one_hundred_twenty_six563040m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_TWENTY_EIGHT564020M_HZ:
            return one_hundred_twenty_eight564020m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_THIRTY_TWO566020M_HZ:
            return one_hundred_thirty_two566020m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_THIRTY_FOUR567040M_HZ:
            return one_hundred_thirty_four567040m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_THIRTY_SIX568020M_HZ:
            return one_hundred_thirty_six568020m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_THIRTY_EIGHT569080M_HZ:
            return one_hundred_thirty_eight569080m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_FORTY570020M_HZ:
            return one_hundred_forty570020m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_FORTY_TWO571040M_HZ:
            return one_hundred_forty_two571040m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_FORTY_FOUR572020M_HZ:
            return one_hundred_forty_four572020m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_FORTY_NINE574520M_HZ:
            return one_hundred_forty_nine574520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_FIFTY_ONE575540M_HZ:
            return one_hundred_fifty_one575540m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_FIFTY_THREE576520M_HZ:
            return one_hundred_fifty_three576520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_FIFTY_FIVE577580M_HZ:
            return one_hundred_fifty_five577580m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_FIFTY_SEVEN578520M_HZ:
            return one_hundred_fifty_seven578520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_FIFTY_NINE579540M_HZ:
            return one_hundred_fifty_nine579540m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_SIXTY_ONE580520M_HZ:
            return one_hundred_sixty_one580520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_SIXTY_THREE5815160M_HZ:
            return one_hundred_sixty_three5815160m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_SIXTY_FIVE582520M_HZ:
            return one_hundred_sixty_five582520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_SIXTY_SEVEN583540M_HZ:
            return one_hundred_sixty_seven583540m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_SIXTY_NINE584520M_HZ:
            return one_hundred_sixty_nine584520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_SEVENTY_ONE585580M_HZ:
            return one_hundred_seventy_one585580m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_SEVENTY_THREE586520M_HZ:
            return one_hundred_seventy_three586520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_SEVENTY_FIVE587540M_HZ:
            return one_hundred_seventy_five587540m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_SEVENTY_SEVEN588520M_HZ:
            return one_hundred_seventy_seven588520m_hz()
        if self is InterfaceRfChannelLabel.ONE595520M_HZ:
            return one595520m_hz()
        if self is InterfaceRfChannelLabel.THREE596540M_HZ:
            return three596540m_hz()
        if self is InterfaceRfChannelLabel.FIVE597520M_HZ:
            return five597520m_hz()
        if self is InterfaceRfChannelLabel.SEVEN598580M_HZ:
            return seven598580m_hz()
        if self is InterfaceRfChannelLabel.NINE599520M_HZ:
            return nine599520m_hz()
        if self is InterfaceRfChannelLabel.ELEVEN600540M_HZ:
            return eleven600540m_hz()
        if self is InterfaceRfChannelLabel.THIRTEEN601520M_HZ:
            return thirteen601520m_hz()
        if self is InterfaceRfChannelLabel.FIFTEEN6025160M_HZ:
            return fifteen6025160m_hz()
        if self is InterfaceRfChannelLabel.SEVENTEEN603520M_HZ:
            return seventeen603520m_hz()
        if self is InterfaceRfChannelLabel.NINETEEN604540M_HZ:
            return nineteen604540m_hz()
        if self is InterfaceRfChannelLabel.TWENTY_ONE605520M_HZ:
            return twenty_one605520m_hz()
        if self is InterfaceRfChannelLabel.TWENTY_THREE606580M_HZ:
            return twenty_three606580m_hz()
        if self is InterfaceRfChannelLabel.TWENTY_FIVE607520M_HZ:
            return twenty_five607520m_hz()
        if self is InterfaceRfChannelLabel.TWENTY_SEVEN608540M_HZ:
            return twenty_seven608540m_hz()
        if self is InterfaceRfChannelLabel.TWENTY_NINE609520M_HZ:
            return twenty_nine609520m_hz()
        if self is InterfaceRfChannelLabel.THIRTY_ONE6105320M_HZ:
            return thirty_one6105320m_hz()
        if self is InterfaceRfChannelLabel.THIRTY_THREE611520M_HZ:
            return thirty_three611520m_hz()
        if self is InterfaceRfChannelLabel.THIRTY_FIVE612540M_HZ:
            return thirty_five612540m_hz()
        if self is InterfaceRfChannelLabel.THIRTY_SEVEN613520M_HZ:
            return thirty_seven613520m_hz()
        if self is InterfaceRfChannelLabel.THIRTY_NINE614580M_HZ:
            return thirty_nine614580m_hz()
        if self is InterfaceRfChannelLabel.FORTY_ONE615520M_HZ:
            return forty_one615520m_hz()
        if self is InterfaceRfChannelLabel.FORTY_THREE616540M_HZ:
            return forty_three616540m_hz()
        if self is InterfaceRfChannelLabel.FORTY_FIVE617520M_HZ:
            return forty_five617520m_hz()
        if self is InterfaceRfChannelLabel.FORTY_SEVEN6185160M_HZ:
            return forty_seven6185160m_hz()
        if self is InterfaceRfChannelLabel.FORTY_NINE619520M_HZ:
            return forty_nine619520m_hz()
        if self is InterfaceRfChannelLabel.FIFTY_ONE620540M_HZ:
            return fifty_one620540m_hz()
        if self is InterfaceRfChannelLabel.FIFTY_THREE621520M_HZ:
            return fifty_three621520m_hz()
        if self is InterfaceRfChannelLabel.FIFTY_FIVE622580M_HZ:
            return fifty_five622580m_hz()
        if self is InterfaceRfChannelLabel.FIFTY_SEVEN623520M_HZ:
            return fifty_seven623520m_hz()
        if self is InterfaceRfChannelLabel.FIFTY_NINE624540M_HZ:
            return fifty_nine624540m_hz()
        if self is InterfaceRfChannelLabel.SIXTY_ONE625520M_HZ:
            return sixty_one625520m_hz()
        if self is InterfaceRfChannelLabel.SIXTY_FIVE627520M_HZ:
            return sixty_five627520m_hz()
        if self is InterfaceRfChannelLabel.SIXTY_SEVEN628540M_HZ:
            return sixty_seven628540m_hz()
        if self is InterfaceRfChannelLabel.SIXTY_NINE629520M_HZ:
            return sixty_nine629520m_hz()
        if self is InterfaceRfChannelLabel.SEVENTY_ONE630580M_HZ:
            return seventy_one630580m_hz()
        if self is InterfaceRfChannelLabel.SEVENTY_THREE631520M_HZ:
            return seventy_three631520m_hz()
        if self is InterfaceRfChannelLabel.SEVENTY_FIVE632540M_HZ:
            return seventy_five632540m_hz()
        if self is InterfaceRfChannelLabel.SEVENTY_SEVEN633520M_HZ:
            return seventy_seven633520m_hz()
        if self is InterfaceRfChannelLabel.SEVENTY_NINE6345160M_HZ:
            return seventy_nine6345160m_hz()
        if self is InterfaceRfChannelLabel.EIGHTY_ONE635520M_HZ:
            return eighty_one635520m_hz()
        if self is InterfaceRfChannelLabel.EIGHTY_THREE636540M_HZ:
            return eighty_three636540m_hz()
        if self is InterfaceRfChannelLabel.EIGHTY_FIVE637520M_HZ:
            return eighty_five637520m_hz()
        if self is InterfaceRfChannelLabel.EIGHTY_SEVEN638580M_HZ:
            return eighty_seven638580m_hz()
        if self is InterfaceRfChannelLabel.EIGHTY_NINE639520M_HZ:
            return eighty_nine639520m_hz()
        if self is InterfaceRfChannelLabel.NINETY_ONE640540M_HZ:
            return ninety_one640540m_hz()
        if self is InterfaceRfChannelLabel.NINETY_THREE641520M_HZ:
            return ninety_three641520m_hz()
        if self is InterfaceRfChannelLabel.NINETY_FIVE6425320M_HZ:
            return ninety_five6425320m_hz()
        if self is InterfaceRfChannelLabel.NINETY_SEVEN643520M_HZ:
            return ninety_seven643520m_hz()
        if self is InterfaceRfChannelLabel.NINETY_NINE644540M_HZ:
            return ninety_nine644540m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_ONE645520M_HZ:
            return one_hundred_one645520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_THREE646580M_HZ:
            return one_hundred_three646580m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_FIVE647520M_HZ:
            return one_hundred_five647520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_SEVEN648540M_HZ:
            return one_hundred_seven648540m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_NINE649520M_HZ:
            return one_hundred_nine649520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_ELEVEN6505160M_HZ:
            return one_hundred_eleven6505160m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_THIRTEEN651520M_HZ:
            return one_hundred_thirteen651520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_FIFTEEN652540M_HZ:
            return one_hundred_fifteen652540m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_SEVENTEEN653520M_HZ:
            return one_hundred_seventeen653520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_NINETEEN654580M_HZ:
            return one_hundred_nineteen654580m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_TWENTY_ONE655520M_HZ:
            return one_hundred_twenty_one655520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_TWENTY_THREE656540M_HZ:
            return one_hundred_twenty_three656540m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_TWENTY_FIVE657520M_HZ:
            return one_hundred_twenty_five657520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_TWENTY_NINE659520M_HZ:
            return one_hundred_twenty_nine659520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_THIRTY_ONE660540M_HZ:
            return one_hundred_thirty_one660540m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_THIRTY_THREE661520M_HZ:
            return one_hundred_thirty_three661520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_THIRTY_FIVE662580M_HZ:
            return one_hundred_thirty_five662580m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_THIRTY_SEVEN663520M_HZ:
            return one_hundred_thirty_seven663520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_THIRTY_NINE664540M_HZ:
            return one_hundred_thirty_nine664540m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_FORTY_ONE665520M_HZ:
            return one_hundred_forty_one665520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_FORTY_THREE6665160M_HZ:
            return one_hundred_forty_three6665160m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_FORTY_FIVE667520M_HZ:
            return one_hundred_forty_five667520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_FORTY_SEVEN668540M_HZ:
            return one_hundred_forty_seven668540m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_FORTY_NINE669520M_HZ:
            return one_hundred_forty_nine669520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_FIFTY_ONE670580M_HZ:
            return one_hundred_fifty_one670580m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_FIFTY_THREE671520M_HZ:
            return one_hundred_fifty_three671520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_FIFTY_FIVE672540M_HZ:
            return one_hundred_fifty_five672540m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_FIFTY_SEVEN673520M_HZ:
            return one_hundred_fifty_seven673520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_FIFTY_NINE6745320M_HZ:
            return one_hundred_fifty_nine6745320m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_SIXTY_ONE675520M_HZ:
            return one_hundred_sixty_one675520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_SIXTY_THREE676540M_HZ:
            return one_hundred_sixty_three676540m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_SIXTY_FIVE677520M_HZ:
            return one_hundred_sixty_five677520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_SIXTY_SEVEN678580M_HZ:
            return one_hundred_sixty_seven678580m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_SIXTY_NINE679520M_HZ:
            return one_hundred_sixty_nine679520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_SEVENTY_ONE680540M_HZ:
            return one_hundred_seventy_one680540m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_SEVENTY_THREE681520M_HZ:
            return one_hundred_seventy_three681520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_SEVENTY_FIVE6825160M_HZ:
            return one_hundred_seventy_five6825160m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_SEVENTY_SEVEN683520M_HZ:
            return one_hundred_seventy_seven683520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_SEVENTY_NINE684540M_HZ:
            return one_hundred_seventy_nine684540m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_EIGHTY_ONE685520M_HZ:
            return one_hundred_eighty_one685520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_EIGHTY_THREE686580M_HZ:
            return one_hundred_eighty_three686580m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_EIGHTY_FIVE687520M_HZ:
            return one_hundred_eighty_five687520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_EIGHTY_SEVEN688540M_HZ:
            return one_hundred_eighty_seven688540m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_EIGHTY_NINE689520M_HZ:
            return one_hundred_eighty_nine689520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_NINETY_THREE691520M_HZ:
            return one_hundred_ninety_three691520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_NINETY_FIVE692540M_HZ:
            return one_hundred_ninety_five692540m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_NINETY_SEVEN693520M_HZ:
            return one_hundred_ninety_seven693520m_hz()
        if self is InterfaceRfChannelLabel.ONE_HUNDRED_NINETY_NINE694580M_HZ:
            return one_hundred_ninety_nine694580m_hz()
        if self is InterfaceRfChannelLabel.TWO_HUNDRED_ONE695520M_HZ:
            return two_hundred_one695520m_hz()
        if self is InterfaceRfChannelLabel.TWO_HUNDRED_THREE696540M_HZ:
            return two_hundred_three696540m_hz()
        if self is InterfaceRfChannelLabel.TWO_HUNDRED_FIVE697520M_HZ:
            return two_hundred_five697520m_hz()
        if self is InterfaceRfChannelLabel.TWO_HUNDRED_SEVEN6985160M_HZ:
            return two_hundred_seven6985160m_hz()
        if self is InterfaceRfChannelLabel.TWO_HUNDRED_NINE699520M_HZ:
            return two_hundred_nine699520m_hz()
        if self is InterfaceRfChannelLabel.TWO_HUNDRED_ELEVEN700540M_HZ:
            return two_hundred_eleven700540m_hz()
        if self is InterfaceRfChannelLabel.TWO_HUNDRED_THIRTEEN701520M_HZ:
            return two_hundred_thirteen701520m_hz()
        if self is InterfaceRfChannelLabel.TWO_HUNDRED_FIFTEEN702580M_HZ:
            return two_hundred_fifteen702580m_hz()
        if self is InterfaceRfChannelLabel.TWO_HUNDRED_SEVENTEEN703520M_HZ:
            return two_hundred_seventeen703520m_hz()
        if self is InterfaceRfChannelLabel.TWO_HUNDRED_NINETEEN704540M_HZ:
            return two_hundred_nineteen704540m_hz()
        if self is InterfaceRfChannelLabel.TWO_HUNDRED_TWENTY_ONE705520M_HZ:
            return two_hundred_twenty_one705520m_hz()
        if self is InterfaceRfChannelLabel.TWO_HUNDRED_TWENTY_FIVE707520M_HZ:
            return two_hundred_twenty_five707520m_hz()
        if self is InterfaceRfChannelLabel.TWO_HUNDRED_TWENTY_SEVEN708540M_HZ:
            return two_hundred_twenty_seven708540m_hz()
        if self is InterfaceRfChannelLabel.TWO_HUNDRED_TWENTY_NINE709520M_HZ:
            return two_hundred_twenty_nine709520m_hz()
        if self is InterfaceRfChannelLabel.TWO_HUNDRED_THIRTY_THREE711520M_HZ:
            return two_hundred_thirty_three711520m_hz()
        if self is InterfaceRfChannelLabel.ONE5832216G_HZ:
            return one5832216g_hz()
        if self is InterfaceRfChannelLabel.TWO6048216G_HZ:
            return two6048216g_hz()
        if self is InterfaceRfChannelLabel.THREE6264216G_HZ:
            return three6264216g_hz()
        if self is InterfaceRfChannelLabel.FOUR6480216G_HZ:
            return four6480216g_hz()
        if self is InterfaceRfChannelLabel.FIVE6696216G_HZ:
            return five6696216g_hz()
        if self is InterfaceRfChannelLabel.SIX6912216G_HZ:
            return six6912216g_hz()
        if self is InterfaceRfChannelLabel.NINE5940432G_HZ:
            return nine5940432g_hz()
        if self is InterfaceRfChannelLabel.TEN6156432G_HZ:
            return ten6156432g_hz()
        if self is InterfaceRfChannelLabel.ELEVEN6372432G_HZ:
            return eleven6372432g_hz()
        if self is InterfaceRfChannelLabel.TWELVE6588432G_HZ:
            return twelve6588432g_hz()
        if self is InterfaceRfChannelLabel.THIRTEEN6804432G_HZ:
            return thirteen6804432g_hz()
        if self is InterfaceRfChannelLabel.SEVENTEEN6048648G_HZ:
            return seventeen6048648g_hz()
        if self is InterfaceRfChannelLabel.EIGHTEEN6264648G_HZ:
            return eighteen6264648g_hz()
        if self is InterfaceRfChannelLabel.NINETEEN6480648G_HZ:
            return nineteen6480648g_hz()
        if self is InterfaceRfChannelLabel.TWENTY6696648G_HZ:
            return twenty6696648g_hz()
        if self is InterfaceRfChannelLabel.TWENTY_FIVE6156864G_HZ:
            return twenty_five6156864g_hz()
        if self is InterfaceRfChannelLabel.TWENTY_SIX6372864G_HZ:
            return twenty_six6372864g_hz()
        if self is InterfaceRfChannelLabel.TWENTY_SEVEN6588864G_HZ:
            return twenty_seven6588864g_hz()
