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
                $.youtubeAPI(data[1][0][0]);
            }
        });
    }
});
$.youtubeAPI = function(kelime) {
    var sonuc = $('#sonuc');
    sonuc.html('Searching...');
    $.ajax({
        type: 'GET',
        url: 'http://gdata.youtube.com/feeds/api/videos?q=' + kelime + '&max-results=15&v=2&alt=jsonc',
        dataType: 'jsonp',
        success: function(veri) {
            sonuc.empty();
            $.each(veri.data.items, function(i, data) {
                $.youtubeAppend(data.id, "sonuc");
            });
        }
    });
}
$.youtubePlay = function(yid) {
    $.ajax({url: '/api/add_video/' + party_token + "/" + yid + "/" + user_token + "/"})
}