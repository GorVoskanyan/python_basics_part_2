# ALL KEYS IN ONE LIST
# ALL VALUES IN ONE LIST
# CHANGE DATA -> ETH -> TOTAL_DIFF 100

# DATA -> TOKENS -> FIRST TOKEN INFO -> NAME = DOGE

# DATA -> ETH -> TOTAL_OUT += DATA -> TOKENS -> TOTAL OUT


data = {
    "address": "0x544444444444",
    "ETH": {"balance": 444, "totalIn": 444, "totalOut": 4},
    "count_txs": 2,
    "tokens": [
        {
            "fst_token_info": {
                "address": "0x44444",
                "name": "fdf",
                "decimals": 0,
                "symbol": "dsfdsf",
                "total_supply": "3228562189",
                "owner": "0x44444",
                "last_updated": 1519022607901,
                "issuances_count": 0,
                "holders_count": 137528,
                "price": False,
            },
            "balance": 5000,
            "totalIn": 0,
            "total_out": 1,
        },
        {
            "sec_token_info": {
                "address": "0x44444",
                "name": "ggg",
                "decimals": "2",
                "symbol": "fff",
                "total_supply": "250000000000",
                "owner": "0x44444",
                "last_updated": 1520452201,
                "issuances_count": 0,
                "holders_count": 20707,
                "price": False,
            },
            "balance": 500,
            "totalIn": 0,
            "total_out": 1,
        },
    ],
}


data['tokens'][0]['fst_token_info']['owner'] = 'Jiro'
data['tokens'][1]['sec_token_info']['holders_count'] = '50000'
print(data)









