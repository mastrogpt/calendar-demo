
#--web true
#--param GOOGLE_CLIENT_ID $GOOGLE_CLIENT_ID
#--param NUVDEV_HOST $NUVDEV_HOST

def main(args):

    client_id = args.get("GOOGLE_CLIENT_ID")
    redirect_uri = args.get("NUVDEV_HOST")
    
    return {
        'body': {
            'client_id': client_id,
            'redirect_uri': redirect_uri
        }
    }
        
    