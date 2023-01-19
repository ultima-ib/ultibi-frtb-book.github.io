import ultibi as ul
import json

ds = ul.FRTBDataSet.from_config_path("datasource_config.toml")
ds.prepare()
added_rows = dict(
    prepare=True,
    rows=[
        {
            "SensitivitySpot": "1000000",
            "PnL_Up": "0",
            "PnL_Down": "0",
            "COB": "",
            "MaturityDate": "",
            "RiskClass": "Commodity",
            "RiskFactor": "XAU",
            "RiskCategory": "Delta",
            "RiskFactorType": "",
            "BucketBCBS": "7",
            "BucketCRR2": "7",
            "CreditQuality": "",
            "CoveredBondReducedWeight": "",
            "Group": "Ultima",
        }
    ],
)

added_rows_json = json.dumps(added_rows)

request1 = dict(
    measures=[
        ["Commodity DeltaCharge Low", "scalar"],
        ["Commodity DeltaCharge Medium", "scalar"],
        ["Commodity DeltaCharge High", "scalar"],
    ],
    add_row=added_rows,
    groupby=["Group"],
    hide_zeros=True,
)

result1 = ds.execute(request1)

# print(result1) #<-- uncomment to see

request2 = dict(
    measures=[
        ["Commodity DeltaCharge Low", "scalar"],
        ["Commodity DeltaCharge Medium", "scalar"],
        ["Commodity DeltaCharge High", "scalar"],
    ],
    groupby=["Group"],
    hide_zeros=True,
)

result2 = ds.execute(request2)
