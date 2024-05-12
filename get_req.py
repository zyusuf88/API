import requests
# https://postcodes.io/

postcodes_req = requests.get("https://api.postcodes.io/postcodes/se120nb")
# print(postcodes_req)
#
# print(type(postcodes_req.status_code))
# print(postcodes_req.headers)
#
# print(postcodes_req.content)
#
# print(postcodes_req.json()) # convert from bytes to json
# print(type(postcodes_req.json())) # now dict

# Get the region of just the postcode

data_dict = postcodes_req.json()["result"]
print(data_dict["region"])  # output London

print(f"This is Player 1:", float(player_one["height"]) * 10, cm);

