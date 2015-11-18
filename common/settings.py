''' Webpage-specific settings '''


# Webpage config data
__bootstrap = 'http://maxcdn.bootstrapcdn.com/bootstrap/3.3.5'
__googleapi = 'https://ajax.googleapis.com/ajax'
__PAGE_CONFIG_DATA = {
    'page': {
        'site': 'Robit Tracker',
        'title': '',
        'js': {
            'jquery': __googleapi + '/libs/jquery/1.11.3/jquery.min.js',
            'bootstrap': __bootstrap + '/js/bootstrap.min.js'
        },
        'css': {
            'bootstrap': __bootstrap + '/css/bootstrap.min.css'
        }
    },
    'user': None
}


def get_page_config(request, **kwargs):
    ''' Returns site-wide config data. Key-value args are passed in '''
    conf = __PAGE_CONFIG_DATA.copy()
    for key, val in kwargs.iteritems():
        conf['page'][key] = val
    if request.user.is_authenticated():
        conf['user'] = request.user
    return conf
