from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paginator_stuff(posts, page_number, post_count):
    '''
       Return the valid post according to page number
    '''
    if post_count== None:
        post_count = 5
    paginator = Paginator(posts, post_count)
    try:
        result_data = paginator.page(page_number)
    except PageNotAnInteger:
        result_data = paginator.page(1)
    except EmptyPage:
        result_data = paginator.page(paginator.num_pages)
    return result_data


def next_url(url, next='next=/'):
    '''
        This function resetting the next url
    '''
    if '?' in url:
        return url+'&'+next
    else:
        return url+'?'+next
