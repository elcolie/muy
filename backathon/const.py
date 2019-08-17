URL = 'http://comtrade.un.org/api/get'
CC_FRUIT = [
    '81090',
    '81340',
    '80450',
    '81190',
    '80110',
    '80290',
    '80300',
    '80540',
    '80130',
    '80510',
    '80232',
    '81290',
    '80810',
    '80430',
    '80231',
    '80212',
    '81350',
    '80720',
    '80520',
    '81330',
]  #
CC_SUGAR = [
    # '170111',
    '170199',
    '170490',
    '170310',
    '170410',
    '170191',
    '170290',
    '170230',
    '170240',
    '170390',
    '170210',
    '170112',
    '170260',
    '170250',
    '170220',
]  # 18
CC_VEG = [
    '71410',
    '70990',
    '71029',
    '71331',
    '70310',
    '71040',
    '71080',
    '71022',
    '71390',
    '70920',
    '71339',
    '71090',
    '71190',
    '70960',
    '71332',
    '71290',
    '70951',
    '71230',
    '71490',
    '70952',
]  #
COMMODITY_CODES = [
    '070110',
    '070190',
    '070200',
    '070310',
    '070320',
    '070390',
    '070410',
    '070420',
    '070490',
    '070511',
    '070519',
    '070521',
    '070529',
    '070610',
    '070690',
    '070700',
    '070810',
    '070820',
    '070890',
    '070920',
    '070930',
    '070940',
    '070951',
    '070959',
    '070960',
    '070970',
    '070990',
    '070991',
    '070992',
    '070993',
    '070999',
    '071010',
    '071021',
    '071022',
    '071029',
    '071030',
    '071040',
    '071080',
    '071090',
    '071120',
    '071140',
    '071151',
    '071159',
    '071190',
    '071220',
    '071231',
    '071232',
    '071233',
    '071239',
    '071290',
    '071310',
    '071320',
    '071331',
    '071332',
    '071333',
    '071334',
    '071335',
    '071339',
    '071340',
    '071350',
    '071360',
    '071390',
    '071410',
    '071420',
    '071430',
    '071440',
    '071450',
    '071490',
    '080111',
    '080112',
    '080119',
    '080121',
    '080122',
    '080131',
    '080132',
    '080211',
    '080212',
    '080221',
    '080222',
    '080231',
    '080232',
    '080240',
    '080241',
    '080242',
    '080250',
    '080251',
    '080252',
    '080260',
    '080261',
    '080262',
    '080270',
    '080280',
    '080290',
    '080300',
    '080310',
    '080390',
    '080410',
    '080420',
    '080430',
    '080440',
    '080450',
    '080510',
    '080520',
    '080521',
    '080529',
    '080540',
    '080550',
    '080590',
    '080610',
    '080620',
    '080711',
    '080719',
    '080720',
    '080810',
    '080820',
    '080830',
    '080840',
    '080910',
    '080920',
    '080921',
    '080929',
    '080930',
    '080940',
    '081010',
    '081020',
    '081030',
    '081040',
    '081050',
    '081060',
    '081070',
    '081090',
    '081110',
    '081120',
    '081190',
    '081210',
    '081290',
    '081310',
    '081320',
    '081330',
    '081340',
    '081350',
    '081400',
    '170111',
    '170112',
    '170113',
    '170114',
    '170191',
    '170199',
    '170211',
    '170219',
    '170220',
    '170230',
    '170240',
    '170250',
    '170260',
    '170290',
    '170310',
    '170390',
    '170410',
    '170490',
]
TRADE_REGIMES = ['1', '2']  # https://comtrade.un.org/Data/cache/tradeRegimes.json

REPORTER_AREAS = [
    {
        "id": "all",
        "text": "All"
    },
    {
        "id": "4",
        "text": "Afghanistan"
    },
    {
        "id": "8",
        "text": "Albania"
    },
    {
        "id": "12",
        "text": "Algeria"
    },
    {
        "id": "20",
        "text": "Andorra"
    },
    {
        "id": "24",
        "text": "Angola"
    },
    {
        "id": "660",
        "text": "Anguilla"
    },
    {
        "id": "28",
        "text": "Antigua and Barbuda"
    },
    {
        "id": "32",
        "text": "Argentina"
    },
    {
        "id": "51",
        "text": "Armenia"
    },
    {
        "id": "533",
        "text": "Aruba"
    },
    {
        "id": "36",
        "text": "Australia"
    },
    {
        "id": "40",
        "text": "Austria"
    },
    {
        "id": "31",
        "text": "Azerbaijan"
    },
    {
        "id": "44",
        "text": "Bahamas"
    },
    {
        "id": "48",
        "text": "Bahrain"
    },
    {
        "id": "50",
        "text": "Bangladesh"
    },
    {
        "id": "52",
        "text": "Barbados"
    },
    {
        "id": "112",
        "text": "Belarus"
    },
    {
        "id": "56",
        "text": "Belgium"
    },
    {
        "id": "58",
        "text": "Belgium-Luxembourg"
    },
    {
        "id": "84",
        "text": "Belize"
    },
    {
        "id": "204",
        "text": "Benin"
    },
    {
        "id": "60",
        "text": "Bermuda"
    },
    {
        "id": "64",
        "text": "Bhutan"
    },
    {
        "id": "68",
        "text": "Bolivia (Plurinational State of)"
    },
    {
        "id": "535",
        "text": "Bonaire"
    },
    {
        "id": "70",
        "text": "Bosnia Herzegovina"
    },
    {
        "id": "72",
        "text": "Botswana"
    },
    {
        "id": "92",
        "text": "Br. Virgin Isds"
    },
    {
        "id": "76",
        "text": "Brazil"
    },
    {
        "id": "96",
        "text": "Brunei Darussalam"
    },
    {
        "id": "100",
        "text": "Bulgaria"
    },
    {
        "id": "854",
        "text": "Burkina Faso"
    },
    {
        "id": "108",
        "text": "Burundi"
    },
    {
        "id": "132",
        "text": "Cabo Verde"
    },
    {
        "id": "116",
        "text": "Cambodia"
    },
    {
        "id": "120",
        "text": "Cameroon"
    },
    {
        "id": "124",
        "text": "Canada"
    },
    {
        "id": "136",
        "text": "Cayman Isds"
    },
    {
        "id": "140",
        "text": "Central African Rep."
    },
    {
        "id": "148",
        "text": "Chad"
    },
    {
        "id": "152",
        "text": "Chile"
    },
    {
        "id": "156",
        "text": "China"
    },
    {
        "id": "344",
        "text": "China, Hong Kong SAR"
    },
    {
        "id": "446",
        "text": "China, Macao SAR"
    },
    {
        "id": "170",
        "text": "Colombia"
    },
    {
        "id": "174",
        "text": "Comoros"
    },
    {
        "id": "178",
        "text": "Congo"
    },
    {
        "id": "184",
        "text": "Cook Isds"
    },
    {
        "id": "188",
        "text": "Costa Rica"
    },
    {
        "id": "384",
        "text": "Côte d'Ivoire"
    },
    {
        "id": "191",
        "text": "Croatia"
    },
    {
        "id": "192",
        "text": "Cuba"
    },
    {
        "id": "531",
        "text": "Curaçao"
    },
    {
        "id": "196",
        "text": "Cyprus"
    },
    {
        "id": "203",
        "text": "Czechia"
    },
    {
        "id": "200",
        "text": "Czechoslovakia"
    },
    {
        "id": "408",
        "text": "Dem. People's Rep. of Korea"
    },
    {
        "id": "180",
        "text": "Dem. Rep. of the Congo"
    },
    {
        "id": "208",
        "text": "Denmark"
    },
    {
        "id": "262",
        "text": "Djibouti"
    },
    {
        "id": "212",
        "text": "Dominica"
    },
    {
        "id": "214",
        "text": "Dominican Rep."
    },
    {
        "id": "588",
        "text": "East and West Pakistan"
    },
    {
        "id": "218",
        "text": "Ecuador"
    },
    {
        "id": "818",
        "text": "Egypt"
    },
    {
        "id": "222",
        "text": "El Salvador"
    },
    {
        "id": "226",
        "text": "Equatorial Guinea"
    },
    {
        "id": "232",
        "text": "Eritrea"
    },
    {
        "id": "233",
        "text": "Estonia"
    },
    {
        "id": "231",
        "text": "Ethiopia"
    },
    {
        "id": "97",
        "text": "EU-28"
    },
    {
        "id": "234",
        "text": "Faeroe Isds"
    },
    {
        "id": "238",
        "text": "Falkland Isds (Malvinas)"
    },
    {
        "id": "242",
        "text": "Fiji"
    },
    {
        "id": "246",
        "text": "Finland"
    },
    {
        "id": "886",
        "text": "Fmr Arab Rep. of Yemen"
    },
    {
        "id": "278",
        "text": "Fmr Dem. Rep. of Germany"
    },
    {
        "id": "866",
        "text": "Fmr Dem. Rep. of Vietnam"
    },
    {
        "id": "720",
        "text": "Fmr Dem. Yemen"
    },
    {
        "id": "230",
        "text": "Fmr Ethiopia"
    },
    {
        "id": "280",
        "text": "Fmr Fed. Rep. of Germany"
    },
    {
        "id": "582",
        "text": "Fmr Pacific Isds"
    },
    {
        "id": "590",
        "text": "Fmr Panama, excl.Canal Zone"
    },
    {
        "id": "592",
        "text": "Fmr Panama-Canal-Zone"
    },
    {
        "id": "868",
        "text": "Fmr Rep. of Vietnam"
    },
    {
        "id": "717",
        "text": "Fmr Rhodesia Nyas"
    },
    {
        "id": "736",
        "text": "Fmr Sudan"
    },
    {
        "id": "835",
        "text": "Fmr Tanganyika"
    },
    {
        "id": "810",
        "text": "Fmr USSR"
    },
    {
        "id": "890",
        "text": "Fmr Yugoslavia"
    },
    {
        "id": "836",
        "text": "Fmr Zanzibar and Pemba Isd"
    },
    {
        "id": "251",
        "text": "France"
    },
    {
        "id": "254",
        "text": "French Guiana"
    },
    {
        "id": "258",
        "text": "French Polynesia"
    },
    {
        "id": "583",
        "text": "FS Micronesia"
    },
    {
        "id": "266",
        "text": "Gabon"
    },
    {
        "id": "270",
        "text": "Gambia"
    },
    {
        "id": "268",
        "text": "Georgia"
    },
    {
        "id": "276",
        "text": "Germany"
    },
    {
        "id": "288",
        "text": "Ghana"
    },
    {
        "id": "292",
        "text": "Gibraltar"
    },
    {
        "id": "300",
        "text": "Greece"
    },
    {
        "id": "304",
        "text": "Greenland"
    },
    {
        "id": "308",
        "text": "Grenada"
    },
    {
        "id": "312",
        "text": "Guadeloupe"
    },
    {
        "id": "320",
        "text": "Guatemala"
    },
    {
        "id": "324",
        "text": "Guinea"
    },
    {
        "id": "624",
        "text": "Guinea-Bissau"
    },
    {
        "id": "328",
        "text": "Guyana"
    },
    {
        "id": "332",
        "text": "Haiti"
    },
    {
        "id": "336",
        "text": "Holy See (Vatican City State)"
    },
    {
        "id": "340",
        "text": "Honduras"
    },
    {
        "id": "348",
        "text": "Hungary"
    },
    {
        "id": "352",
        "text": "Iceland"
    },
    {
        "id": "699",
        "text": "India"
    },
    {
        "id": "356",
        "text": "India, excl. Sikkim"
    },
    {
        "id": "360",
        "text": "Indonesia"
    },
    {
        "id": "364",
        "text": "Iran"
    },
    {
        "id": "368",
        "text": "Iraq"
    },
    {
        "id": "372",
        "text": "Ireland"
    },
    {
        "id": "376",
        "text": "Israel"
    },
    {
        "id": "381",
        "text": "Italy"
    },
    {
        "id": "388",
        "text": "Jamaica"
    },
    {
        "id": "392",
        "text": "Japan"
    },
    {
        "id": "400",
        "text": "Jordan"
    },
    {
        "id": "398",
        "text": "Kazakhstan"
    },
    {
        "id": "404",
        "text": "Kenya"
    },
    {
        "id": "296",
        "text": "Kiribati"
    },
    {
        "id": "414",
        "text": "Kuwait"
    },
    {
        "id": "417",
        "text": "Kyrgyzstan"
    },
    {
        "id": "418",
        "text": "Lao People's Dem. Rep."
    },
    {
        "id": "428",
        "text": "Latvia"
    },
    {
        "id": "422",
        "text": "Lebanon"
    },
    {
        "id": "426",
        "text": "Lesotho"
    },
    {
        "id": "430",
        "text": "Liberia"
    },
    {
        "id": "434",
        "text": "Libya"
    },
    {
        "id": "440",
        "text": "Lithuania"
    },
    {
        "id": "442",
        "text": "Luxembourg"
    },
    {
        "id": "450",
        "text": "Madagascar"
    },
    {
        "id": "454",
        "text": "Malawi"
    },
    {
        "id": "458",
        "text": "Malaysia"
    },
    {
        "id": "462",
        "text": "Maldives"
    },
    {
        "id": "466",
        "text": "Mali"
    },
    {
        "id": "470",
        "text": "Malta"
    },
    {
        "id": "584",
        "text": "Marshall Isds"
    },
    {
        "id": "474",
        "text": "Martinique"
    },
    {
        "id": "478",
        "text": "Mauritania"
    },
    {
        "id": "480",
        "text": "Mauritius"
    },
    {
        "id": "175",
        "text": "Mayotte"
    },
    {
        "id": "484",
        "text": "Mexico"
    },
    {
        "id": "496",
        "text": "Mongolia"
    },
    {
        "id": "499",
        "text": "Montenegro"
    },
    {
        "id": "500",
        "text": "Montserrat"
    },
    {
        "id": "504",
        "text": "Morocco"
    },
    {
        "id": "508",
        "text": "Mozambique"
    },
    {
        "id": "104",
        "text": "Myanmar"
    },
    {
        "id": "580",
        "text": "N. Mariana Isds"
    },
    {
        "id": "516",
        "text": "Namibia"
    },
    {
        "id": "524",
        "text": "Nepal"
    },
    {
        "id": "530",
        "text": "Neth. Antilles"
    },
    {
        "id": "532",
        "text": "Neth. Antilles and Aruba"
    },
    {
        "id": "528",
        "text": "Netherlands"
    },
    {
        "id": "540",
        "text": "New Caledonia"
    },
    {
        "id": "554",
        "text": "New Zealand"
    },
    {
        "id": "558",
        "text": "Nicaragua"
    },
    {
        "id": "562",
        "text": "Niger"
    },
    {
        "id": "566",
        "text": "Nigeria"
    },
    {
        "id": "579",
        "text": "Norway"
    },
    {
        "id": "512",
        "text": "Oman"
    },
    {
        "id": "490",
        "text": "Other Asia, nes"
    },
    {
        "id": "586",
        "text": "Pakistan"
    },
    {
        "id": "585",
        "text": "Palau"
    },
    {
        "id": "591",
        "text": "Panama"
    },
    {
        "id": "598",
        "text": "Papua New Guinea"
    },
    {
        "id": "600",
        "text": "Paraguay"
    },
    {
        "id": "459",
        "text": "Peninsula Malaysia"
    },
    {
        "id": "604",
        "text": "Peru"
    },
    {
        "id": "608",
        "text": "Philippines"
    },
    {
        "id": "616",
        "text": "Poland"
    },
    {
        "id": "620",
        "text": "Portugal"
    },
    {
        "id": "634",
        "text": "Qatar"
    },
    {
        "id": "410",
        "text": "Rep. of Korea"
    },
    {
        "id": "498",
        "text": "Rep. of Moldova"
    },
    {
        "id": "638",
        "text": "Réunion"
    },
    {
        "id": "642",
        "text": "Romania"
    },
    {
        "id": "643",
        "text": "Russian Federation"
    },
    {
        "id": "646",
        "text": "Rwanda"
    },
    {
        "id": "647",
        "text": "Ryukyu Isd"
    },
    {
        "id": "461",
        "text": "Sabah"
    },
    {
        "id": "654",
        "text": "Saint Helena"
    },
    {
        "id": "659",
        "text": "Saint Kitts and Nevis"
    },
    {
        "id": "658",
        "text": "Saint Kitts, Nevis and Anguilla"
    },
    {
        "id": "662",
        "text": "Saint Lucia"
    },
    {
        "id": "534",
        "text": "Saint Maarten"
    },
    {
        "id": "666",
        "text": "Saint Pierre and Miquelon"
    },
    {
        "id": "670",
        "text": "Saint Vincent and the Grenadines"
    },
    {
        "id": "882",
        "text": "Samoa"
    },
    {
        "id": "674",
        "text": "San Marino"
    },
    {
        "id": "678",
        "text": "Sao Tome and Principe"
    },
    {
        "id": "457",
        "text": "Sarawak"
    },
    {
        "id": "682",
        "text": "Saudi Arabia"
    },
    {
        "id": "686",
        "text": "Senegal"
    },
    {
        "id": "688",
        "text": "Serbia"
    },
    {
        "id": "891",
        "text": "Serbia and Montenegro"
    },
    {
        "id": "690",
        "text": "Seychelles"
    },
    {
        "id": "694",
        "text": "Sierra Leone"
    },
    {
        "id": "702",
        "text": "Singapore"
    },
    {
        "id": "703",
        "text": "Slovakia"
    },
    {
        "id": "705",
        "text": "Slovenia"
    },
    {
        "id": "711",
        "text": "So. African Customs Union"
    },
    {
        "id": "90",
        "text": "Solomon Isds"
    },
    {
        "id": "706",
        "text": "Somalia"
    },
    {
        "id": "710",
        "text": "South Africa"
    },
    {
        "id": "728",
        "text": "South Sudan"
    },
    {
        "id": "724",
        "text": "Spain"
    },
    {
        "id": "144",
        "text": "Sri Lanka"
    },
    {
        "id": "275",
        "text": "State of Palestine"
    },
    {
        "id": "729",
        "text": "Sudan"
    },
    {
        "id": "740",
        "text": "Suriname"
    },
    {
        "id": "748",
        "text": "Swaziland"
    },
    {
        "id": "752",
        "text": "Sweden"
    },
    {
        "id": "757",
        "text": "Switzerland"
    },
    {
        "id": "760",
        "text": "Syria"
    },
    {
        "id": "762",
        "text": "Tajikistan"
    },
    {
        "id": "807",
        "text": "TFYR of Macedonia"
    },
    {
        "id": "764",
        "text": "Thailand"
    },
    {
        "id": "626",
        "text": "Timor-Leste"
    },
    {
        "id": "768",
        "text": "Togo"
    },
    {
        "id": "772",
        "text": "Tokelau"
    },
    {
        "id": "776",
        "text": "Tonga"
    },
    {
        "id": "780",
        "text": "Trinidad and Tobago"
    },
    {
        "id": "788",
        "text": "Tunisia"
    },
    {
        "id": "792",
        "text": "Turkey"
    },
    {
        "id": "795",
        "text": "Turkmenistan"
    },
    {
        "id": "796",
        "text": "Turks and Caicos Isds"
    },
    {
        "id": "798",
        "text": "Tuvalu"
    },
    {
        "id": "800",
        "text": "Uganda"
    },
    {
        "id": "804",
        "text": "Ukraine"
    },
    {
        "id": "784",
        "text": "United Arab Emirates"
    },
    {
        "id": "826",
        "text": "United Kingdom"
    },
    {
        "id": "834",
        "text": "United Rep. of Tanzania"
    },
    {
        "id": "858",
        "text": "Uruguay"
    },
    {
        "id": "850",
        "text": "US Virgin Isds"
    },
    {
        "id": "842",
        "text": "USA"
    },
    {
        "id": "841",
        "text": "USA (before 1981)"
    },
    {
        "id": "860",
        "text": "Uzbekistan"
    },
    {
        "id": "548",
        "text": "Vanuatu"
    },
    {
        "id": "862",
        "text": "Venezuela"
    },
    {
        "id": "704",
        "text": "Viet Nam"
    },
    {
        "id": "876",
        "text": "Wallis and Futuna Isds"
    },
    {
        "id": "887",
        "text": "Yemen"
    },
    {
        "id": "894",
        "text": "Zambia"
    },
    {
        "id": "716",
        "text": "Zimbabwe"
    }
]
