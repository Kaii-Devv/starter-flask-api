import requests

url = "https://analytics-gateway.delta.dp.lightricks.com/record_batch"
headers = {
    "ltx-dp-batch-id": "01HRRBFW7E0WXZ85VMHJ9SPHMG",
    "ltx-dp-batch-timestamp": "1710214344942",
    "content-type": "avro/binary; schema_id=103055",
    "content-length": "640",
    "accept-encoding": "gzip",
    "user-agent": "okhttp/4.10.0"
}
data = b"\x02\xef\xbf\xbd\x0cHdf1173ee-33be-47bb-a2c7-b9fcafd0a919\xef\xbf\xbd\xe8\x8b\x8b\xef\xbf\xbdc\x0eandroid\x12videoleap\xef\xbf\xbd\x08\x02\nvideo\x00\x02\x08clip\x00\x02\xef\xbf\xbd\x01{\"control_net_feature\":\"ai-video-gaming\",\"prompt_text\":\"snow, morning\",\"preset\":\"gaming001\"}Hcb20b12f-62ed-47f0-a2bc-295f3b0176a8\"ai_prompt_entered\x02\x12cancelled\x000com.lightricks.videoleap\"videoleap_android\x082144Hf4c79ceb-5aaf-474e-87b6-0ee64770b3f2\xef\xbf\xbd\xe8\x8b\x8b\xef\xbf\xbdc\x02Hd306eda0-dc4b-4ade-9aae-6e6ae1b4aac9Hdf1173ee-33be-47bb-a2c7-b9fcafd0a919\x02401HRPN379Y4C4A0PDN25YJ72TS\x08\x00\x00\x00\x00\x00\x00\x60d@401HRPN379Y4C4A0PDN25YJ72TS\x00\x02(8Zi_fcbohlWO1-nSPe8p\x02Hb772e4f1-3847-4793-81ae-a50f9f496ed7\x0eandroid\x02 c596b93ca298e0ac\x00\x00Hdbb11f57-716a-41cc-8c26-732e47f2209f\x04H98e34fe6-c2e5-401c-8dfb-e4921de1edf7\x00\x00"

response = requests.post(url, headers=headers, data=data)

# print the response status code
print(response.status_code)

# print the response content
print(response.content)
