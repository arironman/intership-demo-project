// getching the get stuff for next url
var search = window.location.search.split('?');
var get_data = '';
if (search.length > 1) {
    if (search[1].includes('page')) {
        get_data = '?' + search;
    }
}

// next url 
var next = window.location.pathname + get_data;

