function loadData() {

    var cityStr = $('#city').val();
    $('.grid').innerHTML = "";
    _500px.init({
        sdk_key: '263c9111787193d930ce0aa02f6e353ed5928fad' //replace with your js sdk key
    });

    // Get my user id
    _500px.api('/photos/search', { term: cityStr, image_size: 4, page: 1 }, function(response) {
        console.log(response.data.photos);
        var siteurl = "http://500px.com/photo/";
        var mapUrl = "https://www.google.com/maps/@";
        if (response.success) {
            $.each(response.data.photos, function() {
                $('.grid').append('<div class="grid-item contain"><h5>' + '</h5><a href="' + siteurl + this.id + '" target="_blank"><img src="'+ this.image_url + '" class="image" width="99%"/>' +
                    '<div class="middle">'+
                        '<div class="text glyphicon glyphicon-map-marker"><a href="https://www.google.co.jp/maps/?q=' + this.latitude + ',' + this.longitude + '" target="_blank"> Map</a></div>'+
                        '<div class="text glyphicon glyphicon-save"><a href="#"> Save</a></div>'+
                    '</div>'+
                    '</div>');

            });
            // $('#grid').masonry({
            //     // options...
            //     itemSelector: '.grid-item',
            //     columnWidth: 200
            // });
        } else {
            alert('Nothing found! Please refresh...');
        }
    });

    return false;
};

$('#form-container').submit(loadData);