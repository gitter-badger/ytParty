/**
 * Created by leonid <> on 23.11.14.
 */
$.youtubeAppend = function(token, destinaton_id, video_id, video_likes) {
    resp = $.ajax({
        type: "GET",
        url: 'http://gdata.youtube.com/feeds/api/videos/' + token + '?v=2&alt=jsonc',
        async: false
    }).responseText;
    resp = JSON.parse(resp);
    console.log(resp);
    if (video_id == undefined) {
        video_id = -1;
    }
    if (video_likes == undefined) {
        video_likes = 0;
    }
    console.log("Dane: " + token + " " + destinaton_id + " " + video_id + " " + video_likes);
    $('#' + destinaton_id).append('<div class="youtube"><input type="hidden" name="video_id" value="' + video_id + '"><input type="hidden" name="video_likes" value="' + video_likes + '"><img src="' + resp.data.thumbnail.sqDefault + '" alt="" /><h3><a href="javascript:void(0)" onclick="$.youtubePlay(\'' + resp.data.id + '\')">' + resp.data.title + '</a></h3></div>');
    $('#youtube_list').html("LOOOL");
};
