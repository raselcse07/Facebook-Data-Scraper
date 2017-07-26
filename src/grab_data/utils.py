import facebook



def grab_data_from_facebook(token,types_of_data,data_fields,number_of_data):

    graph = facebook.GraphAPI(access_token=token, version = 2.7)
    user="me"
    profile = graph.get_object(id=user, fields=types_of_data)
    posts = graph.get_connections(id=user, connection_name='posts', fields=data_fields,limit=number_of_data)
    desired_posts=posts["data"]

    return desired_posts
