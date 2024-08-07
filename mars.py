import requests
import gradio as gr


# 定义函数通过NASA的火星漫游车照片API获取指定火星日期和页面的照片
def fetch_mars_rover_photos(api_key, sol=1000, page=1):
    base_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"
    
    params = {
        'api_key': api_key,
        'sol': sol,
        'page': page
    }
    print(params)
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Gradio
def mars_rover_photo_interface(sol,page):
    api_key = "KKDMzTTxJzgLJBkaMqw0ZfMAyTBtLdKUmneFbPD8" # 还没替换（）
    data = fetch_mars_rover_photos(api_key, sol=sol,page=page)
    print(data)
    if data:
        photos = data.get('photos', [])
        photo_urls = [photo['img_src'] for photo in photos]
        print(photo_urls)
        return photo_urls
    else:
        return []

# Define the input components for the Gradio interface
sol_input = gr.Number(label="Martian Sol", value=1000)
page_input = gr.Number(label="Page", value=1)

# Create the Gradio interface
gr.Interface(fn=mars_rover_photo_interface, 
        inputs=[sol_input,  page_input], 
        outputs=gr.Gallery(label="Mars Rover Photos")).launch()