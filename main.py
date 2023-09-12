#mind donating SRAVstudios
#BTC - bc1q5kmqqynratseyh7v0n8q58rn7p5xejuemmc4px

#USDT(ETH) - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

#USDT(SOLANA) - 4MjmiAwiQT1cqb5fSpvdsKCabZAKxopcMsTqem9gWBqB

#USDT(POLYGON) - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

#ETH - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

import requests
import json

url = "https://www.galaxus.de/api/graphql/enter-search"
ts = input('what to search? ')
payload = json.dumps([
  {
    "operationName": "ENTER_SEARCH",
    "variables": {
      "limit": 500,
      "offset": 0,
      "query": ts ,
      "filters": [],
      "sortOrder": None,
      "include": [
        "bra",
        "pt",
        "pr",
        "off"
      ],
      "searchQueryId": "9c8a1e2c-8d86-47ea-b615-4f0b8309a721",
      "ltrEnabled": True,
      "siteId": None
    },
    "query": "query ENTER_SEARCH($query: String!, $sortOrder: ProductSort, $limit: Int = 9, $offset: Int = 0, $filters: [SearchFilter], $include: [String!], $exclude: [String!], $searchQueryId: String, $rewriters: [String!], $ltrEnabled: Boolean, $siteId: String) {\n  search(\n    query: $query\n    filters: $filters\n    searchQueryId: $searchQueryId\n    rewriters: $rewriters\n    ltrEnabled: $ltrEnabled\n    siteId: $siteId\n  ) {\n    products(limit: $limit, offset: $offset, sortOrder: $sortOrder) {\n      total\n      hasMore\n      nextOffset\n      results {\n        ...ProductSearchResult\n        __typename\n      }\n      __typename\n    }\n    filters(include: $include, exclude: $exclude) {\n      product {\n        identifier\n        name\n        filterType\n        score\n        tooltip {\n          ...FilterTooltipResult\n          __typename\n        }\n        ...CheckboxSearchFilterResult\n        ...RangeSearchFilterResult\n        __typename\n      }\n      quickFilter {\n        options {\n          filterType\n          filterIdentifier\n          filterName\n          filterOptionIdentifier\n          filterOptionName\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    magazinePages(limit: 3) {\n      ids {\n        id\n        score\n        __typename\n      }\n      __typename\n    }\n    discussions(limit: 3) {\n      ids {\n        id\n        score\n        __typename\n      }\n      __typename\n    }\n    questions(limit: 3) {\n      ids {\n        id\n        score\n        __typename\n      }\n      __typename\n    }\n    ratings(limit: 3) {\n      ids {\n        id\n        score\n        __typename\n      }\n      total\n      __typename\n    }\n    productTypes(limit: 24) {\n      total\n      results {\n        id\n        name\n        primarySynonyms\n        isVisible\n        description\n        metaDescription\n        imageUrl\n        searchScore\n        __typename\n      }\n      __typename\n    }\n    brands(limit: 24) {\n      total\n      results {\n        id\n        title\n        searchScore\n        __typename\n      }\n      __typename\n    }\n    _meta {\n      queryInfo {\n        correctedQuery\n        didYouMeanQuery\n        lastProductSearchPass\n        executedSearchTerm\n        testGroup\n        isManagedQuery\n        isRerankedQuery\n        __typename\n      }\n      redirectionUrl\n      portalReferral {\n        productCount\n        portalName\n        url\n        productImageUrls\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment ProductSearchResult on ProductSearchResultItem {\n  searchScore\n  mandatorSpecificData {\n    ...ProductMandatorSpecific\n    __typename\n  }\n  product {\n    ...ProductMandatorIndependent\n    __typename\n  }\n  offer {\n    ...ProductOffer\n    __typename\n  }\n  __typename\n}\n\nfragment FilterTooltipResult on FilterTooltip {\n  text\n  moreInformationLink\n  __typename\n}\n\nfragment CheckboxSearchFilterResult on CheckboxSearchFilter {\n  options {\n    identifier\n    name\n    productCount\n    score\n    referenceValue {\n      value\n      unit {\n        abbreviation\n        __typename\n      }\n      __typename\n    }\n    preferredValue {\n      value\n      unit {\n        abbreviation\n        __typename\n      }\n      __typename\n    }\n    tooltip {\n      ...FilterTooltipResult\n      __typename\n    }\n    __typename\n  }\n  __typename\n}\n\nfragment RangeSearchFilterResult on RangeSearchFilter {\n  referenceMin\n  preferredMin\n  referenceMax\n  preferredMax\n  referenceStepSize\n  preferredStepSize\n  rangeMergeInfo {\n    isBottomMerged\n    isTopMerged\n    __typename\n  }\n  referenceUnit {\n    abbreviation\n    __typename\n  }\n  preferredUnit {\n    abbreviation\n    __typename\n  }\n  rangeFilterDataPoint {\n    ...RangeFilterDataPointResult\n    __typename\n  }\n  __typename\n}\n\nfragment ProductMandatorSpecific on MandatorSpecificData {\n  isBestseller\n  isDeleted\n  showroomSites\n  sectorIds\n  hasVariants\n  __typename\n}\n\nfragment ProductMandatorIndependent on ProductV2 {\n  id\n  productId\n  name\n  nameProperties\n  productTypeId\n  productTypeName\n  brandId\n  brandName\n  averageRating\n  totalRatings\n  totalQuestions\n  isProductSet\n  images {\n    url\n    height\n    width\n    __typename\n  }\n  energyEfficiency {\n    energyEfficiencyColorType\n    energyEfficiencyLabelText\n    energyEfficiencyLabelSigns\n    energyEfficiencyImage {\n      url\n      height\n      width\n      __typename\n    }\n    __typename\n  }\n  seo {\n    seoProductTypeName\n    seoNameProperties\n    productGroups {\n      productGroup1\n      productGroup2\n      productGroup3\n      productGroup4\n      __typename\n    }\n    gtin\n    __typename\n  }\n  smallDimensions\n  basePrice {\n    priceFactor\n    value\n    __typename\n  }\n  productDataSheet {\n    name\n    languages\n    url\n    size\n    __typename\n  }\n  __typename\n}\n\nfragment ProductOffer on OfferV2 {\n  id\n  productId\n  offerId\n  shopOfferId\n  price {\n    amountInclusive\n    amountExclusive\n    currency\n    __typename\n  }\n  deliveryOptions {\n    mail {\n      classification\n      futureReleaseDate\n      __typename\n    }\n    pickup {\n      siteId\n      classification\n      futureReleaseDate\n      __typename\n    }\n    detailsProvider {\n      productId\n      offerId\n      quantity\n      type\n      __typename\n    }\n    __typename\n  }\n  label\n  labelType\n  type\n  volumeDiscountPrices {\n    minAmount\n    price {\n      amountInclusive\n      amountExclusive\n      currency\n      __typename\n    }\n    isDefault\n    __typename\n  }\n  salesInformation {\n    numberOfItems\n    numberOfItemsSold\n    isEndingSoon\n    validFrom\n    __typename\n  }\n  incentiveText\n  isIncentiveCashback\n  isNew\n  isSalesPromotion\n  hideInProductDiscovery\n  canAddToBasket\n  hidePrice\n  insteadOfPrice {\n    type\n    price {\n      amountInclusive\n      amountExclusive\n      currency\n      __typename\n    }\n    __typename\n  }\n  minOrderQuantity\n  __typename\n}\n\nfragment RangeFilterDataPointResult on RangeFilterDataPoint {\n  count\n  referenceValue {\n    value\n    unit {\n      abbreviation\n      __typename\n    }\n    __typename\n  }\n  preferredValue {\n    value\n    unit {\n      abbreviation\n      __typename\n    }\n    __typename\n  }\n  __typename\n}"
  }
])
headers = {
  'authority': 'www.galaxus.de',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9',
  'content-type': 'application/json',
  'cookie': '.bid=eacdea55-f5a4-4f16-afd2-94dd4b7bddc5; .xpid=d187a114; _gcl_au=1.1.531242129.1692881176; _gat_UA-34235288-14=1; .consent=pe1-ma1-fu1; .cid=95c5f41f-2531-45d8-a991-9bbbafa2b5d7; _fbp=fb.1.1692881177067.1948134969; _pin_unauth=dWlkPU0yWmhPVFkzTlRRdE9HRTVOQzAwTkRKa0xUa3dZVFl0WkdOa1lqZzFPV1l5TkdJMQ; sp=996e50f7-1469-4069-855a-1ac4c14e0d07; _biAN=55836; _biBI=no0b2a18-a856-4142-9e92-79ba294bd3cf; TRADEDOUBLER=3188c26d40785a4ed1287b4bcee9c4d1; _derived_epik=dj0yJnU9d29RaHRDOTJnczlITXhHSDBjb01ZMGxzRnFlR0tEZXYmbj1MVjdfTWI3Rl9IcGR4MExOb2lRM19RJm09MSZ0PUFBQUFBR1RuVWVFJnJtPTEmcnQ9QUFBQUFHVG5VZUUmc3A9Mg; _abck=AC691D88844EC2F0ABCF0F9A4273F8C4~-1~YAAQX13SFxMpUiyKAQAAn0phQQpnKszuUGBr0yVnwK/kg6lHoQJ7Q0PPygk6j6NK8jS0SFmnyfVwT67/eAjX0SGR37D1H5nzmHkDgh8V1Jq93l5IO0uvxeJJaHv4q+aiSPybvCKaYbhkeMI0i0O46jDRFrvWQw2Pq3jNQOzXbndyOcHh6d85k1tvGKUXCMsA8r+EUEtj8xRCXZFiendd5T6PtS5pnxBDwkVnyrZhcqUaxsnSzbVQ5P2VvDBamXBbtGZzZtEUX5OTHxtG2HDJoH58aQWoVSdpzCiRiMemeONz1uJtBRRQDO8CqpcjLdbOnJaRmNVM7hCbIxr0FkEWgK42PI96+exCQMuvqOhd7oDKw2OBq9FTy0SPk+nd8mWb+2nxMtU4/mix3g==~-1~-1~1692884660; bm_sz=456F6D10BE63BE92F81AD6690BCDB21E~YAAQX13SFxYpUiyKAQAAn0phQRRJX765T+qZs9+NI+GcNKxl+knuNN4c88xf6LwUgpWjbhA+FcuoCQNtbsa7OOuSImitzmth0GoBG9OzkxRUJS6WlR33KwtNMCV+c1+7ADKhXeSob/ECmIcXVoAAh8vM+OSHaLCpkyHIZQgtwtHATB41qc/9uiVSoDGkYPOLQ17SoqbMEXSGWqEQISQGfP+wibdMFOpvPrA4TY4CufTes89K+lj/IsO7W277nASnid5VGS+76l9UHeXFbPl9FYwwIOTOw6UudRpzpCBZl4VUDOA=~3487302~4600386; .ub.ses.579b=*; .sid=b10255d1-b55b-4221-bbc3-2f4d5d6bdf4e; _ga=GA1.2.343738843.1693314012; _gid=GA1.2.1025615910.1693314012; RedirectCountry=off; ak_bmsc=C693B156968C171BBBC9A9AFC7833951~000000000000000000000000000000~YAAQX13SF8UpUiyKAQAATXhhQRRzqYFRKgn+nCy1gX0iP5MzTc7BzxUlyj6WqM7r+sMiz5hI8G1hmFnfU+MkGw8yQ1f5sKzx96ayxZ6bY8sT45MHuWiOgtlVAxv/RMQdlgpF3E8Cvy2+xvV6/kYuvghFB7Nn6nVd6ATEq2BDg81sDFrY/qsozRGJJoBBc6KnVVT1xl/9yG4W7czuFYFuucP8rjN7XVBd1Wqp83m80BRflOEsd6KlvbSSPRh/APjMdRKJ/3ti3YgqqU0/62e3DGL44sG7oPueghwSXtsMqJSewfl8U5wJXeRdZpNlbhFSDyDLGX+I+5AzCg9oCP5JM7OtPW4XYyH2Rpd14lZNlrwRD7pFZDXJDI6o4LqiEcONp4gNW2BehqH0Nb3A0rVbSn2Es5ZLLIHk; bm_mi=8F3A76301A917567436A02DB3DEBF6E8~YAAQX13SFyCJUiyKAQAAn7h5QRSxwecXXHCs7Yp3g1fz3T+dFoOk0a3okSKZ/8Iv7JPz7uleWRnLQu9Yy2brhhaV93OQAa1z3sfcYxLWtzastjqIuoTu2jxtCQCNOszBtwJ2DwqrsSa8kDUxhwaDf2H28DeRJnsk7TYjrrW3ULHgpZo3weBAvFzoghYhS1hJXd34yV3lRFBnAV26kSm4QVhtEFcvAzsWNxZPZvXwo9pWIIo8XEO1qdW+PMgeVLSMRVlDd5kBboZt9Wx7iEJLhJd8/RZZMi9f2qmVEykleOFb2UUu6fy9QPruX2gCAQ==~1; .sidexp=1693322812; .bidexp=2008934812; _uetsid=fe06f3c0466b11eea5d4db8b65bc5e2f; _uetvid=37ae6af0427c11eeb98297238fbc3d04; outbrain_cid_fetch=true; .ub.id.579b=c340c590-f3b1-4572-b051-14d03a01ec19.1692881176.4.1693315619.1693202720.ce2412a4-d828-4eb4-9cd6-78101657be33.9d05cc9d-faf8-4c12-8f67-70591f39833c.41667666-4b3e-41e2-9978-e6f48e435222.1693314010695.26; bm_sv=5434820809945EDF9DA074526808B86B~YAAQX13SF3SJUiyKAQAAOtt5QRTX4SUeN8bZ4zYLlUbr9ICCVvdu81PwWFw1bNPib+DjiwQ2TbZFP/B+VPtz3Qmrr/o3pX8Pkpt54e4jj25HfNklIhjwmxw5gFWCUymVP+9y/u3LRXFzMRIE/gNnld8hrbLNmuo3ou0g+hKy9coxuGKmTYNJcwtT0hvGrF4h9X1ZjZE+VzJ6SX9DdFFPoK8NxLGJ+OjgTOnP4lyx8NmnbeQAbTEhyrRG1HXTHclhUQ==~1; _dd_s=logs=0&expire=1693316519099; bm_sv=5434820809945EDF9DA074526808B86B~YAAQX13SF1SRUiyKAQAA8Nt7QRRW2R7IzdSHv1/HgaN8g713gp7xshImm/GWHfA4U2rEY7jZ4v3n+7sQ58NDWQwyixcFhyojShI4d2KVwWK9uFr6ChkQUtFb5BWyaODMDJH+1AmePW95vltVS0Rf0IkvEjjhJHmtvYd+1Peg/k9lVV+/PnN3NwW3eXP5CfZjhYjcfmArlq+yfb+id+aUoYHRn4JSc2ofSpXfbz3jnEISG2aEHFo1XxolQXwfcz4aZw==~1',
  'origin': 'https://www.galaxus.de',
  'referer': 'https://www.galaxus.de/de/search?q=sugar',
  'sec-ch-ua': '"Chromium";v="116", "Not)A;Brand";v="24", "Microsoft Edge";v="116"',
  'sec-ch-ua-arch': '"x86"',
  'sec-ch-ua-bitness': '"64"',
  'sec-ch-ua-full-version': '"116.0.1938.62"',
  'sec-ch-ua-full-version-list': '"Chromium";v="116.0.5845.111", "Not)A;Brand";v="24.0.0.0", "Microsoft Edge";v="116.0.1938.62"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-model': '""',
  'sec-ch-ua-platform': '"Windows"',
  'sec-ch-ua-platform-version': '"10.0.0"',
  'sec-ch-ua-wow64': '?0',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.62',
  'x-dg-correlation-id': 'f3f17b90-35ee-4564-9f82-f751578f47b2',
  'x-dg-language': 'de-CH',
  'x-dg-portal': '27',
  'x-dg-routename': '/search',
  'x-dg-scrumteam': 'Endeavour',
  'x-dg-testgroup': 'Default'
}

response = requests.request("POST", url, headers=headers, data=payload)

data = json.loads(response.text)
count = 0
productcount = len(data[0]['data']['search']['products']['results'])
print(productcount)
while count < productcount:
    productname = data[0]['data']['search']['products']['results'][count]['product']['name']
    ean = data[0]['data']['search']['products']['results'][count]['product']['seo']['gtin']
    rating = data[0]['data']['search']['products']['results'][count]['product']['averageRating']
    price = data[0]['data']['search']['products']['results'][count]['offer']['price']['amountInclusive']
    delivery = data[0]['data']['search']['products']['results'][count]['offer']['deliveryOptions']['mail']['classification']
    manufacturer = data[0]['data']['search']['products']['results'][count]['product']['brandName']
    print(count+1)
    print(productname)
    print(ean)
    print(rating)
    print(price)
    print(delivery)
    print(manufacturer)
    print('')
    count += 1
#mind donating SRAVstudios
#BTC - bc1q5kmqqynratseyh7v0n8q58rn7p5xejuemmc4px

#USDT(ETH) - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

#USDT(SOLANA) - 4MjmiAwiQT1cqb5fSpvdsKCabZAKxopcMsTqem9gWBqB

#USDT(POLYGON) - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572

#ETH - 0x8558288490E11E7F900471E7D52F0b0A0B6b8572
