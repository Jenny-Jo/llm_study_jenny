import pandas as pd
from tqdm.auto import tqdm
import time

from common.utils import mkdir
from common.youtube import get_video_urls, get_youtube_video_info

def main(lst_dic:list[dict]):
  for dic_data in tqdm(lst_dic, desc="downloading.."):
    save_path = mkdir()

    urls = [dic_data['url']]
    urls.extend(
      get_video_urls(dic_data['url'])
    )

    lst_info = []
    for url in urls:
      try:
        video_info = get_youtube_video_info(url)
        lst_info.append(video_info)
      except:
        pass
      time.sleep(0.005)

    df = pd.DataFrame(lst_info)
    file_name = save_path+dic_data['playlist_title']+".csv"
    df.to_csv(file_name, header=True, index=False)


