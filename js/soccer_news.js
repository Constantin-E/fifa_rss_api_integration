console.log("hello there")

$(document).ready(function () {
    $('#refresh').click(getNewsList);

});

var getNewsList = function () {
    var serverStuff = "";
    $.ajax({
        type: "GET",
        dataType: 'json',
        url: 'http://localhost:7007/getNews',
        success: function (msg) {
            console.log("success: " + msg);
            articleList = msg;
            console.log(articleList);
            $('#news-list').empty();
            for (var i = 0; i < articleList.length; i++) {
                let bullet = $('<li/>');
                let article = $('<a/>');
                article.text(articleList[i]["title"])
                    .attr("href", articleList[i]["link"])
                    .appendTo(bullet);
                bullet.appendTo($('#news-list'));
            }
        },
        error: function (msg) {
            console.log("error: " + msg);
        },
    });
}
