import googlemaps


def get_location(address: str, google_maps_api_key: str):
    '''住所から緯度経度情報，正規化された住所を取得する

    Args:
        address (str): 住所
        google_maps_api_key (str): google mapsのapikey

    '''
    gmaps = googlemaps.Client(key=google_maps_api_key)
    result = gmaps.geocode(address, language='ja')
    location = result[0]['geometry']['location']
    formatted_address = result[0]['formatted_address']
    location.update(
        {'formatted_address': formatted_address}
    )
    return location


if __name__ == '__main__':
    import os
    google_maps_api_key = os.environ['GOOGLE_MAPS_API_KEY']
    address = u'東京千代田区丸の内1-11-1'
    location = get_location(address, google_maps_api_key)
    print(location)
