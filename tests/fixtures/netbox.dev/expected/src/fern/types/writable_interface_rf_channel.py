

import typing

from ..core import enum

T_Result = typing.TypeVar("T_Result")


class WritableInterfaceRfChannel(enum.StrEnum):
    TWO4G1241222 = "2.4g-1-2412-22"
    TWO4G2241722 = "2.4g-2-2417-22"
    TWO4G3242222 = "2.4g-3-2422-22"
    TWO4G4242722 = "2.4g-4-2427-22"
    TWO4G5243222 = "2.4g-5-2432-22"
    TWO4G6243722 = "2.4g-6-2437-22"
    TWO4G7244222 = "2.4g-7-2442-22"
    TWO4G8244722 = "2.4g-8-2447-22"
    TWO4G9245222 = "2.4g-9-2452-22"
    TWO4G10245722 = "2.4g-10-2457-22"
    TWO4G11246222 = "2.4g-11-2462-22"
    TWO4G12246722 = "2.4g-12-2467-22"
    TWO4G13247222 = "2.4g-13-2472-22"
    FIVE_G32516020 = "5g-32-5160-20"
    FIVE_G34517040 = "5g-34-5170-40"
    FIVE_G36518020 = "5g-36-5180-20"
    FIVE_G38519040 = "5g-38-5190-40"
    FIVE_G40520020 = "5g-40-5200-20"
    FIVE_G42521080 = "5g-42-5210-80"
    FIVE_G44522020 = "5g-44-5220-20"
    FIVE_G46523040 = "5g-46-5230-40"
    FIVE_G48524020 = "5g-48-5240-20"
    FIVE_G505250160 = "5g-50-5250-160"
    FIVE_G52526020 = "5g-52-5260-20"
    FIVE_G54527040 = "5g-54-5270-40"
    FIVE_G56528020 = "5g-56-5280-20"
    FIVE_G58529080 = "5g-58-5290-80"
    FIVE_G60530020 = "5g-60-5300-20"
    FIVE_G62531040 = "5g-62-5310-40"
    FIVE_G64532020 = "5g-64-5320-20"
    FIVE_G100550020 = "5g-100-5500-20"
    FIVE_G102551040 = "5g-102-5510-40"
    FIVE_G104552020 = "5g-104-5520-20"
    FIVE_G106553080 = "5g-106-5530-80"
    FIVE_G108554020 = "5g-108-5540-20"
    FIVE_G110555040 = "5g-110-5550-40"
    FIVE_G112556020 = "5g-112-5560-20"
    FIVE_G1145570160 = "5g-114-5570-160"
    FIVE_G116558020 = "5g-116-5580-20"
    FIVE_G118559040 = "5g-118-5590-40"
    FIVE_G120560020 = "5g-120-5600-20"
    FIVE_G122561080 = "5g-122-5610-80"
    FIVE_G124562020 = "5g-124-5620-20"
    FIVE_G126563040 = "5g-126-5630-40"
    FIVE_G128564020 = "5g-128-5640-20"
    FIVE_G132566020 = "5g-132-5660-20"
    FIVE_G134567040 = "5g-134-5670-40"
    FIVE_G136568020 = "5g-136-5680-20"
    FIVE_G138569080 = "5g-138-5690-80"
    FIVE_G140570020 = "5g-140-5700-20"
    FIVE_G142571040 = "5g-142-5710-40"
    FIVE_G144572020 = "5g-144-5720-20"
    FIVE_G149574520 = "5g-149-5745-20"
    FIVE_G151575540 = "5g-151-5755-40"
    FIVE_G153576520 = "5g-153-5765-20"
    FIVE_G155577580 = "5g-155-5775-80"
    FIVE_G157578520 = "5g-157-5785-20"
    FIVE_G159579540 = "5g-159-5795-40"
    FIVE_G161580520 = "5g-161-5805-20"
    FIVE_G1635815160 = "5g-163-5815-160"
    FIVE_G165582520 = "5g-165-5825-20"
    FIVE_G167583540 = "5g-167-5835-40"
    FIVE_G169584520 = "5g-169-5845-20"
    FIVE_G171585580 = "5g-171-5855-80"
    FIVE_G173586520 = "5g-173-5865-20"
    FIVE_G175587540 = "5g-175-5875-40"
    FIVE_G177588520 = "5g-177-5885-20"
    SIX_G1595520 = "6g-1-5955-20"
    SIX_G3596540 = "6g-3-5965-40"
    SIX_G5597520 = "6g-5-5975-20"
    SIX_G7598580 = "6g-7-5985-80"
    SIX_G9599520 = "6g-9-5995-20"
    SIX_G11600540 = "6g-11-6005-40"
    SIX_G13601520 = "6g-13-6015-20"
    SIX_G156025160 = "6g-15-6025-160"
    SIX_G17603520 = "6g-17-6035-20"
    SIX_G19604540 = "6g-19-6045-40"
    SIX_G21605520 = "6g-21-6055-20"
    SIX_G23606580 = "6g-23-6065-80"
    SIX_G25607520 = "6g-25-6075-20"
    SIX_G27608540 = "6g-27-6085-40"
    SIX_G29609520 = "6g-29-6095-20"
    SIX_G316105320 = "6g-31-6105-320"
    SIX_G33611520 = "6g-33-6115-20"
    SIX_G35612540 = "6g-35-6125-40"
    SIX_G37613520 = "6g-37-6135-20"
    SIX_G39614580 = "6g-39-6145-80"
    SIX_G41615520 = "6g-41-6155-20"
    SIX_G43616540 = "6g-43-6165-40"
    SIX_G45617520 = "6g-45-6175-20"
    SIX_G476185160 = "6g-47-6185-160"
    SIX_G49619520 = "6g-49-6195-20"
    SIX_G51620540 = "6g-51-6205-40"
    SIX_G53621520 = "6g-53-6215-20"
    SIX_G55622580 = "6g-55-6225-80"
    SIX_G57623520 = "6g-57-6235-20"
    SIX_G59624540 = "6g-59-6245-40"
    SIX_G61625520 = "6g-61-6255-20"
    SIX_G65627520 = "6g-65-6275-20"
    SIX_G67628540 = "6g-67-6285-40"
    SIX_G69629520 = "6g-69-6295-20"
    SIX_G71630580 = "6g-71-6305-80"
    SIX_G73631520 = "6g-73-6315-20"
    SIX_G75632540 = "6g-75-6325-40"
    SIX_G77633520 = "6g-77-6335-20"
    SIX_G796345160 = "6g-79-6345-160"
    SIX_G81635520 = "6g-81-6355-20"
    SIX_G83636540 = "6g-83-6365-40"
    SIX_G85637520 = "6g-85-6375-20"
    SIX_G87638580 = "6g-87-6385-80"
    SIX_G89639520 = "6g-89-6395-20"
    SIX_G91640540 = "6g-91-6405-40"
    SIX_G93641520 = "6g-93-6415-20"
    SIX_G956425320 = "6g-95-6425-320"
    SIX_G97643520 = "6g-97-6435-20"
    SIX_G99644540 = "6g-99-6445-40"
    SIX_G101645520 = "6g-101-6455-20"
    SIX_G103646580 = "6g-103-6465-80"
    SIX_G105647520 = "6g-105-6475-20"
    SIX_G107648540 = "6g-107-6485-40"
    SIX_G109649520 = "6g-109-6495-20"
    SIX_G1116505160 = "6g-111-6505-160"
    SIX_G113651520 = "6g-113-6515-20"
    SIX_G115652540 = "6g-115-6525-40"
    SIX_G117653520 = "6g-117-6535-20"
    SIX_G119654580 = "6g-119-6545-80"
    SIX_G121655520 = "6g-121-6555-20"
    SIX_G123656540 = "6g-123-6565-40"
    SIX_G125657520 = "6g-125-6575-20"
    SIX_G129659520 = "6g-129-6595-20"
    SIX_G131660540 = "6g-131-6605-40"
    SIX_G133661520 = "6g-133-6615-20"
    SIX_G135662580 = "6g-135-6625-80"
    SIX_G137663520 = "6g-137-6635-20"
    SIX_G139664540 = "6g-139-6645-40"
    SIX_G141665520 = "6g-141-6655-20"
    SIX_G1436665160 = "6g-143-6665-160"
    SIX_G145667520 = "6g-145-6675-20"
    SIX_G147668540 = "6g-147-6685-40"
    SIX_G149669520 = "6g-149-6695-20"
    SIX_G151670580 = "6g-151-6705-80"
    SIX_G153671520 = "6g-153-6715-20"
    SIX_G155672540 = "6g-155-6725-40"
    SIX_G157673520 = "6g-157-6735-20"
    SIX_G1596745320 = "6g-159-6745-320"
    SIX_G161675520 = "6g-161-6755-20"
    SIX_G163676540 = "6g-163-6765-40"
    SIX_G165677520 = "6g-165-6775-20"
    SIX_G167678580 = "6g-167-6785-80"
    SIX_G169679520 = "6g-169-6795-20"
    SIX_G171680540 = "6g-171-6805-40"
    SIX_G173681520 = "6g-173-6815-20"
    SIX_G1756825160 = "6g-175-6825-160"
    SIX_G177683520 = "6g-177-6835-20"
    SIX_G179684540 = "6g-179-6845-40"
    SIX_G181685520 = "6g-181-6855-20"
    SIX_G183686580 = "6g-183-6865-80"
    SIX_G185687520 = "6g-185-6875-20"
    SIX_G187688540 = "6g-187-6885-40"
    SIX_G189689520 = "6g-189-6895-20"
    SIX_G193691520 = "6g-193-6915-20"
    SIX_G195692540 = "6g-195-6925-40"
    SIX_G197693520 = "6g-197-6935-20"
    SIX_G199694580 = "6g-199-6945-80"
    SIX_G201695520 = "6g-201-6955-20"
    SIX_G203696540 = "6g-203-6965-40"
    SIX_G205697520 = "6g-205-6975-20"
    SIX_G2076985160 = "6g-207-6985-160"
    SIX_G209699520 = "6g-209-6995-20"
    SIX_G211700540 = "6g-211-7005-40"
    SIX_G213701520 = "6g-213-7015-20"
    SIX_G215702580 = "6g-215-7025-80"
    SIX_G217703520 = "6g-217-7035-20"
    SIX_G219704540 = "6g-219-7045-40"
    SIX_G221705520 = "6g-221-7055-20"
    SIX_G225707520 = "6g-225-7075-20"
    SIX_G227708540 = "6g-227-7085-40"
    SIX_G229709520 = "6g-229-7095-20"
    SIX_G233711520 = "6g-233-7115-20"
    SIXTY_G1583202160 = "60g-1-58320-2160"
    SIXTY_G2604802160 = "60g-2-60480-2160"
    SIXTY_G3626402160 = "60g-3-62640-2160"
    SIXTY_G4648002160 = "60g-4-64800-2160"
    SIXTY_G5669602160 = "60g-5-66960-2160"
    SIXTY_G6691202160 = "60g-6-69120-2160"
    SIXTY_G9594004320 = "60g-9-59400-4320"
    SIXTY_G10615604320 = "60g-10-61560-4320"
    SIXTY_G11637204320 = "60g-11-63720-4320"
    SIXTY_G12658804320 = "60g-12-65880-4320"
    SIXTY_G13680404320 = "60g-13-68040-4320"
    SIXTY_G17604806480 = "60g-17-60480-6480"
    SIXTY_G18626406480 = "60g-18-62640-6480"
    SIXTY_G19648006480 = "60g-19-64800-6480"
    SIXTY_G20669606480 = "60g-20-66960-6480"
    SIXTY_G25615606480 = "60g-25-61560-6480"
    SIXTY_G26637206480 = "60g-26-63720-6480"
    SIXTY_G27658806480 = "60g-27-65880-6480"

    def visit(
        self,
        two4g1241222: typing.Callable[[], T_Result],
        two4g2241722: typing.Callable[[], T_Result],
        two4g3242222: typing.Callable[[], T_Result],
        two4g4242722: typing.Callable[[], T_Result],
        two4g5243222: typing.Callable[[], T_Result],
        two4g6243722: typing.Callable[[], T_Result],
        two4g7244222: typing.Callable[[], T_Result],
        two4g8244722: typing.Callable[[], T_Result],
        two4g9245222: typing.Callable[[], T_Result],
        two4g10245722: typing.Callable[[], T_Result],
        two4g11246222: typing.Callable[[], T_Result],
        two4g12246722: typing.Callable[[], T_Result],
        two4g13247222: typing.Callable[[], T_Result],
        five_g32516020: typing.Callable[[], T_Result],
        five_g34517040: typing.Callable[[], T_Result],
        five_g36518020: typing.Callable[[], T_Result],
        five_g38519040: typing.Callable[[], T_Result],
        five_g40520020: typing.Callable[[], T_Result],
        five_g42521080: typing.Callable[[], T_Result],
        five_g44522020: typing.Callable[[], T_Result],
        five_g46523040: typing.Callable[[], T_Result],
        five_g48524020: typing.Callable[[], T_Result],
        five_g505250160: typing.Callable[[], T_Result],
        five_g52526020: typing.Callable[[], T_Result],
        five_g54527040: typing.Callable[[], T_Result],
        five_g56528020: typing.Callable[[], T_Result],
        five_g58529080: typing.Callable[[], T_Result],
        five_g60530020: typing.Callable[[], T_Result],
        five_g62531040: typing.Callable[[], T_Result],
        five_g64532020: typing.Callable[[], T_Result],
        five_g100550020: typing.Callable[[], T_Result],
        five_g102551040: typing.Callable[[], T_Result],
        five_g104552020: typing.Callable[[], T_Result],
        five_g106553080: typing.Callable[[], T_Result],
        five_g108554020: typing.Callable[[], T_Result],
        five_g110555040: typing.Callable[[], T_Result],
        five_g112556020: typing.Callable[[], T_Result],
        five_g1145570160: typing.Callable[[], T_Result],
        five_g116558020: typing.Callable[[], T_Result],
        five_g118559040: typing.Callable[[], T_Result],
        five_g120560020: typing.Callable[[], T_Result],
        five_g122561080: typing.Callable[[], T_Result],
        five_g124562020: typing.Callable[[], T_Result],
        five_g126563040: typing.Callable[[], T_Result],
        five_g128564020: typing.Callable[[], T_Result],
        five_g132566020: typing.Callable[[], T_Result],
        five_g134567040: typing.Callable[[], T_Result],
        five_g136568020: typing.Callable[[], T_Result],
        five_g138569080: typing.Callable[[], T_Result],
        five_g140570020: typing.Callable[[], T_Result],
        five_g142571040: typing.Callable[[], T_Result],
        five_g144572020: typing.Callable[[], T_Result],
        five_g149574520: typing.Callable[[], T_Result],
        five_g151575540: typing.Callable[[], T_Result],
        five_g153576520: typing.Callable[[], T_Result],
        five_g155577580: typing.Callable[[], T_Result],
        five_g157578520: typing.Callable[[], T_Result],
        five_g159579540: typing.Callable[[], T_Result],
        five_g161580520: typing.Callable[[], T_Result],
        five_g1635815160: typing.Callable[[], T_Result],
        five_g165582520: typing.Callable[[], T_Result],
        five_g167583540: typing.Callable[[], T_Result],
        five_g169584520: typing.Callable[[], T_Result],
        five_g171585580: typing.Callable[[], T_Result],
        five_g173586520: typing.Callable[[], T_Result],
        five_g175587540: typing.Callable[[], T_Result],
        five_g177588520: typing.Callable[[], T_Result],
        six_g1595520: typing.Callable[[], T_Result],
        six_g3596540: typing.Callable[[], T_Result],
        six_g5597520: typing.Callable[[], T_Result],
        six_g7598580: typing.Callable[[], T_Result],
        six_g9599520: typing.Callable[[], T_Result],
        six_g11600540: typing.Callable[[], T_Result],
        six_g13601520: typing.Callable[[], T_Result],
        six_g156025160: typing.Callable[[], T_Result],
        six_g17603520: typing.Callable[[], T_Result],
        six_g19604540: typing.Callable[[], T_Result],
        six_g21605520: typing.Callable[[], T_Result],
        six_g23606580: typing.Callable[[], T_Result],
        six_g25607520: typing.Callable[[], T_Result],
        six_g27608540: typing.Callable[[], T_Result],
        six_g29609520: typing.Callable[[], T_Result],
        six_g316105320: typing.Callable[[], T_Result],
        six_g33611520: typing.Callable[[], T_Result],
        six_g35612540: typing.Callable[[], T_Result],
        six_g37613520: typing.Callable[[], T_Result],
        six_g39614580: typing.Callable[[], T_Result],
        six_g41615520: typing.Callable[[], T_Result],
        six_g43616540: typing.Callable[[], T_Result],
        six_g45617520: typing.Callable[[], T_Result],
        six_g476185160: typing.Callable[[], T_Result],
        six_g49619520: typing.Callable[[], T_Result],
        six_g51620540: typing.Callable[[], T_Result],
        six_g53621520: typing.Callable[[], T_Result],
        six_g55622580: typing.Callable[[], T_Result],
        six_g57623520: typing.Callable[[], T_Result],
        six_g59624540: typing.Callable[[], T_Result],
        six_g61625520: typing.Callable[[], T_Result],
        six_g65627520: typing.Callable[[], T_Result],
        six_g67628540: typing.Callable[[], T_Result],
        six_g69629520: typing.Callable[[], T_Result],
        six_g71630580: typing.Callable[[], T_Result],
        six_g73631520: typing.Callable[[], T_Result],
        six_g75632540: typing.Callable[[], T_Result],
        six_g77633520: typing.Callable[[], T_Result],
        six_g796345160: typing.Callable[[], T_Result],
        six_g81635520: typing.Callable[[], T_Result],
        six_g83636540: typing.Callable[[], T_Result],
        six_g85637520: typing.Callable[[], T_Result],
        six_g87638580: typing.Callable[[], T_Result],
        six_g89639520: typing.Callable[[], T_Result],
        six_g91640540: typing.Callable[[], T_Result],
        six_g93641520: typing.Callable[[], T_Result],
        six_g956425320: typing.Callable[[], T_Result],
        six_g97643520: typing.Callable[[], T_Result],
        six_g99644540: typing.Callable[[], T_Result],
        six_g101645520: typing.Callable[[], T_Result],
        six_g103646580: typing.Callable[[], T_Result],
        six_g105647520: typing.Callable[[], T_Result],
        six_g107648540: typing.Callable[[], T_Result],
        six_g109649520: typing.Callable[[], T_Result],
        six_g1116505160: typing.Callable[[], T_Result],
        six_g113651520: typing.Callable[[], T_Result],
        six_g115652540: typing.Callable[[], T_Result],
        six_g117653520: typing.Callable[[], T_Result],
        six_g119654580: typing.Callable[[], T_Result],
        six_g121655520: typing.Callable[[], T_Result],
        six_g123656540: typing.Callable[[], T_Result],
        six_g125657520: typing.Callable[[], T_Result],
        six_g129659520: typing.Callable[[], T_Result],
        six_g131660540: typing.Callable[[], T_Result],
        six_g133661520: typing.Callable[[], T_Result],
        six_g135662580: typing.Callable[[], T_Result],
        six_g137663520: typing.Callable[[], T_Result],
        six_g139664540: typing.Callable[[], T_Result],
        six_g141665520: typing.Callable[[], T_Result],
        six_g1436665160: typing.Callable[[], T_Result],
        six_g145667520: typing.Callable[[], T_Result],
        six_g147668540: typing.Callable[[], T_Result],
        six_g149669520: typing.Callable[[], T_Result],
        six_g151670580: typing.Callable[[], T_Result],
        six_g153671520: typing.Callable[[], T_Result],
        six_g155672540: typing.Callable[[], T_Result],
        six_g157673520: typing.Callable[[], T_Result],
        six_g1596745320: typing.Callable[[], T_Result],
        six_g161675520: typing.Callable[[], T_Result],
        six_g163676540: typing.Callable[[], T_Result],
        six_g165677520: typing.Callable[[], T_Result],
        six_g167678580: typing.Callable[[], T_Result],
        six_g169679520: typing.Callable[[], T_Result],
        six_g171680540: typing.Callable[[], T_Result],
        six_g173681520: typing.Callable[[], T_Result],
        six_g1756825160: typing.Callable[[], T_Result],
        six_g177683520: typing.Callable[[], T_Result],
        six_g179684540: typing.Callable[[], T_Result],
        six_g181685520: typing.Callable[[], T_Result],
        six_g183686580: typing.Callable[[], T_Result],
        six_g185687520: typing.Callable[[], T_Result],
        six_g187688540: typing.Callable[[], T_Result],
        six_g189689520: typing.Callable[[], T_Result],
        six_g193691520: typing.Callable[[], T_Result],
        six_g195692540: typing.Callable[[], T_Result],
        six_g197693520: typing.Callable[[], T_Result],
        six_g199694580: typing.Callable[[], T_Result],
        six_g201695520: typing.Callable[[], T_Result],
        six_g203696540: typing.Callable[[], T_Result],
        six_g205697520: typing.Callable[[], T_Result],
        six_g2076985160: typing.Callable[[], T_Result],
        six_g209699520: typing.Callable[[], T_Result],
        six_g211700540: typing.Callable[[], T_Result],
        six_g213701520: typing.Callable[[], T_Result],
        six_g215702580: typing.Callable[[], T_Result],
        six_g217703520: typing.Callable[[], T_Result],
        six_g219704540: typing.Callable[[], T_Result],
        six_g221705520: typing.Callable[[], T_Result],
        six_g225707520: typing.Callable[[], T_Result],
        six_g227708540: typing.Callable[[], T_Result],
        six_g229709520: typing.Callable[[], T_Result],
        six_g233711520: typing.Callable[[], T_Result],
        sixty_g1583202160: typing.Callable[[], T_Result],
        sixty_g2604802160: typing.Callable[[], T_Result],
        sixty_g3626402160: typing.Callable[[], T_Result],
        sixty_g4648002160: typing.Callable[[], T_Result],
        sixty_g5669602160: typing.Callable[[], T_Result],
        sixty_g6691202160: typing.Callable[[], T_Result],
        sixty_g9594004320: typing.Callable[[], T_Result],
        sixty_g10615604320: typing.Callable[[], T_Result],
        sixty_g11637204320: typing.Callable[[], T_Result],
        sixty_g12658804320: typing.Callable[[], T_Result],
        sixty_g13680404320: typing.Callable[[], T_Result],
        sixty_g17604806480: typing.Callable[[], T_Result],
        sixty_g18626406480: typing.Callable[[], T_Result],
        sixty_g19648006480: typing.Callable[[], T_Result],
        sixty_g20669606480: typing.Callable[[], T_Result],
        sixty_g25615606480: typing.Callable[[], T_Result],
        sixty_g26637206480: typing.Callable[[], T_Result],
        sixty_g27658806480: typing.Callable[[], T_Result],
    ) -> T_Result:
        if self is WritableInterfaceRfChannel.TWO4G1241222:
            return two4g1241222()
        if self is WritableInterfaceRfChannel.TWO4G2241722:
            return two4g2241722()
        if self is WritableInterfaceRfChannel.TWO4G3242222:
            return two4g3242222()
        if self is WritableInterfaceRfChannel.TWO4G4242722:
            return two4g4242722()
        if self is WritableInterfaceRfChannel.TWO4G5243222:
            return two4g5243222()
        if self is WritableInterfaceRfChannel.TWO4G6243722:
            return two4g6243722()
        if self is WritableInterfaceRfChannel.TWO4G7244222:
            return two4g7244222()
        if self is WritableInterfaceRfChannel.TWO4G8244722:
            return two4g8244722()
        if self is WritableInterfaceRfChannel.TWO4G9245222:
            return two4g9245222()
        if self is WritableInterfaceRfChannel.TWO4G10245722:
            return two4g10245722()
        if self is WritableInterfaceRfChannel.TWO4G11246222:
            return two4g11246222()
        if self is WritableInterfaceRfChannel.TWO4G12246722:
            return two4g12246722()
        if self is WritableInterfaceRfChannel.TWO4G13247222:
            return two4g13247222()
        if self is WritableInterfaceRfChannel.FIVE_G32516020:
            return five_g32516020()
        if self is WritableInterfaceRfChannel.FIVE_G34517040:
            return five_g34517040()
        if self is WritableInterfaceRfChannel.FIVE_G36518020:
            return five_g36518020()
        if self is WritableInterfaceRfChannel.FIVE_G38519040:
            return five_g38519040()
        if self is WritableInterfaceRfChannel.FIVE_G40520020:
            return five_g40520020()
        if self is WritableInterfaceRfChannel.FIVE_G42521080:
            return five_g42521080()
        if self is WritableInterfaceRfChannel.FIVE_G44522020:
            return five_g44522020()
        if self is WritableInterfaceRfChannel.FIVE_G46523040:
            return five_g46523040()
        if self is WritableInterfaceRfChannel.FIVE_G48524020:
            return five_g48524020()
        if self is WritableInterfaceRfChannel.FIVE_G505250160:
            return five_g505250160()
        if self is WritableInterfaceRfChannel.FIVE_G52526020:
            return five_g52526020()
        if self is WritableInterfaceRfChannel.FIVE_G54527040:
            return five_g54527040()
        if self is WritableInterfaceRfChannel.FIVE_G56528020:
            return five_g56528020()
        if self is WritableInterfaceRfChannel.FIVE_G58529080:
            return five_g58529080()
        if self is WritableInterfaceRfChannel.FIVE_G60530020:
            return five_g60530020()
        if self is WritableInterfaceRfChannel.FIVE_G62531040:
            return five_g62531040()
        if self is WritableInterfaceRfChannel.FIVE_G64532020:
            return five_g64532020()
        if self is WritableInterfaceRfChannel.FIVE_G100550020:
            return five_g100550020()
        if self is WritableInterfaceRfChannel.FIVE_G102551040:
            return five_g102551040()
        if self is WritableInterfaceRfChannel.FIVE_G104552020:
            return five_g104552020()
        if self is WritableInterfaceRfChannel.FIVE_G106553080:
            return five_g106553080()
        if self is WritableInterfaceRfChannel.FIVE_G108554020:
            return five_g108554020()
        if self is WritableInterfaceRfChannel.FIVE_G110555040:
            return five_g110555040()
        if self is WritableInterfaceRfChannel.FIVE_G112556020:
            return five_g112556020()
        if self is WritableInterfaceRfChannel.FIVE_G1145570160:
            return five_g1145570160()
        if self is WritableInterfaceRfChannel.FIVE_G116558020:
            return five_g116558020()
        if self is WritableInterfaceRfChannel.FIVE_G118559040:
            return five_g118559040()
        if self is WritableInterfaceRfChannel.FIVE_G120560020:
            return five_g120560020()
        if self is WritableInterfaceRfChannel.FIVE_G122561080:
            return five_g122561080()
        if self is WritableInterfaceRfChannel.FIVE_G124562020:
            return five_g124562020()
        if self is WritableInterfaceRfChannel.FIVE_G126563040:
            return five_g126563040()
        if self is WritableInterfaceRfChannel.FIVE_G128564020:
            return five_g128564020()
        if self is WritableInterfaceRfChannel.FIVE_G132566020:
            return five_g132566020()
        if self is WritableInterfaceRfChannel.FIVE_G134567040:
            return five_g134567040()
        if self is WritableInterfaceRfChannel.FIVE_G136568020:
            return five_g136568020()
        if self is WritableInterfaceRfChannel.FIVE_G138569080:
            return five_g138569080()
        if self is WritableInterfaceRfChannel.FIVE_G140570020:
            return five_g140570020()
        if self is WritableInterfaceRfChannel.FIVE_G142571040:
            return five_g142571040()
        if self is WritableInterfaceRfChannel.FIVE_G144572020:
            return five_g144572020()
        if self is WritableInterfaceRfChannel.FIVE_G149574520:
            return five_g149574520()
        if self is WritableInterfaceRfChannel.FIVE_G151575540:
            return five_g151575540()
        if self is WritableInterfaceRfChannel.FIVE_G153576520:
            return five_g153576520()
        if self is WritableInterfaceRfChannel.FIVE_G155577580:
            return five_g155577580()
        if self is WritableInterfaceRfChannel.FIVE_G157578520:
            return five_g157578520()
        if self is WritableInterfaceRfChannel.FIVE_G159579540:
            return five_g159579540()
        if self is WritableInterfaceRfChannel.FIVE_G161580520:
            return five_g161580520()
        if self is WritableInterfaceRfChannel.FIVE_G1635815160:
            return five_g1635815160()
        if self is WritableInterfaceRfChannel.FIVE_G165582520:
            return five_g165582520()
        if self is WritableInterfaceRfChannel.FIVE_G167583540:
            return five_g167583540()
        if self is WritableInterfaceRfChannel.FIVE_G169584520:
            return five_g169584520()
        if self is WritableInterfaceRfChannel.FIVE_G171585580:
            return five_g171585580()
        if self is WritableInterfaceRfChannel.FIVE_G173586520:
            return five_g173586520()
        if self is WritableInterfaceRfChannel.FIVE_G175587540:
            return five_g175587540()
        if self is WritableInterfaceRfChannel.FIVE_G177588520:
            return five_g177588520()
        if self is WritableInterfaceRfChannel.SIX_G1595520:
            return six_g1595520()
        if self is WritableInterfaceRfChannel.SIX_G3596540:
            return six_g3596540()
        if self is WritableInterfaceRfChannel.SIX_G5597520:
            return six_g5597520()
        if self is WritableInterfaceRfChannel.SIX_G7598580:
            return six_g7598580()
        if self is WritableInterfaceRfChannel.SIX_G9599520:
            return six_g9599520()
        if self is WritableInterfaceRfChannel.SIX_G11600540:
            return six_g11600540()
        if self is WritableInterfaceRfChannel.SIX_G13601520:
            return six_g13601520()
        if self is WritableInterfaceRfChannel.SIX_G156025160:
            return six_g156025160()
        if self is WritableInterfaceRfChannel.SIX_G17603520:
            return six_g17603520()
        if self is WritableInterfaceRfChannel.SIX_G19604540:
            return six_g19604540()
        if self is WritableInterfaceRfChannel.SIX_G21605520:
            return six_g21605520()
        if self is WritableInterfaceRfChannel.SIX_G23606580:
            return six_g23606580()
        if self is WritableInterfaceRfChannel.SIX_G25607520:
            return six_g25607520()
        if self is WritableInterfaceRfChannel.SIX_G27608540:
            return six_g27608540()
        if self is WritableInterfaceRfChannel.SIX_G29609520:
            return six_g29609520()
        if self is WritableInterfaceRfChannel.SIX_G316105320:
            return six_g316105320()
        if self is WritableInterfaceRfChannel.SIX_G33611520:
            return six_g33611520()
        if self is WritableInterfaceRfChannel.SIX_G35612540:
            return six_g35612540()
        if self is WritableInterfaceRfChannel.SIX_G37613520:
            return six_g37613520()
        if self is WritableInterfaceRfChannel.SIX_G39614580:
            return six_g39614580()
        if self is WritableInterfaceRfChannel.SIX_G41615520:
            return six_g41615520()
        if self is WritableInterfaceRfChannel.SIX_G43616540:
            return six_g43616540()
        if self is WritableInterfaceRfChannel.SIX_G45617520:
            return six_g45617520()
        if self is WritableInterfaceRfChannel.SIX_G476185160:
            return six_g476185160()
        if self is WritableInterfaceRfChannel.SIX_G49619520:
            return six_g49619520()
        if self is WritableInterfaceRfChannel.SIX_G51620540:
            return six_g51620540()
        if self is WritableInterfaceRfChannel.SIX_G53621520:
            return six_g53621520()
        if self is WritableInterfaceRfChannel.SIX_G55622580:
            return six_g55622580()
        if self is WritableInterfaceRfChannel.SIX_G57623520:
            return six_g57623520()
        if self is WritableInterfaceRfChannel.SIX_G59624540:
            return six_g59624540()
        if self is WritableInterfaceRfChannel.SIX_G61625520:
            return six_g61625520()
        if self is WritableInterfaceRfChannel.SIX_G65627520:
            return six_g65627520()
        if self is WritableInterfaceRfChannel.SIX_G67628540:
            return six_g67628540()
        if self is WritableInterfaceRfChannel.SIX_G69629520:
            return six_g69629520()
        if self is WritableInterfaceRfChannel.SIX_G71630580:
            return six_g71630580()
        if self is WritableInterfaceRfChannel.SIX_G73631520:
            return six_g73631520()
        if self is WritableInterfaceRfChannel.SIX_G75632540:
            return six_g75632540()
        if self is WritableInterfaceRfChannel.SIX_G77633520:
            return six_g77633520()
        if self is WritableInterfaceRfChannel.SIX_G796345160:
            return six_g796345160()
        if self is WritableInterfaceRfChannel.SIX_G81635520:
            return six_g81635520()
        if self is WritableInterfaceRfChannel.SIX_G83636540:
            return six_g83636540()
        if self is WritableInterfaceRfChannel.SIX_G85637520:
            return six_g85637520()
        if self is WritableInterfaceRfChannel.SIX_G87638580:
            return six_g87638580()
        if self is WritableInterfaceRfChannel.SIX_G89639520:
            return six_g89639520()
        if self is WritableInterfaceRfChannel.SIX_G91640540:
            return six_g91640540()
        if self is WritableInterfaceRfChannel.SIX_G93641520:
            return six_g93641520()
        if self is WritableInterfaceRfChannel.SIX_G956425320:
            return six_g956425320()
        if self is WritableInterfaceRfChannel.SIX_G97643520:
            return six_g97643520()
        if self is WritableInterfaceRfChannel.SIX_G99644540:
            return six_g99644540()
        if self is WritableInterfaceRfChannel.SIX_G101645520:
            return six_g101645520()
        if self is WritableInterfaceRfChannel.SIX_G103646580:
            return six_g103646580()
        if self is WritableInterfaceRfChannel.SIX_G105647520:
            return six_g105647520()
        if self is WritableInterfaceRfChannel.SIX_G107648540:
            return six_g107648540()
        if self is WritableInterfaceRfChannel.SIX_G109649520:
            return six_g109649520()
        if self is WritableInterfaceRfChannel.SIX_G1116505160:
            return six_g1116505160()
        if self is WritableInterfaceRfChannel.SIX_G113651520:
            return six_g113651520()
        if self is WritableInterfaceRfChannel.SIX_G115652540:
            return six_g115652540()
        if self is WritableInterfaceRfChannel.SIX_G117653520:
            return six_g117653520()
        if self is WritableInterfaceRfChannel.SIX_G119654580:
            return six_g119654580()
        if self is WritableInterfaceRfChannel.SIX_G121655520:
            return six_g121655520()
        if self is WritableInterfaceRfChannel.SIX_G123656540:
            return six_g123656540()
        if self is WritableInterfaceRfChannel.SIX_G125657520:
            return six_g125657520()
        if self is WritableInterfaceRfChannel.SIX_G129659520:
            return six_g129659520()
        if self is WritableInterfaceRfChannel.SIX_G131660540:
            return six_g131660540()
        if self is WritableInterfaceRfChannel.SIX_G133661520:
            return six_g133661520()
        if self is WritableInterfaceRfChannel.SIX_G135662580:
            return six_g135662580()
        if self is WritableInterfaceRfChannel.SIX_G137663520:
            return six_g137663520()
        if self is WritableInterfaceRfChannel.SIX_G139664540:
            return six_g139664540()
        if self is WritableInterfaceRfChannel.SIX_G141665520:
            return six_g141665520()
        if self is WritableInterfaceRfChannel.SIX_G1436665160:
            return six_g1436665160()
        if self is WritableInterfaceRfChannel.SIX_G145667520:
            return six_g145667520()
        if self is WritableInterfaceRfChannel.SIX_G147668540:
            return six_g147668540()
        if self is WritableInterfaceRfChannel.SIX_G149669520:
            return six_g149669520()
        if self is WritableInterfaceRfChannel.SIX_G151670580:
            return six_g151670580()
        if self is WritableInterfaceRfChannel.SIX_G153671520:
            return six_g153671520()
        if self is WritableInterfaceRfChannel.SIX_G155672540:
            return six_g155672540()
        if self is WritableInterfaceRfChannel.SIX_G157673520:
            return six_g157673520()
        if self is WritableInterfaceRfChannel.SIX_G1596745320:
            return six_g1596745320()
        if self is WritableInterfaceRfChannel.SIX_G161675520:
            return six_g161675520()
        if self is WritableInterfaceRfChannel.SIX_G163676540:
            return six_g163676540()
        if self is WritableInterfaceRfChannel.SIX_G165677520:
            return six_g165677520()
        if self is WritableInterfaceRfChannel.SIX_G167678580:
            return six_g167678580()
        if self is WritableInterfaceRfChannel.SIX_G169679520:
            return six_g169679520()
        if self is WritableInterfaceRfChannel.SIX_G171680540:
            return six_g171680540()
        if self is WritableInterfaceRfChannel.SIX_G173681520:
            return six_g173681520()
        if self is WritableInterfaceRfChannel.SIX_G1756825160:
            return six_g1756825160()
        if self is WritableInterfaceRfChannel.SIX_G177683520:
            return six_g177683520()
        if self is WritableInterfaceRfChannel.SIX_G179684540:
            return six_g179684540()
        if self is WritableInterfaceRfChannel.SIX_G181685520:
            return six_g181685520()
        if self is WritableInterfaceRfChannel.SIX_G183686580:
            return six_g183686580()
        if self is WritableInterfaceRfChannel.SIX_G185687520:
            return six_g185687520()
        if self is WritableInterfaceRfChannel.SIX_G187688540:
            return six_g187688540()
        if self is WritableInterfaceRfChannel.SIX_G189689520:
            return six_g189689520()
        if self is WritableInterfaceRfChannel.SIX_G193691520:
            return six_g193691520()
        if self is WritableInterfaceRfChannel.SIX_G195692540:
            return six_g195692540()
        if self is WritableInterfaceRfChannel.SIX_G197693520:
            return six_g197693520()
        if self is WritableInterfaceRfChannel.SIX_G199694580:
            return six_g199694580()
        if self is WritableInterfaceRfChannel.SIX_G201695520:
            return six_g201695520()
        if self is WritableInterfaceRfChannel.SIX_G203696540:
            return six_g203696540()
        if self is WritableInterfaceRfChannel.SIX_G205697520:
            return six_g205697520()
        if self is WritableInterfaceRfChannel.SIX_G2076985160:
            return six_g2076985160()
        if self is WritableInterfaceRfChannel.SIX_G209699520:
            return six_g209699520()
        if self is WritableInterfaceRfChannel.SIX_G211700540:
            return six_g211700540()
        if self is WritableInterfaceRfChannel.SIX_G213701520:
            return six_g213701520()
        if self is WritableInterfaceRfChannel.SIX_G215702580:
            return six_g215702580()
        if self is WritableInterfaceRfChannel.SIX_G217703520:
            return six_g217703520()
        if self is WritableInterfaceRfChannel.SIX_G219704540:
            return six_g219704540()
        if self is WritableInterfaceRfChannel.SIX_G221705520:
            return six_g221705520()
        if self is WritableInterfaceRfChannel.SIX_G225707520:
            return six_g225707520()
        if self is WritableInterfaceRfChannel.SIX_G227708540:
            return six_g227708540()
        if self is WritableInterfaceRfChannel.SIX_G229709520:
            return six_g229709520()
        if self is WritableInterfaceRfChannel.SIX_G233711520:
            return six_g233711520()
        if self is WritableInterfaceRfChannel.SIXTY_G1583202160:
            return sixty_g1583202160()
        if self is WritableInterfaceRfChannel.SIXTY_G2604802160:
            return sixty_g2604802160()
        if self is WritableInterfaceRfChannel.SIXTY_G3626402160:
            return sixty_g3626402160()
        if self is WritableInterfaceRfChannel.SIXTY_G4648002160:
            return sixty_g4648002160()
        if self is WritableInterfaceRfChannel.SIXTY_G5669602160:
            return sixty_g5669602160()
        if self is WritableInterfaceRfChannel.SIXTY_G6691202160:
            return sixty_g6691202160()
        if self is WritableInterfaceRfChannel.SIXTY_G9594004320:
            return sixty_g9594004320()
        if self is WritableInterfaceRfChannel.SIXTY_G10615604320:
            return sixty_g10615604320()
        if self is WritableInterfaceRfChannel.SIXTY_G11637204320:
            return sixty_g11637204320()
        if self is WritableInterfaceRfChannel.SIXTY_G12658804320:
            return sixty_g12658804320()
        if self is WritableInterfaceRfChannel.SIXTY_G13680404320:
            return sixty_g13680404320()
        if self is WritableInterfaceRfChannel.SIXTY_G17604806480:
            return sixty_g17604806480()
        if self is WritableInterfaceRfChannel.SIXTY_G18626406480:
            return sixty_g18626406480()
        if self is WritableInterfaceRfChannel.SIXTY_G19648006480:
            return sixty_g19648006480()
        if self is WritableInterfaceRfChannel.SIXTY_G20669606480:
            return sixty_g20669606480()
        if self is WritableInterfaceRfChannel.SIXTY_G25615606480:
            return sixty_g25615606480()
        if self is WritableInterfaceRfChannel.SIXTY_G26637206480:
            return sixty_g26637206480()
        if self is WritableInterfaceRfChannel.SIXTY_G27658806480:
            return sixty_g27658806480()
