import requests

print("--- 1. GET REQUEST (Data Mangwana) ---")
# Man le tujhe kisi user ki profile details chahiye
get_url = "https://reqres.in/api/users/2"

get_response = requests.get(get_url)

if get_response.status_code == 200:
    user_data = get_response.json()
    print(f"GET Success: User ka naam '{user_data['data']['first_name']}' hai.")
else:
    print("GET Fail!")


print("\n--- 2. POST REQUEST (Data Bhejna) ---")
# Man le tu kisi naye user ko apne database/server par create/register kar raha hai
post_url = "https://reqres.in/api/users"

# POST mein humesha ek "Payload" (Data ka dabba) bhejna padta hai
naya_data = {
    "name": "Haydan",
    "job": "Backend Developer"
}

# Yahan hum .post() use kar rahe hain, aur apna 'naya_data' usko de rahe hain
post_response = requests.post(post_url, data=naya_data)

# POST ka success code aksar 201 (Created) hota hai
if post_response.status_code == 201:
    result = post_response.json()
    print(f"POST Success: Server ne bola -> Welcome {result['name']}, tumhari job '{result['job']}' register ho gayi!")
    print(f"Server Time (ID): {result['id']}")
else:
    print("POST Fail!")