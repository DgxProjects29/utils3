import datetime
import dateutil.parser

def utc_to_local(utc_dt):
    return utc_dt.replace(tzinfo=datetime.timezone.utc).astimezone(tz=None)

def filter_by_extension(ext):
    def filter(file):
        return file['fileExtension'] == ext
    return filter

def filter_by_tags(user_tags, reverse = False):
    # If all tags in user_tags appear in file_tags, return True
    def filter(file):
        file_title = file['title'].replace('.' + file['fileExtension'], '')
        file_tags = set(file_title.split('-')[1:])
        if reverse:
            return bool(user_tags.difference(file_tags))
        else:
            return not bool(user_tags.difference(file_tags))
        
    return filter


def filter_by_date(from_date, to_date):

    def filter(file):

        created_date_utc = dateutil.parser.parse(file['createdDate'])
        created_date = utc_to_local(created_date_utc).date()
        
        # if date is not given, just return true
        is_date_greater = not bool(from_date) or created_date >= from_date
        is_date_lesser = not bool(to_date) or created_date <= to_date
        
        return is_date_greater and is_date_lesser

    return filter