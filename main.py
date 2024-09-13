from instagram_private_api import Client, ClientCompatPatch, ClientError

if __name__ == '__main__':
    # Авторизуйтесь в Instagram через неофициальный API
    username = 'nictol18'
    password = 'n15e81912NET18'

    device_id = 'android-1234567890abcdef'

    api = Client(username, password, device_id=device_id)

    # Получите ID пользователя через имя профиля
    user_info = api.username_info('slvesta')
    user_id = user_info['user']['pk']

    # Получите активные сторис
    stories = api.user_story_feed(user_id)

    # Вывод информации о сторис
    for story in stories['reel']['items']:
        print(f"Story ID: {story['id']}")
        print(f"Story media type: {story['media_type']}")
        if 'image_versions2' in story:
            print(f"Image URL: {story['image_versions2']['candidates'][0]['url']}")
        if 'video_versions' in story:
            print(f"Video URL: {story['video_versions'][0]['url']}")