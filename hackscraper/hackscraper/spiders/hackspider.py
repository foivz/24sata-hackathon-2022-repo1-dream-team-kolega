import scrapy
from hackscraper.items import HackscraperItem
from scrapy.loader import ItemLoader


class HackSpider(scrapy.Spider):
    name = 'hacker'
    start_urls = ['https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=pice-sc.104972889%2Fpivo-c.561338429',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=pice-sc.104972889%2Fnegazirani-sokovi-c.561338410',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=pice-sc.104972889%2Fvoda-c.561338425',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=pice-sc.104972889%2Fzestoka-alkoholna-pica-c.561338408',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=pice-sc.104972889%2Fgazirani-sokovi-c.561338404',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=pice-sc.104972889%2Fvinoteka-c.561338424',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=pice-sc.104972889%2Fenergetska-pica-c.561338403',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=pice-sc.104972889%2Fpraskasti-napitak-i-sumece-tablete-c.561338422',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=mlijecni-proizvodi-i-jaja-sc.104972890%2Fmlijeko-c.561338418',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=mlijecni-proizvodi-i-jaja-sc.104972890%2Fdesert-c.561338426',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=mlijecni-proizvodi-i-jaja-sc.104972890%2Fjogurt-c.561338423',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=mlijecni-proizvodi-i-jaja-sc.104972890%2Fvrhnje-c.561338420',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=mlijecni-proizvodi-i-jaja-sc.104972890%2Fsir-c.561338416',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=mlijecni-proizvodi-i-jaja-sc.104972890%2Fmaslac-margarin-c.561338421',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=mlijecni-proizvodi-i-jaja-sc.104972890%2Fnamazi-c.561338417',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=mlijecni-proizvodi-i-jaja-sc.104972890%2Fjaja-c.561338419',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=voce-i-povrce-sc.104972888%2Fvoce-i-povrce-c.561338412',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=grickalice-i-slatkisi-sc.104972891%2Fcokolade-i-bomboniere-c.561338428',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=grickalice-i-slatkisi-sc.104972891%2Fbomboni-zvakace-gume-c.561338413',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=grickalice-i-slatkisi-sc.104972891%2Fgrickalice-c.561338400',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=grickalice-i-slatkisi-sc.104972891%2Fkeksi-c.561338399',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=delikatesa-sc.104972892%2Fsalame-i-naresci-c.561338414',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=delikatesa-sc.104972892%2Fkobasice-i-hrenovke-c.561338398',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=delikatesa-sc.104972892%2Fsuhomesnato-c.561338405',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=gotova-i-konzervirana-hrana-sc.104972881%2Fkonzervirano-povrce-c.561338409',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=gotova-i-konzervirana-hrana-sc.104972881%2Fpasteta-i-mesni-proizvodi-c.561338396',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=gotova-i-konzervirana-hrana-sc.104972881%2Fjuhe-c.561338395',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=gotova-i-konzervirana-hrana-sc.104972881%2Friblje-konzerve-c.561338391',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=smrznuta-hrana-sc.104972882%2Fsmrznuta-hrana-c.561338394',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=osnovne-namirnice-sc.104972884%2Fpriprema-kolaca-i-tijesta-c.561338397',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=osnovne-namirnice-sc.104972884%2Fpriprema-jela-c.561338407',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=osnovne-namirnice-sc.104972884%2Fumaci-i-zacini-c.561338393',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=osnovne-namirnice-sc.104972884%2Ftjestenina-riza-njoki-tortilje-c.561338392',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=osobna-njega-i-bebe-sc.104972885%2Fbebe-i-mame-c.561338387',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=osobna-njega-i-bebe-sc.104972885%2Fnjega-i-higijena-c.561338427',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=domacinstvo-i-kucni-ljubimci-sc.104972887%2Fciscenje-i-pospremanje-c.561338411',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=domacinstvo-i-kucni-ljubimci-sc.104972887%2Fkucni-ljubimci-c.561338401',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=domacinstvo-i-kucni-ljubimci-sc.104972887%2Fbaterije-c.561338402',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=dorucak-i-topli-napitci-sc.104972886%2Fkava-i-caj-c.561338406',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=dorucak-i-topli-napitci-sc.104972886%2Fpahuljice-i-namazi-c.561338389',
                  'https://glovoapp.com/hr/hr/zagreb/tommy-zagreb/?content=dorucak-i-topli-napitci-sc.104972886%2Fzdravi-kutak-c.561338388',
                  'https://glovoapp.com/hr/hr/zagreb/studenac-zag/?content=pice-sc.106790449%2Fpice-c.571721108',
                  'https://glovoapp.com/hr/hr/zagreb/studenac-zag/?content=grickalice-i-slatkisi-sc.106790450%2Fgrickalice-i-slatkisi-c.571721115',
                  'https://glovoapp.com/hr/hr/zagreb/studenac-zag/?content=mlijecni-proizvodi-sc.106790451%2Fmlijecni-proizvodi-c.571721109',
                  'https://glovoapp.com/hr/hr/zagreb/studenac-zag/?content=osnovne-namirnice-sc.106790452%2Fosnovne-namirnice-c.571721112',
                  'https://glovoapp.com/hr/hr/zagreb/studenac-zag/?content=voce-i-povrce-sc.106790453%2Fvoce-i-povrce-c.571721110',
                  'https://glovoapp.com/hr/hr/zagreb/studenac-zag/?content=gotova-i-konzervirana-hrana-sc.106790454%2Fgotova-i-konzervirana-hrana-c.571721127',
                  'https://glovoapp.com/hr/hr/zagreb/studenac-zag/?content=delikatesa-sc.106790455%2Fdelikatesa-c.571721107',
                  'https://glovoapp.com/hr/hr/zagreb/studenac-zag/?content=meso-sc.106790456%2Fmeso-c.571721131',
                  'https://glovoapp.com/hr/hr/zagreb/studenac-zag/?content=smrznuta-hrana-sc.106790457%2Fsmrznuta-hrana-c.571721114',
                  'https://glovoapp.com/hr/hr/zagreb/studenac-zag/?content=osobna-njega-i-bebe-sc.106790458%2Fosobna-njega-i-bebe-c.571721113',
                  'https://glovoapp.com/hr/hr/zagreb/studenac-zag/?content=deserti-sc.106790460%2Fdeserti-c.571721106',
                  'https://glovoapp.com/hr/hr/zagreb/studenac-zag/?content=domacinstvo-sc.106790459%2Fdomacinstvo-c.571721111',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=pice-sc.102429012%2Fpivo-c.547638677',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=pice-sc.102429012%2Fgazirani-sokovi-c.547638744',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=pice-sc.102429012%2Fnegazirani-sokovi-c.547638743',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=pice-sc.102429012%2Fenergetski-napitak-c.547638697',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=pice-sc.102429012%2Fledeni-caj-c.547638745',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=pice-sc.102429012%2Fgazirana-voda-c.547638739',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=pice-sc.102429012%2Fnegazirana-voda-c.547638738',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=pice-sc.102429012%2Fpraskasti-napitak-i-sumece-tablete-c.547638672',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=pice-sc.102429012%2Fzestoka-alkoholna-pica-c.547638742',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=pice-sc.102429012%2Fvino-c.547638740',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=pice-sc.102429012%2Fhladeni-napitci-c.547638852',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=pice-sc.102429012%2Fsirupi-c.547638741',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=tiskovina-sc.102429013%2Fnovine-c.547638779',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=tiskovina-sc.102429013%2Fcasopis-c.547638786',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=tiskovina-sc.102429013%2Fslicice-i-navijanje-c.547638751',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=tiskovina-sc.102429013%2Fkrizaljka-c.547638773',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=mlijecni-proizvodi-sc.102429014%2Fmargarin-c.547638781',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=mlijecni-proizvodi-sc.102429014%2Fsir-topljeni-sir-svjezi-sir-c.547638771',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=mlijecni-proizvodi-sc.102429014%2Fjogurt-c.547638788',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=mlijecni-proizvodi-sc.102429014%2Fvocni-jogurt-c.547638863',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=mlijecni-proizvodi-sc.102429014%2Fvrhnje-c.547638862',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=mlijecni-proizvodi-sc.102429014%2Fmaslac-c.547638794',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=mlijecni-proizvodi-sc.102429014%2Fmlijeko-c.547638699',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=mlijecni-proizvodi-sc.102429014%2Fdeserti-c.547638716',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=mlijecni-proizvodi-sc.102429014%2Fproteinski-proizvodi-c.547638861',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=slatkisi-i-grickalice-sc.102429015%2Fkolaci-c.547638690',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=slatkisi-i-grickalice-sc.102429015%2Fkrekeri-c.547638680',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=slatkisi-i-grickalice-sc.102429015%2Fcips-c.547638696',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=slatkisi-i-grickalice-sc.102429015%2Fflips-c.547638695',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=slatkisi-i-grickalice-sc.102429015%2Fstapici-c.547638688',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=slatkisi-i-grickalice-sc.102429015%2Fkikiriki-i-orasasti-plodovi-c.547638691',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=slatkisi-i-grickalice-sc.102429015%2Fpereci-c.547638847',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=slatkisi-i-grickalice-sc.102429015%2Fkokice-i-kukuruz-c.547638679',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=slatkisi-i-grickalice-sc.102429015%2Fbomboni-zvakace-gume-c.547638684',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=slatkisi-i-grickalice-sc.102429015%2Fcokolade-c.547638683',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=slatkisi-i-grickalice-sc.102429015%2Fkeksi-c.547638702',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=slatkisi-i-grickalice-sc.102429015%2Fvafli-i-napolitanke-c.547638704',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=slatkisi-i-grickalice-sc.102429015%2Fbomboniere-c.547638673',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=svjeze-voce-i-povrce-sc.102429016%2Fpovrce-c.547638714',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=svjeze-voce-i-povrce-sc.102429016%2Fvoce-c.547638717',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=delikatesa-sc.102429017%2Fkobasice-hrenovke-c.547638674',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=delikatesa-sc.102429017%2Fsalame-c.547638715',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=delikatesa-sc.102429017%2Fpiletina-i-puretina-c.547638712',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=mesnica-sc.102429018%2Fprsut-slanina-cvarci-c.547638675',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=mesnica-sc.102429018%2Fmeso-i-mesne-preradevine-c.547638707',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=smrznute-namirnice-sc.102429019%2Fsladoledi-i-deserti-c.547638774',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=smrznute-namirnice-sc.102429019%2Fsmrznuto-voce-c.547638706',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=smrznute-namirnice-sc.102429019%2Fsmrznuto-povrce-c.547638710',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=smrznute-namirnice-sc.102429019%2Fsmrznuto-meso-c.547638711',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=smrznute-namirnice-sc.102429019%2Fsmrznuta-tijesta-c.547638778',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=smrznute-namirnice-sc.102429019%2Fsmrznuta-riba-c.547638719',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Fbrasno-c.547638796',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Ftoast-dvopek-c.547638797',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Ftjestenina-c.547638698',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Friza-c.547638864',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Fzacini-dodatci-jelima-c.547638669',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Fulje-c.547638693',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Fcornflakes-c.547638889',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Fcappucino-c.547638671',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Fsecer-c.547638689',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Fgotova-jela-c.547638692',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Frajcica-c.547638758',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Fnapitci-c.547638890',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Fslatki-namazi-c.547638705',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Fpasteta-i-mesni-proizvodi-c.547638709',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Friblje-konzerve-c.547638701',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Fketchup-senf-majoneza-c.547638718',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Fsirni-i-mlijecni-namazi-c.547638798',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Flistovi-za-kore-savijace-c.547638703',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Fkruh-c.547638883',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Fpecivo-c.547638888',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Fkrafna-c.547638682',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Fkvasac-c.547638887',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Fjaja-c.547638737',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Fgotove-kreme-c.547638768',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Fsastojci-za-kolace-c.547638708',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Fpalenta-c.547638799',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Fjuhe-u-vrecici-c.547638668',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Fjuhe-u-kocki-c.547638667',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Flisnato-tijesto-c.547638891',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osnovne-namirnice-sc.102429020%2Fgris-c.547638780',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osobna-njega-i-bebe-sc.102429021%2Fnjega-tijela-c.547638763',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osobna-njega-i-bebe-sc.102429021%2Fnjega-kose-c.547638749',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osobna-njega-i-bebe-sc.102429021%2Foralna-higijena-c.547638800',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osobna-njega-i-bebe-sc.102429021%2Fbrijanje-c.547638676',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osobna-njega-i-bebe-sc.102429021%2Fdezodorans-c.547638783',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osobna-njega-i-bebe-sc.102429021%2Ftoaletni-papir-c.547638666',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osobna-njega-i-bebe-sc.102429021%2Fdjecja-hrana-c.547638777',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osobna-njega-i-bebe-sc.102429021%2Fpelene-c.547638766',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osobna-njega-i-bebe-sc.102429021%2Fsampon-i-kupka-c.547638769',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osobna-njega-i-bebe-sc.102429021%2Fkasice-za-bebe-c.547638885',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osobna-njega-i-bebe-sc.102429021%2Ftekuci-sapuni-c.547638762',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osobna-njega-i-bebe-sc.102429021%2Fhigijenski-ulosci-c.547638764',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osobna-njega-i-bebe-sc.102429021%2Fpapirnate-maramice-c.547638789',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osobna-njega-i-bebe-sc.102429021%2Fkreme-c.547638784',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osobna-njega-i-bebe-sc.102429021%2Fstapici-za-usi-c.547638790',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osobna-njega-i-bebe-sc.102429021%2Fkondomi-c.547638782',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osobna-njega-i-bebe-sc.102429021%2Fostalo-c.547638765',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osobna-njega-i-bebe-sc.102429021%2Fcvrsti-sapuni-c.547638678',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osobna-njega-i-bebe-sc.102429021%2Fpoklon-paketi-c.547638793',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=osobna-njega-i-bebe-sc.102429021%2Fvlazne-maramice-c.547638750',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=dorucak-i-topli-napitci-sc.102429023%2Fkava-c.547638681',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=dorucak-i-topli-napitci-sc.102429023%2Finstant-kava-c.547638686',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=dorucak-i-topli-napitci-sc.102429023%2Fzitne-loptice-c.547638767',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=dorucak-i-topli-napitci-sc.102429023%2Fcaj-c.547638694',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=dorucak-i-topli-napitci-sc.102429023%2Fzobene-pahuljice-c.547638884',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=dorucak-i-topli-napitci-sc.102429023%2Fmuesli-c.547638886',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=dorucak-i-topli-napitci-sc.102429023%2Fdorucak-c.547638791',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=domacinstvo-i-kucni-ljubimci-sc.102429031%2Fhrana-za-pse-c.547638747',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=domacinstvo-i-kucni-ljubimci-sc.102429031%2Fhrana-za-macke-c.547638746',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=domacinstvo-i-kucni-ljubimci-sc.102429031%2Fdeterdzenti-i-omeksivac-i-za-rublje-c.547638753',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=domacinstvo-i-kucni-ljubimci-sc.102429031%2Fsredstva-za-pranje-posuda-i-stakla-c.547638759',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=domacinstvo-i-kucni-ljubimci-sc.102429031%2Fsredstva-za-ciscenje-kupaonice-i-wc-a-c.547638761',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=domacinstvo-i-kucni-ljubimci-sc.102429031%2Fsredstva-za-ciscenje-kuhinje-c.547638755',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=domacinstvo-i-kucni-ljubimci-sc.102429031%2Fabrazivna-sredstva-za-ciscenje-c.547638756',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=domacinstvo-i-kucni-ljubimci-sc.102429031%2Fsredstva-za-ciscenje-drvenih-povrsina-c.547638849',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=domacinstvo-i-kucni-ljubimci-sc.102429031%2Fsolna-kiselina-c.547638757',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=domacinstvo-i-kucni-ljubimci-sc.102429031%2Fpapirnati-rucnici-c.547638787',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=domacinstvo-i-kucni-ljubimci-sc.102429031%2Ffolija-c.547638775',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=domacinstvo-i-kucni-ljubimci-sc.102429031%2Fpribor-za-ciscenje-c.547638770',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=domacinstvo-i-kucni-ljubimci-sc.102429031%2Fkocke-za-potpalu-c.547638772',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=domacinstvo-i-kucni-ljubimci-sc.102429031%2Fvrece-c.547638687',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=domacinstvo-i-kucni-ljubimci-sc.102429031%2Fzarulje-c.547638851',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=domacinstvo-i-kucni-ljubimci-sc.102429031%2Flampioni-c.547638670',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=domacinstvo-i-kucni-ljubimci-sc.102429031%2Fljepilo-c.547638795',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=domacinstvo-i-kucni-ljubimci-sc.102429031%2Ffolija-papir-za-pecenje-c.547638792',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=domacinstvo-i-kucni-ljubimci-sc.102429031%2Fkrpe-spuzvice-c.547638785',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=domacinstvo-i-kucni-ljubimci-sc.102429031%2Fpribor-za-ciscnje-c.547638760',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=domacinstvo-i-kucni-ljubimci-sc.102429031%2Finsekticidi-c.547638752',
                  'https://glovoapp.com/hr/hr/zagreb/lonia/?content=skolski-pribor-sc.102429032%2Fskolski-pribor-c.547638754'
                  ]

    def parse(self, response):

        tag = str(response.css('p.list__title::text').get())

        store = str(response)[39: str(response).index('?')-1]

        for products in response.css('div.product-row'):
            l = ItemLoader(item = HackscraperItem(), selector=products)

            l.add_css('name', 'div.product-row__name')
            l.add_css('price', 'span.product-price__effective.product-price__effective--new-card::text')
            l.add_css('link', 'img.product-row__image::attr(src)')
            l.add_value('tag', tag)
            l.add_value('store', store)

            yield l.load_item()


        #next_page = response.css('a.action.next').attrib['href']
        #if next_page is not None:
        #    yield response.follow(next_page, callback=self.parse)