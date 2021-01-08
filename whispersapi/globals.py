from django.conf import settings
from whispersapi.models import Configuration
from whispersapi.immediate_tasks import send_missing_configuration_value_email, send_wrong_type_configuration_value_email


LIST_DELIMITER = ','
PK_REQUESTS = ['retrieve', 'update', 'partial_update', 'destroy']
COMMENT_CONTENT_TYPES = ['event', 'eventgroup', 'eventlocation', 'servicerequest']

whispers_admin_user_record = Configuration.objects.filter(name='whispers_admin_user').first()
if whispers_admin_user_record:
    if whispers_admin_user_record.value.isdecimal():
        WHISPERS_ADMIN_USER_ID = int(whispers_admin_user_record.value)
    else:
        WHISPERS_ADMIN_USER_ID = settings.WHISPERS_ADMIN_USER_ID
        encountered_type = type(whispers_admin_user_record.value).__name__
        send_wrong_type_configuration_value_email('whispers_admin_user', encountered_type, 'int')
else:
    WHISPERS_ADMIN_USER_ID = settings.WHISPERS_ADMIN_USER_ID
    send_missing_configuration_value_email('whispers_admin_user')

whispers_email_address = Configuration.objects.filter(name='whispers_email_address').first()
if whispers_email_address:
    if whispers_email_address.value.count('@') == 1:
        EMAIL_WHISPERS = whispers_email_address.value
    else:
        EMAIL_WHISPERS = settings.EMAIL_WHISPERS
        encountered_type = type(whispers_email_address.value).__name__
        send_wrong_type_configuration_value_email('whispers_email_address', encountered_type, 'email_address')
else:
    EMAIL_WHISPERS = settings.EMAIL_WHISPERS
    send_missing_configuration_value_email('whispers_email_address')

email_boilerplate_record = Configuration.objects.filter(name='email_boilerplate').first()
if email_boilerplate_record:
    EMAIL_BOILERPLATE = email_boilerplate_record.value
else:
    EMAIL_BOILERPLATE = settings.EMAIL_BOILERPLATE
    send_missing_configuration_value_email('email_boilerplate')

geonames_username_record = Configuration.objects.filter(name='geonames_username').first()
if geonames_username_record:
    GEONAMES_USERNAME = geonames_username_record.value
else:
    GEONAMES_USERNAME = settings.GEONAMES_USERNAME
    send_missing_configuration_value_email('geonames_username')

geonames_api_url_record = Configuration.objects.filter(name='geonames_api_url').first()
if geonames_api_url_record:
    GEONAMES_API = geonames_api_url_record.value
else:
    GEONAMES_API = settings.GEONAMES_API
    send_missing_configuration_value_email('geonames_api_url')

flyways_api_url_record = Configuration.objects.filter(name='flyways_api_url').first()
if flyways_api_url_record:
    FLYWAYS_API = flyways_api_url_record.value
else:
    FLYWAYS_API = settings.FLYWAYS_API
    send_missing_configuration_value_email('flyways_api_url')

nwhc_org_record = Configuration.objects.filter(name='nwhc_organization').first()
if nwhc_org_record:
    if nwhc_org_record.value.isdecimal():
        NWHC_ORG_ID = int(nwhc_org_record.value)
    else:
        NWHC_ORG_ID = settings.NWHC_ORG_ID
        encountered_type = type(nwhc_org_record.value).__name__
        send_wrong_type_configuration_value_email('nwhc_organization', encountered_type, 'int')
else:
    NWHC_ORG_ID = settings.NWHC_ORG_ID
    send_missing_configuration_value_email('nwhc_organization')

hfs_locations_record = Configuration.objects.filter(name='hfs_locations').first()
if hfs_locations_record:
    hfs_locations_str = hfs_locations_record.value.split(',')
    if all(x.strip().isdecimal() for x in hfs_locations_str):
        HFS_LOCATIONS = [int(hfs_loc) for hfs_loc in hfs_locations_str]
    else:
        encountered_types = ''.join(list(set([type(x).__name__ for x in hfs_locations_str])))
        send_wrong_type_configuration_value_email('hfs_locations', encountered_types, 'int')
else:
    HFS_LOCATIONS = settings.HFS_LOCATIONS
    send_missing_configuration_value_email('hfs_locations')

hfs_epi_user_id_record = Configuration.objects.filter(name='hfs_epi_user').first()
if hfs_epi_user_id_record:
    if hfs_epi_user_id_record.value.isdecimal():
        HFS_EPI_USER_ID = hfs_epi_user_id_record.value
    else:
        HFS_EPI_USER_ID = settings.WHISPERS_ADMIN_USER_ID
        encountered_type = type(hfs_epi_user_id_record.value).__name__
        send_wrong_type_configuration_value_email('hfs_epi_user', encountered_type, 'int')
else:
    HFS_EPI_USER_ID = settings.WHISPERS_ADMIN_USER_ID
    send_missing_configuration_value_email('hfs_epi_user')

madison_epi_user_id_record = Configuration.objects.filter(name='madison_epi_user').first()
if madison_epi_user_id_record:
    if madison_epi_user_id_record.value.isdecimal():
        MADISON_EPI_USER_ID = madison_epi_user_id_record.value
    else:
        MADISON_EPI_USER_ID = settings.WHISPERS_ADMIN_USER_ID
        encountered_type = type(madison_epi_user_id_record.value).__name__
        send_wrong_type_configuration_value_email('madison_epi_user', encountered_type, 'int')
else:
    MADISON_EPI_USER_ID = settings.WHISPERS_ADMIN_USER_ID
    send_missing_configuration_value_email('madison_epi_user')

stale_event_periods_record = Configuration.objects.filter(name='stale_event_periods').first()
if stale_event_periods_record:
    STALE_EVENT_PERIODS = stale_event_periods_record.value
else:
    STALE_EVENT_PERIODS = settings.STALE_EVENT_PERIODS
    message = "Default periods were used (" + ', '.join([str(x) for x in STALE_EVENT_PERIODS]) + ")."
    send_missing_configuration_value_email('stale_event_periods', message=message)
stale_event_periods_list = STALE_EVENT_PERIODS.split(',')
if all(x.strip().isdecimal() for x in stale_event_periods_list):
    stale_event_periods_list_ints = [int(x) for x in stale_event_periods_list]
else:
    encountered_types = ''.join(list(set([type(x).__name__ for x in stale_event_periods_list])))
    send_wrong_type_configuration_value_email('stale_event_periods', encountered_types, 'int',
                                              "No notifications were created.")
