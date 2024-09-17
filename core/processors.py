from .models import About, Linksocial, Category

# ABOUT
def ctx_dic_about(req):
    ctx_about = {}    
    ctx_about['ABOUT'] = About.objects.latest('created')    
    return ctx_about

# CATEGORIES



# LINK SOCIAL
def ctx_dic_linksocial(req):
    ctx_links = {}    
    links = Linksocial.objects.all()
    
    for link in links:
        ctx_links[link.key] = {
            'name': link.name,
            'url': link.url,
            'icon': link.icon
        }

    return {'link_all':ctx_links}