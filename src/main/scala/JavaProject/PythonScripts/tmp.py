#import pymongo 
import sys 
import os 
#from pymongo import MongoClient 
from moveBatch import moveBatch
rString = moveBatch([0.6485319410878442,0.19515390653325326,0.6179816186714856,0.7270793126297952,0.7220249733213719,0.60063957812815,0.37698868919102113,0.44377915478472696,0.415472189903225,0.4144023378134696,0.1321660096807279,0.8815775669148704,0.44361740803636707,0.3604208899387067,0.4998704774975943,0.6475077662501026,0.44942062616608325,0.10900819659622141,0.40871067995383337,0.2254446434921431,0.3146882973771804,0.7070729384740678,0.3411548569646683,0.3232837688480217,0.10630370700938185,0.43070006379724124,0.15527806107120856,0.4613445915823743,0.3662516878944152,0.47989208997438904,0.8296991200558841,0.4009607651767234,0.37887456029453614,0.5761728272951995,0.9349805678005031,0.609147878757105,0.8400983403335325,0.853341637270018,0.7486590017789811,0.6881278420316066,0.8515407146644877,0.9187752796825657,0.7275133891212572,0.9066889532954598,0.8696568702613965,0.9477866460260085,0.9016041169531737,0.6608660338530068,0.06842678404169,0.7040231952512226,0.5511068981240371,0.20746592536044428,0.9323171234453859,0.4922332908867032,0.24954922664552404,0.8361292592752652,0.9778760609251625,0.7071435627474729,0.45792504550593327,0.1658972581849537,0.742957417172885,0.49982082910480574,0.08421976349800886,0.05166472771904129,0.22672846394866364,0.07158729553749343,0.30769973868174605,0.4187024227327629,0.6298737445649105,0.9496274687115329,0.2826968647697483,0.16518091122612544,0.15452202029728634,0.9941851993105069,0.4789412274769401,0.11233464326964704,0.17347884657408597,0.9340134731870287,0.31674173130143013,0.7477704643024262,0.5773423059007801,0.2896670488403198,0.3463814588599897,0.6150020398421588,0.8435646567421972,0.813917272825304,0.2370723703932539,0.7770076814920249,0.19966450745962439,0.7479374449594178,0.4930761742494978,0.13681669192167234,0.5845481697772698,0.25379936406030823,0.42607350198910376,0.45345735245029917,0.8895578742398725,0.6937246197733994,0.9048914693080808,0.059126363948225236,0.7644473487425425,0.36018370837697833,0.5832642937363318,0.10770187455812064,0.7627266307059783,0.816959480451711,0.3556611018830813,0.8034343952085555,0.14659649418339415,0.31420968120004833,0.8774887507119397,0.4099274819590123,0.7939827220716122,0.053877349518645534,0.2706204982552599,0.983280632429421,0.33034550625437065,0.3512933142397261,0.24420012180947215,0.7248664124141313,0.38564125123513293,0.8662549185288055,0.984334537630978,0.644865265371643,0.7793780437725423,0.3195785209312578,0.8592141806358387,0.4974078256907536,0.8351710110055789,0.9846036851372995,0.805228620001229,0.33061430984104145,0.32303430387615095,0.6775600768991856,0.9375112350888618,0.38176736898072317,0.9729304364220778,0.3548454212726456,0.6362741790084069,0.39503039705161913,0.713121886971466,0.8859730911104104,0.8113307633549272,0.6073452533368231,0.6970571833336013,0.4389405192486253,0.6850515240290775,0.6356429810138576,0.6815416429077494,0.555282873799394,0.19468217011887068,0.4365361157513089,0.8679017855260173,0.9829011998313089,0.8885871449964278,0.1035000420227501,0.307282324700463,0.8765404279028207,0.9122887962855414,0.9135572164582297,0.258502218974351,0.8828889649795588,0.768264571143532,0.45185357103468404,0.6977656704634634,0.20365978194614265,0.15223601671556042,0.6252528705134158,0.799098470273881,0.1242082231436572,0.550430730925768,0.7615325455475569,0.8656465999110796,0.33585270128699496,0.8346760119495268,0.7655204550593383,0.18245038288550786,0.9483412722495707,0.8604793843940802,0.1106130529716749,0.8772813281176128,0.872576135869599,0.9960199581976086,0.6321958768332799,0.28826128964365605,0.793747274791731,0.7815422846726424,0.44492291412218576,0.05511513595960471,0.8549184191641994,0.5845623137816678,0.932282989779145,0.9303725327774759,0.8398745229095969,0.514198779231054,0.7875128480613011,0.27012134682127775,0.5803775870972386,0.6713249850448054,0.652179667233994,0.8231942423260777,0.9533520971781781,0.05973771071678957,0.2670753523079943,0.46805586159655166,0.6551043424369957,0.596519676716012,0.9715925627596989,0.4356772779800111,0.6197087886308623,0.10531999671406667,0.8857245544700649,0.9977368239521504,0.37365591080846206,0.9942294537340948,0.3422852344472387,0.6788761577700368,0.5166965654269539,0.6619998827042354,0.8324478103183443,0.7753660071150797,0.10831404514655274,0.8491535841170779,0.4024444913448273,0.5248945997275836,0.8473919923474057,0.48156969860500076,0.09044666214971386,0.11212829559603799,0.839339678025642,0.9275296408381751,0.8050423621812295,0.9409631669631737,0.6002530464520807,0.7534912325879604,0.3017812850275202,0.06839472447432471,0.48998616840018006,0.6563374000032296,0.2561730345747639,0.703962872069135,0.10821881575977343,0.9966202511017821,0.9970229761070989,0.3670839185147089,0.29925629621173555,0.5249633936513984,0.40820602506428183,0.46831720217566075,0.0964416345369502,0.8201938863402256,0.345958345952479,0.6488733453279967,0.48131913802910475,0.791043015320202,0.70352699389436,0.06668133211736749,0.43618988600606046,0.6112404683152584,0.740893413346608,0.8386826158982462,0.8303275334112155,0.410080237584891,0.37273927915204275,0.6966127331862361,0.8108306297150343,0.45890821576991603,0.8883452830131368,0.7727616869737359,0.725212344962034,0.29096540365898327,0.8320043056923107,0.2872233412802644,0.6951912382074615,0.3922447796336972,0.6045362524517871,0.6953881507387553,0.3701724349579567,0.13665741101109075,0.31534820012963416,0.41751693055999983,0.3254988891337651,0.835969813288999,0.8536543769202952,0.2973264822440643,0.8644631207386008,0.6600738479444304,0.13481866009068277,0.7970576149229935,0.24548371855444295,0.2808847470770748,0.7547440789974993,0.24321426022713843,0.2697175185534679,0.5506858875335241,0.8604662714761908,0.8911896975767539,0.7095615485983039,0.4508300321936194,0.2420977036939409,0.13977982799841027,0.9620138028395524,0.6756623713394037,0.45677114678663155,0.7233758636782551,0.1163958749209284,0.7924661516314869,0.9880163278500254,0.9850963464258599,0.099303431394138,0.39831947025702086,0.5462774066703066,0.8981091125513916,0.2898707041305195,0.7450755391978493,0.9220325701153853,0.48990887079297507,0.1301638723999795,0.45112399420617,0.6596297254681809,0.7675711210792945,0.8755652477749682,0.3030848163016929,0.6767673389298026,0.33702904162533676,0.8452486015255791,0.25126779430025736,0.8765860080990482,0.3329606234326792,0.450830647311275,0.2001329974256364,0.056588298964899586,0.5209873153141792,0.12944317861767374,0.9837858621578455,0.5650562028455872,0.5645291852411733,0.333429767776085,0.9547255877511195,0.22338132752094164,0.8414298289306309,0.8127543610413416,0.09323162223816561,0.6150747032630209,0.4096617922512842,0.5455745547202355,0.5796595540845252,0.6902305640507752,0.9972054531375001,0.8318390949804007,0.24478377038416477,0.9090161218584792,0.8716982285367599,0.6440161050216867,0.7902270494389487,0.3528368111316751,0.39636882451932376,0.6835865613085157,0.3740185587397875,0.17265525164465745,0.7669776427359929,0.470804875732048,0.2710254247461925,0.815294284822649,0.7003456827173863,0.13636691247966615,0.592728091528527,0.9237667213185659,0.6372625764488765,0.4005788033257248,0.7301284936476679,0.4453470496080725,0.7440900564721334,0.3387507351261324,0.9345203309953674,0.41298187234695716,0.6224607364288783,0.1462454305457015,0.33809104801459733,0.5827217458172492,0.7488873622878539,0.703379768077728,0.20495134181730368,0.38680711642979526,0.7826800854935327,0.9419008112035557,0.7756658202016539,0.8431975417204433,0.9479074125502599,0.5993707079365905,0.8312205534532061,0.18305415278640313,0.5360185023869334,0.09860138199291535,0.058759422729908306,0.8405861248229157,0.30012768873532536,0.16184632331666238,0.46313748842364644,0.8684051503854602,0.06054618178874416,0.13808897825950028,0.3005724278948615,0.3608492936037736,0.5418623609189495,0.2548465895430878,0.16803123610757886,0.7581747275705207,0.36127023143901627,0.8168935826221458,0.26988061860234924,0.13399087027072032,0.12070888920821243,0.8098048808374719,0.15151516002291254,0.23408362883459644,0.6448975588542185,0.3711279620783626,0.13994473601192836,0.9736726015524847,0.11602778102855726,0.6707542566215675,0.429010642160496,0.21411424316177952,0.5621503217804211,0.27350738526326224,0.36725635105859833,0.721059327853568,0.48842719309043203,0.13052564529478106,0.9955942781266967,0.28168286921373353,0.7975233670626458,0.44127013450478336,0.7521325937155184,0.7868981687789585,0.35686201142143625,0.8507906196146855,0.14396284193200282,0.3259680912775398,0.45508157352130907,0.9727078342326724,0.7766317860526285,0.693927935060027,0.8601563170022841,0.050790884460174324,0.942697200055606,0.651874780752948,0.5641704477776709,0.9085539648015555,0.42700626644944584,0.5414181258715525,0.428470761866502,0.9557772995798994,0.6076653889611107,0.8579569473333241,0.7981184459301376,0.8652104821130873,0.3841428591462739,0.45706864358352994,0.1699167684368762,0.09521183830743007,0.36433896048860315,0.8927255285234211,0.8758100769871178,0.88484400419842,0.6367340019626746,0.7480668709443303,0.4698954611401591,0.8119674579734572,0.11977097952179283,0.8027905965124523,0.5870073340561636,0.9940366488892779,0.27917492133945987,0.6682751437717435,0.6761148620061471,0.6058300871145946,0.30171529728525115,0.9940210639444055,0.16672161316839307,0.46265363717336827,0.42492389669535724,0.298674690265469,0.09120581955655249,0.06908657269296681,0.24546460910768764,0.551198521838022,0.3688624360703736,0.07371065120458353,0.9974241131237812,0.45702138376674306,0.3723562952382261,0.11315804199335644,0.5498529500135899,0.8471660507529779,0.9383803730694726,0.712831935337986,0.35692494982213496,0.806137912177505,0.7599614214205009,0.2443564674695411,0.9455899244884312,0.13501072710589668,0.8456018349572932,0.34374128857538044,0.4243462036482488,0.8262039464581727,0.15379914300763908,0.3890409073498323,0.09998453996278656,0.7409744843535422,0.20297964708106875,0.10622112984895937,0.4242230763930738,0.31495182940739985,0.26176651178953547,0.5975652874235181,0.7798320701403615,0.5820495893861547,0.08713376899128134,0.06623255216860613,0.4096619396547495,0.9829659845018484,0.6869721369803631,0.9814993643918294,0.7995976507715968,0.9548893898503533,0.082268971172332,0.1497541785926444,0.8988440057895328,0.985916351814285,0.7953665133865273,0.18698023395615837,0.704747289198609,0.7776299355430305,0.3668701237776163,0.4436090713000309,0.24480298797271538,0.1604489649046863,0.3459943009608979,0.6055302640831299,0.8776506310037555,0.31615956068973305,0.3263351948805292,0.48314577407880943,0.7149248423822337,0.7285902809703806,0.39565404990267095,0.38254277998612196,0.6070825477996326,0.4423604182774642,0.17050392778841084,0.8805995844684095,0.530027175907977,0.7420931862210753,0.7665894007712732,0.7667369323376797,0.8639026285864527,0.6868657307811603,0.5669372542488348,0.4338864456372349,0.34383779999024366,0.1810429850957801,0.43377229893036395,0.5038422434969796,0.17646886351274815,0.15759380653449384,0.6505525366155896,0.6141547528929454,0.8614807598202141,0.9662652049068539,0.9238136460911321,0.9457720263984799,0.2820933361684792,0.6198837159324107,0.8124340081505578,0.854000789101511,0.2537504765941687,0.6501577191285687,0.6293539169429643,0.295275378956963,0.9462849615656125,0.8141223688283995,0.9588245413047773,0.8403307166067743,0.7492171474496361,0.11490956720840662,0.6858116566576505,0.7261479184797783,0.6594740288174713,0.2593679493718124,0.8143482856087918,0.36635078947827493,0.4756973352907481,0.8673737389577072,0.36379530849541686,0.37288315830436924,0.9979835535704766,0.07835852357504636],0.0)
print str(rString)
