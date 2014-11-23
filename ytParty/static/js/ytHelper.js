/**
 * Created by leonid <> on 23.11.14.
 */
$.youtubeAppend = function(token, destinaton_id) {
    resp = $.ajax({
        type: "GET",
        url: 'http://gdata.youtube.com/feeds/api/videos/' + token + '?v=2&alt=jsonc',
        async: false
    }).responseText;
    resp = JSON.parse(resp);
    $('#' + destinaton_id).append('<div class="youtube">\
                 <img src="' + resp.data.thumbnail.sqDefault + '" alt="" />\
                 <h3><a href="javascript:void(0)" onclick="$.youtubePlay(\'' + resp.data.id + '\')">' + resp.data.title + '</a></h3>\
                 </div>');
};
