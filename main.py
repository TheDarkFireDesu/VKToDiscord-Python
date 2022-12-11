import time

import pypresence
import vk_api

from log import logout
from settings import init_setting, select_language

def run():
    try:
        settings = init_setting()
        language = select_language(settings['language'])
        
        presence = pypresence.Presence(settings['app_id'])
        presence.connect()
        
        vk_session = vk_api.VkApi(token=settings['app_token'])
        vk = vk_session.get_api()
        
        time.sleep(5)
        
        while True:
            
            large_image = "vk"
            activity = {
                "large_image": large_image
            }
            res = vk.users.get(user_ids=settings['id'], fields="status")[0]

            if "status_audio" not in res:
                state = language['state']
                
                if "details" in activity:
                    activity.pop("details")

                large_image = 'vk'
                activity.update({'state': state, 'large_image': large_image})
            
            else:
                curr_music = res['status_audio']

                state = f"{language['artist']} - {curr_music['artist']}"
                details = f"{language['title']} - {curr_music['title']}"
                logout(curr_music['artist'] + ' - ' + curr_music['title'], 1) # LOGGING
                
                if 'album' in curr_music and 'thumb' in curr_music['album']:
                    large_image = curr_music["album"]["thumb"]["photo_300"]

                activity.update(
                    {'state': state, 'details': details,
                     'large_image': large_image})

            presence.update(**activity)
            time.sleep(15)
    except OSError:
        logout(0, 2) # LOGGING
        run()

if __name__ == "__main__":
    run()