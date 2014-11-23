/**
 * Created by leonid <> on 23.11.14.
 */
$("#youtube").autocomplete({
    source: function(request, response) {
        var apiKey = 'AIzaSyA2KQaiWRK_l_t1asGzg6rvv0gKpM6DdFA';
        var query = request.term;
        $.ajax({
            url: "http://suggestqueries.google.com/complete/search?hl=en&ds=yt&client=youtube&hjson=t&cp=1&q=" + query + "&key=" + apiKey + "&format=5&alt=json&callback=?",
            dataType: 'jsonp',
            success: function(data, textStatus, request) {
                response($.map({}, function(item) {
                    return {
                        label: item[0],
                        value: item[0]
                    }
                }));
                $.youtubeAPI(data[1][0][0]);
            }
        });
    },
    select: function(event, ui) {
        $.youtubeAPI(ui.item.label);
    }
});
$('button#submit').click(function() {
    var value = $('input#youtube').val();
    $.youtubeAPI(value);
});
$.youtubeAPI = function(kelime) {
    var sonuc = $('#sonuc');
    sonuc.html('Searching...');
    $.ajax({
        type: 'GET',
        url: 'http://gdata.youtube.com/feeds/api/videos?q=' + kelime + '&max-results=15&v=2&alt=jsonc',
        dataType: 'jsonp',
        success: function(veri) {
            if (veri.data.items) {
                sonuc.empty();
                $.each(veri.data.items, function(i, data) {
                    sonuc.append('<div class="youtube">\
                        <img src="' + data.thumbnail.sqDefault + '" alt="" />\
                        <h3><a href="javascript:void(0)" onclick="$.youtubePlay(\'' + data.id + '\')">' + data.title + '</a></h3>\
                    </div>');
                });
            }
            else {
                sonuc.html('<div class="hata"><strong>' + kelime + '</strong> ile ilgili hiç video bulunamadı!</div>');
            }
        }
    });
}
$.youtubePlay = function(yid) {
    console.log(yid);
    $.ajax({
        url: '/api/add_video/' + party_token + "/" + yid + "/" + user_token + "/",
    })
}