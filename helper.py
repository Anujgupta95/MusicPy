from datetime import datetime, time

def str_to_date_obj(release_date):
    release_date_obj = datetime.strptime(release_date, '%Y-%m-%d').date()
    return release_date_obj

if __name__=='__main__':
    str_to_date_obj()