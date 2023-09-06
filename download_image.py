from bing_image_downloader import downloader

keywords = ["building workers"]

for kw in keywords:
    downloader.download(query=kw, limit=30, output_dir="dataset")
